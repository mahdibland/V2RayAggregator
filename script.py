import requests
import base64
import json
import geoip2.database
import re
import os

# تنظیمات
SUB_URL = "https://raw.githubusercontent.com/mahdibland/SSAggregator/master/sub/sub_merge.txt"
OUTPUT_FILE = "sub/us_only_sub.txt"  # فایل خروجی
GEOIP_DB = "GeoLite2-City.mmdb"  # مسیر دیتابیس GeoLite2

# تابع برای گرفتن آی‌پی از لینک کانکشن
def extract_ip_from_connection(connection):
    try:
        # برای پروتکل‌های مختلف (ss, ssr, vmess, trojan, vless)
        if connection.startswith("vmess://"):
            decoded = base64.b64decode(connection.split("vmess://")[1]).decode("utf-8")
            config = json.loads(decoded)
            return config.get("add")
        elif connection.startswith("trojan://"):
            server = connection.split("@")[1].split("?")[0].split(":")[0]
            return server
        elif connection.startswith("ss://") or connection.startswith("ssr://"):
            # فرمت ss/ssr: ss://<method>:<password>@<server>:<port>
            server = re.search(r"@([\w\.\-]+):", connection)
            return server.group(1) if server else None
        return None
    except Exception as e:
        print(f"Error parsing connection: {e}")
        return None

# تابع برای چک کردن موقعیت آی‌پی
def is_us_ip(ip, reader):
    try:
        response = reader.city(ip)
        return response.country.iso_code == "US"
    except Exception:
        return False

def main():
    # گرفتن لیست کانکشن‌ها از لینک خام
    try:
        response = requests.get(SUB_URL, timeout=10)
        response.raise_for_status()
        connections = response.text.strip().splitlines()
    except requests.RequestException as e:
        print(f"Error fetching {SUB_URL}: {e}")
        return

    # باز کردن دیتابیس GeoIP
    reader = geoip2.database.Reader(GEOIP_DB)

    # فیلتر کردن کانکشن‌های مربوط به آمریکا
    us_connections = []
    for conn in connections:
        ip = extract_ip_from_connection(conn)
        if ip and is_us_ip(ip, reader):
            us_connections.append(conn)

    # ذخیره کانکشن‌ها در فایل
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        f.write("\n".join(us_connections))

    # بستن دیتابیس GeoIP
    reader.close()

if __name__ == "__main__":
    main()
