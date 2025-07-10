import requests
import base64
import json
import geoip2.database
import re
import os
import socket

# تنظیمات
SUB_URL = "https://raw.githubusercontent.com/MEHR1DAD/V2RayAggregator/refs/heads/master/merged_configs.txt"
OUTPUT_FILE = "sub/us_only_sub.txt"  # فایل خروجی
GEOIP_DB = "GeoLite2-City.mmdb"  # مسیر دیتابیس GeoLite2
TEST_URL = "https://labs.google/"  # URL جدید برای تست HTTP
LOG_FILE = "http_test.log"  # فایل لاگ برای عیب‌یابی
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.google.com/"
}

# تابع برای گرفتن آی‌پی یا دامنه از لینک کانکشن
def extract_ip_from_connection(connection):
    try:
        if not connection or not isinstance(connection, str):
            with open(LOG_FILE, "a") as f:
                f.write(f"Invalid connection: {connection}\n")
            return None

        if connection.startswith("vmess://"):
            decoded = base64.b64decode(connection.split("vmess://")[1]).decode("utf-8")
            config = json.loads(decoded)
            host = config.get("add")
            if not host or host.strip() == ".":
                with open(LOG_FILE, "a") as f:
                    f.write(f"Invalid host in vmess://: {host}\n")
                return None
            return host
        elif connection.startswith(("vless://", "trojan://", "hysteria://", "hysteria2://", "tuic://")):
            server = connection.split("@")[1].split("?")[0].split(":")[0]
            if not server or server.strip() == ".":
                with open(LOG_FILE, "a") as f:
                    f.write(f"Invalid server in {connection.split('://')[0]}://: {server}\n")
                return None
            return server
        elif connection.startswith(("ss://", "ssr://")):
            server = re.search(r"@([\w\.\-]+):", connection)
            if server:
                host = server.group(1)
                if not host or host.strip() == ".":
                    with open(LOG_FILE, "a") as f:
                        f.write(f"Invalid server in {connection.split('://')[0]}://: {host}\n")
                    return None
                return host
            return None
        elif connection.startswith("brook://"):
            server = connection.split("@")[1].split(":")[0]
            if not server or server.strip() == ".":
                with open(LOG_FILE, "a") as f:
                    f.write(f"Invalid server in brook://: {server}\n")
                return None
            return server
        elif connection.startswith(("socks://", "http://")):
            server = connection.split("://")[1].split(":")[0]
            if not server or server.strip() == ".":
                with open(LOG_FILE, "a") as f:
                    f.write(f"Invalid server in {connection.split('://')[0]}://: {server}\n")
                return None
            return server
        elif connection.startswith("wireguard://"):
            server = connection.split("@")[1].split(":")[0]
            if not server or server.strip() == ".":
                with open(LOG_FILE, "a") as f:
                    f.write(f"Invalid server in wireguard://: {server}\ grano")
                return None
            return server
        return None
    except Exception as e:
        with open(LOG_FILE, "a") as f:
            f.write(f"Error parsing connection {connection}: {e}\n")
        return None

# تابع برای تبدیل دامنه به آی‌پی
def resolve_to_ip(host):
    if not host or not isinstance(host, str) or host.strip() == ".":
        with open(LOG_FILE, "a") as f:
            f.write(f"Invalid host for DNS resolution: {host}\n")
        return None
    try:
        ip = socket.gethostbyname(host)
        with open(LOG_FILE, "a") as f:
            f.write(f"Resolved {host} to {ip}\n")
        return ip
    except socket.gaierror as e:
        with open(LOG_FILE, "a") as f:
            f.write(f"DNS resolution error for {host}: {e}\n")
        return None

# تابع برای چک کردن موقعیت آی‌پی
def is_us_ip(ip, reader):
    try:
        response = reader.city(ip)
        return response.country.iso_code == "US"
    except Exception:
        with open(LOG_FILE, "a") as f:
            f.write(f"GeoIP error for IP {ip}\n")
        return False

# تابع برای تست دسترسی به سرویس
def test_service_access(ip):
    try:
        response = requests.head(TEST_URL, headers=HEADERS, timeout=5, allow_redirects=True)
        result = response.status_code in (200, 301, 302)
        with open(LOG_FILE, "a") as f:
            f.write(f"HTTP test {ip}: {'Success' if result else 'Failed'} (Status: {response.status_code})\n")
        return result
    except requests.RequestException as e:
        with open(LOG_FILE, "a") as f:
            f.write(f"HTTP error for {ip}: {e}\n")
        return False

def main():
    # باز کردن فایل لاگ
    with open(LOG_FILE, "w") as f:
        f.write(f"Starting HTTP test log at {os.popen('date').read()}\n")

    # گرفتن لیست کانکشن‌ها از لینک خام
    try:
        response = requests.get(SUB_URL, timeout=10)
        response.raise_for_status()
        connections = response.text.strip().splitlines()
        with open(LOG_FILE, "a") as f:
            f.write(f"Fetched {len(connections)} connections from {SUB_URL}\n")
    except requests.RequestException as e:
        with open(LOG_FILE, "a") as f:
            f.write(f"Error fetching {SUB_URL}: {e}\n")
        return

    # باز کردن دیتابیس GeoIP
    try:
        reader = geoip2.database.Reader(GEOIP_DB)
    except Exception as e:
        with open(LOG_FILE, "a") as f:
            f.write(f"Error opening GeoIP database: {e}\n")
        return

    # فیلتر کردن کانکشن‌های مربوط به آمریکا
    us_connections = []
    us_ips = 0
    domains = 0
    for conn in connections:
        host = extract_ip_from_connection(conn)
        if host:
            # چک کردن اینکه ورودی آی‌پی است یا دامنه
            if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", host):
                ip = host
            else:
                domains += 1
                ip = resolve_to_ip(host)
                if not ip:
                    continue

            if is_us_ip(ip, reader):
                us_ips += 1
                if test_service_access(ip):
                    us_connections.append(conn)
                else:
                    with open(LOG_FILE, "a") as f:
                        f.write(f"Skipping {ip}: Failed HTTP test\n")

    with open(LOG_FILE, "a") as f:
        f.write(f"Processed {domains} domains, Found {us_ips} US IPs, Saved {len(us_connections)} connections\n")

    # ذخیره کانکشن‌ها در فایل
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        f.write("\n".join(us_connections))

    with open(LOG_FILE, "a") as f:
        f.write(f"Saved {len(us_connections)} US connections to {OUTPUT_FILE}\n")

    # بستن دیتابیس GeoIP
    reader.close()

if __name__ == "__main__":
    main()
