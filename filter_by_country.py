import requests
import base64
import json
import geoip2.database
import re
import os

# تنظیمات
SUB_URL = "https://raw.githubusercontent.com/mahdibland/SSAggregator/master/sub/sub_merge.txt"
OUTPUT_DIR = "sub"  # پوشه خروجی
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

# تابع برای گرفتن کد کشور از آی‌پی
def get_country_code(ip, reader):
    try:
        response = reader.city(ip)
        return response.country.iso_code
    except Exception:
        return None

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

    # دیکشنری برای ذخیره کانکشن‌ها بر اساس کشور
    country_connections = {}

    # فیلتر کردن کانکشن‌ها بر اساس کشور
    for conn in connections:
        ip = extract_ip_from_connection(conn)
        if ip:
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
        print(f"Saved {len(conns)} connections for {country_code} to {output_file}")

    # بستن دیتابیس GeoIP
    reader.close()

if __name__ == "__main__":
    main()