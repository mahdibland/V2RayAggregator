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
PING_URL = "8.8.8.8"  # پینگ به سرور DNS گوگل
CACHE_FILE = "ip_cache.pkl"  # فایل کش برای نتایج تست
LOG_FILE = "ping_test.log"  # فایل لاگ برای عیب‌یابی

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
        with open(LOG_FILE, "a") as f:
            f.write(f"Error parsing connection: {e}\n")
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

# تابع برای تست پینگ
def test_ping(ip):
    try:
        with open(CACHE_FILE, "rb") as f:
            cache = pickle.load(f)
    except FileNotFoundError:
        cache = {}

    if f"{ip}_ping" in cache:
        result = cache[f"{ip}_ping"]
        with open(LOG_FILE, "a") as f:
            f.write(f"Cached ping result for {ip}: {'Success' if result else 'Failed'}\n")
        return result

    try:
        response = ping(PING_URL, count=2, timeout=2)  # 2 پینگ به 8.8.8.8 با تایم‌اوت 2 ثانیه
        result = response.success()
        cache[f"{ip}_ping"] = result
        with open(LOG_FILE, "a") as f:
            f.write(f"Ping {ip} to {PING_URL}: {'Success' if result else 'Failed'}\n")
    except Exception as e:
        with open(LOG_FILE, "a") as f:
            f.write(f"Ping error for {ip} to {PING_URL}: {e}\n")
        cache[f"{ip}_ping"] = False
        result = False

    with open(CACHE_FILE, "wb") as f:
        pickle.dump(cache, f)

    return result

def main():
    # باز کردن فایل لاگ
    with open(LOG_FILE, "w") as f:
        f.write(f"Starting ping test log at {os.popen('date').read()}\n")

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
    for conn in connections:
        ip = extract_ip_from_connection(conn)
        if ip and is_us_ip(ip, reader):
            us_ips += 1
            if test_ping(ip):
                us_connections.append(conn)
            else:
                with open(LOG_FILE, "a") as f:
                    f.write(f"Skipping {ip}: Failed ping test to {PING_URL}\n")

    with open(LOG_FILE, "a") as f:
        f.write(f"Found {us_ips} US IPs, {len(us_connections)} passed ping test\n")

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
