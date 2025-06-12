import requests
import base64
import json
import geoip2.database
import re
import os
import pickle
import socket
from pythonping import ping

# تنظیمات
SUB_URL = "https://raw.githubusercontent.com/mahdibland/SSAggregator/master/sub/sub_merge.txt"
OUTPUT_FILE = "sub/us_only_sub.txt"  # فایل خروجی
GEOIP_DB = "GeoLite2-City.mmdb"  # مسیر دیتابیس GeoLite2
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
        response = ping(ip, count=2, timeout=4)  # 2 پینگ با تایم‌اوت 4 ثانیه
        result = response.success()
        cache[f"{ip}_ping"] = result
        with open(LOG_FILE, "a") as f:
            f.write(f"Ping {ip}: {'Success' if result else 'Failed'}\n")
    except Exception as e:
        with open(LOG_FILE, "a") as f:
            f.write(f"Ping error for {ip}: {e}\n")
        cache[f"{ip}_ping"] = False
        result = False

    with open(CACHE_FILE, "wb") as f:
        pickle.dump(cache, f)

    return result

def main():
    # پاک کردن کش قدیمی
    if os.path.exists(CACHE_FILE):
        os.remove(CACHE_FILE)
        with open(LOG_FILE, "a") as f:
            f.write("Cleared old cache file\n")

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
                if test_ping(ip):
                    us_connections.append(conn)
                else:
                    with open(LOG_FILE, "a") as f:
                        f.write(f"Skipping {ip}: Failed ping test\n")

    with open(LOG_FILE, "a") as f:
        f.write(f"Processed {domains} domains, Found {us_ips} US IPs, {len(us_connections)} passed ping test\n")

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
