import requests
import base64
import json
import geoip2.database
import re
import os
import socket

# تنظیمات
SUB_URL = "https://raw.githubusercontent.com/mahdibland/SSAggregator/master/sub/sub_merge.txt"
OUTPUT_DIR = "sub"  # پوشه خروجی
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

# تابع برای گرفتن کد کشور از آی‌پی
def get_country_code(ip, reader):
    try:
        response = reader.city(ip)
        return response.country.iso_code
    except Exception:
        with open(LOG_FILE, "a") as f:
            f.write(f"GeoIP error for IP {ip}\n")
        return None

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

    # دیکشنری برای ذخیره کانکشن‌ها بر اساس کشور
    country_connections = {}
    domains = 0

    # فیلتر کردن کانکشن‌ها بر اساس کشور
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

            country_code = get_country_code(ip, reader)
            if country_code:  # فقط اگه کد کشور معتبر باشه
                if country_code not in country_connections:
                    country_connections[country_code] = []
                country_connections[country_code].append(conn)

    # ذخیره کانکشن‌ها در فایل‌های جداگانه
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for country_code, conns in country_connections.items():
        output_file = f"{OUTPUT_DIR}/{country_code.lower()}_only_sub.txt"
        with open(output_file, "w") as f:
            f.write("\n".join(conns))
        with open(LOG_FILE, "a") as f:
            f.write(f"Saved {len(conns)} connections for {country_code} to {output_file}\n")

    with open(LOG_FILE, "a") as f:
        f.write(f"Processed {domains} domains, Found {sum(len(conns) for conns in country_connections.values())} total connections\n")

    # بستن دیتابیس GeoIP
    reader.close()

if __name__ == "__main__":
    main()
