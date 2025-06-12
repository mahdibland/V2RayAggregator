import requests
import base64
import json
import geoip2.database
import re
import os
import socket

# تنظیمات
SUB_URL = "https://raw.githubusercontent.com/mahdibland/SSAggregator/master/sub/sub_merge.txt"
OUTPUT_FILE = "sub/us_only_sub.txt"  # فایل خروجی
GEOIP_DB = "GeoLite2-City.mmdb"  # مسیر دیتابیس GeoLite2
LOG_FILE = "geoip_test.log"  # فایل لاگ برای عیب‌یابی

# تابع برای گرفتن آی‌پی یا دامنه از لینک کانکشن
def extract_ip_from_connection(connection):
    try:
        if connection.startswith("vmess://"):
            decoded = base64.b64decode(connection.split("vmess://")[1]).decode("utf-8")
            config = json.loads(decoded)
            return config.get("add")
        elif connection.startswith("trojan://"):
            server = connection.split("@")[1].split("?")[0].split(":")[0]
            return server
        elif connection.startswith("ss://") or connection.startswith("ssr://"):
            server = re.search(r"@([\w\.\-]+):", connection)
            return server.group(1) if server else None
        return None
    except Exception as e:
        with open(LOG_FILE, "a") as f:
            f.write(f"Error parsing connection: {e}\n")
        return None

# تابع برای تبدیل دامنه به آی‌پی
def resolve_to_ip(host):
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

def main():
    # باز کردن فایل لاگ
    with open(LOG_FILE, "w") as f:
        f.write(f"Starting GeoIP test log at {os.popen('date').read()}\n")

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
                us_connections.append(conn)

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
