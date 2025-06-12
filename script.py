import requests
import base64
import json
import geoip2.database
import re
import os
import pickle
from pythonping import ping

# تنظیمات
SUB_URL = "https://raw.githubusercontent.com/mahdibland/SSAggregator/master/sub/sub_merge.txt"
OUTPUT_FILE = "sub/us_only_sub.txt"  # فایل خروجی
GEOIP_DB = "GeoLite2-City.mmdb"  # مسیر دیتابیس GeoLite2
TEST_URL = "https://labs.google/fx/tools/image-fx"
PING_URL = "cp.cloudflare.com"
CACHE_FILE = "ip_cache.pkl"  # فایل کش برای نتایج تست
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124"
}

# تابع برای گرفتن آی‌پی از لینک کانکشن
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
        print(f"Error parsing connection: {e}")
        return None

# تابع برای چک کردن موقعیت آی‌پی
def is_us_ip(ip, reader):
    try:
        response = reader.city(ip)
        return response.country.iso_code == "US"
    except Exception:
        return False

# تابع برای تست پینگ
def test_ping(ip):
    try:
        with open(CACHE_FILE, "rb") as f:
            cache = pickle.load(f)
    except FileNotFoundError:
        cache = {}

    if f"{ip}_ping" in cache:
        print(f"Using cached ping result for {ip}: {cache[f'{ip}_ping']}")
        return cache[f"{ip}_ping"]

    try:
        response = ping(ip, count=2, timeout=2)  # 2 پینگ با تایم‌اوت 2 ثانیه
        result = response.success()
        cache[f"{ip}_ping"] = result
        print(f"Ping {ip}: {'Success' if result else 'Failed'}")
    except Exception as e:
        print(f"Ping error for {ip}: {e}")
        cache[f"{ip}_ping"] = False
        result = False

    with open(CACHE_FILE, "wb") as f:
        pickle.dump(cache, f)

    return result

# تابع برای تست دسترسی به سرویس
def test_service_access(ip):
    try:
        with open(CACHE_FILE, "rb") as f:
            cache = pickle.load(f)
    except FileNotFoundError:
        cache = {}

    if f"{ip}_http" in cache:
        print(f"Using cached HTTP result for {ip}: {cache[f'{ip}_http']}")
        return cache[f"{ip}_http"]

    try:
        response = requests.head(TEST_URL, headers=HEADERS, timeout=5, allow_redirects=True)
        result = response.status_code in (200, 301, 302)
        cache[f"{ip}_http"] = result
        print(f"HTTP test {ip}: {'Success' if result else 'Failed'} (Status: {response.status_code})")
    except requests.RequestException as e:
        print(f"HTTP error for {ip}: {e}")
        cache[f"{ip}_http"] = False
        result = False

    with open(CACHE_FILE, "wb") as f:
        pickle.dump(cache, f)

    return result

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
            # مرحله 1: تست پینگ
            if not test_ping(ip):
                print(f"Skipping {ip}: Failed ping test")
                continue
            # مرحله 2: تست سرویس
            if test_service_access(ip):
                us_connections.append(conn)
            else:
                print(f"Skipping {ip}: Failed service test")

    # ذخیره کانکشن‌ها در فایل
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        f.write("\n".join(us_connections))

    print(f"Saved {len(us_connections)} US connections to {OUTPUT_FILE}")

    # بستن دیتابیس GeoIP
    reader.close()

if __name__ == "__main__":
    main()
