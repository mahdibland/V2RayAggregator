import requests
import base64
import json
import geoip2.database
import re
import os
import socket
import tarfile
import time
from datetime import datetime, timedelta

# تنظیمات
SUB_URL = "https://raw.githubusercontent.com/MEHR1DAD/V2RayAggregator/refs/heads/master/merged_configs.txt"
OUTPUT_DIR = "subscription"
GEOIP_DB = "GeoLite2-City.mmdb"
GEOIP_URL = "https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-City&license_key={}&suffix=tar.gz"
MAXMIND_LICENSE_KEY = os.getenv("MAXMIND_LICENSE_KEY")
TEST_URL = "https://labs.google.com/"
LOG_FILE = "http_test.log"
CACHE_DURATION = 24 * 60 * 60  # کش برای ۲۴ ساعت (به ثانیه)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
COUNTRIES = {
    "US": "US_sub.txt", "NL": "NL_sub.txt", "DE": "DE_sub.txt",
    "GB": "UK_sub.txt", "FR": "FR_sub.txt", "CA": "CA_sub.txt",
    "TR": "TR_sub.txt", "AE": "UE_sub.txt", "SE": "SE_sub.txt"
}

# تابع دانلود دیتابیس (بدون تغییر)
def download_geoip_database():
    if not MAXMIND_LICENSE_KEY:
        print("Error: MAXMIND_LICENSE_KEY not set. Cannot download.")
        return False
    try:
        url = GEOIP_URL.format(MAXMIND_LICENSE_KEY)
        print("Downloading fresh GeoIP database from MaxMind...")
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        with open("GeoLite2-City.tar.gz", "wb") as f:
            f.write(response.content)
        print("Download complete. Extracting...")
        with tarfile.open("GeoLite2-City.tar.gz", "r:gz") as tar:
            db_member = next((m for m in tar.getmembers() if m.name.endswith("GeoLite2-City.mmdb")), None)
            if db_member is None:
                print("Error: Could not find .mmdb file in the archive.")
                return False
            db_member.name = os.path.basename(db_member.name)
            tar.extract(db_member, path=".")
            os.rename(db_member.name, GEOIP_DB)
        os.remove("GeoLite2-City.tar.gz")
        print(f"✅ GeoIP database successfully updated to {GEOIP_DB}")
        return True
    except Exception as e:
        print(f"An error occurred during GeoIP download: {e}")
        return False

# توابع extract_ip_from_connection, resolve_to_ip, get_country_code, test_service_access
# این توابع بدون تغییر باقی می‌مانند. آن‌ها را از اسکریپت قبلی خود کپی کنید یا اینجا نگه دارید.

def extract_ip_from_connection(connection):
    # (کد این تابع بدون تغییر است)
    try:
        if not connection or not isinstance(connection, str): return None
        if not re.match(r"^(vmess|vless|trojan|ss)://", connection): return None
        if connection.startswith("vmess://"):
            decoded = base64.b64decode(connection.split("vmess://")[1]).decode("utf-8")
            return json.loads(decoded).get("add")
        elif connection.startswith(("vless://", "trojan://")):
            return connection.split("@")[1].split("?")[0].split(":")[0]
        elif connection.startswith("ss://"):
            server = re.search(r"@([\w\.\-]+):", connection)
            return server.group(1) if server else None
    except Exception:
        return None
    return None

def resolve_to_ip(host):
    # (کد این تابع بدون تغییر است)
    try: return socket.gethostbyname(host)
    except socket.gaierror: return None

def get_country_code(ip, reader):
    # (کد این تابع بدون تغییر است)
    try: return reader.city(ip).country.iso_code
    except Exception: return None

def test_service_access(ip):
    # (کد این تابع بدون تغییر است)
    try:
        response = requests.head(TEST_URL, headers=HEADERS, timeout=5, allow_redirects=True)
        return response.status_code in (200, 301, 302)
    except requests.RequestException:
        return False

# تابع اصلی با منطق جدید
def main():
    with open(LOG_FILE, "w") as f:
        f.write(f"Starting process at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # --- منطق جدید برای مدیریت دیتابیس GeoIP ---
    needs_download = False
    if not os.path.exists(GEOIP_DB):
        print(f"'{GEOIP_DB}' not found. Will try to download.")
        needs_download = True
    elif time.time() - os.path.getmtime(GEOIP_DB) > CACHE_DURATION:
        print(f"GeoIP database is older than 24 hours. Will try to update.")
        needs_download = True
    else:
        print("✅ Using existing GeoIP database (cache is fresh).")

    if needs_download:
        if not download_geoip_database():
            print("⚠️ WARNING: Failed to download new GeoIP database. Will use the existing file if available.")
    
    # --- بررسی نهایی قبل از اجرا ---
    if not os.path.exists(GEOIP_DB):
        print(f"❌ ERROR: GeoIP database '{GEOIP_DB}' is missing and download failed. Cannot continue.")
        return

    # ادامه اسکریپت...
    try:
        reader = geoip2.database.Reader(GEOIP_DB)
        print("Successfully loaded GeoIP database.")
    except Exception as e:
        print(f"❌ ERROR: Could not read '{GEOIP_DB}'. It might be corrupt. {e}")
        return

    try:
        response = requests.get(SUB_URL, timeout=10)
        response.raise_for_status()
        connections = response.text.strip().splitlines()
    except requests.RequestException as e:
        print(f"Error fetching subscription URL: {e}")
        return

    country_connections = {country: [] for country in COUNTRIES}
    
    # ... (بقیه حلقه for برای پردازش کانفیگ‌ها بدون تغییر است) ...
    for conn in connections:
        host = extract_ip_from_connection(conn)
        if host:
            ip = host if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", host) else resolve_to_ip(host)
            if ip:
                country_code = get_country_code(ip, reader)
                if country_code in COUNTRIES and test_service_access(ip):
                    country_connections[country_code].append(conn)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for country_code, filename in COUNTRIES.items():
        output_path = os.path.join(OUTPUT_DIR, filename)
        with open(output_path, "w") as f:
            f.write("\n".join(country_connections[country_code]))
        print(f"Saved {len(country_connections[country_code])} configs for {country_code} to {output_path}")
    
    reader.close()
    print("Process finished successfully.")

if __name__ == "__main__":
    main()
