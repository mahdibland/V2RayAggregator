import requests
import geoip2.database
import os
import tarfile
import time
from datetime import datetime
import yaml # کتابخانه جدید برای خواندن فایل کانفیگ
from utils import extract_ip_from_connection, resolve_to_ip

# --- Load Configuration ---
with open("config.yml", "r") as f:
    config = yaml.safe_load(f)

# --- Constants from Config File ---
SUB_URL = config['paths']['merged_configs']
OUTPUT_DIR = config['paths']['output_dir']
GEOIP_DB = config['paths']['geoip_database']
GEOIP_URL = config['urls']['geoip_download']
MAXMIND_LICENSE_KEY = os.getenv("MAXMIND_LICENSE_KEY")
TEST_URL = config['urls']['http_test']
LOG_FILE = config['paths']['http_log']
COUNTRIES = config['countries']
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
# --- End of Constants ---

def download_geoip_database():
    # ... (این تابع بدون تغییر باقی می‌ماند) ...
    if not MAXMIND_LICENSE_KEY: print("Error: MAXMIND_LICENSE_KEY not set."); return False
    try:
        url = GEOIP_URL.format(MAXMIND_LICENSE_KEY)
        print("Downloading fresh GeoIP database from MaxMind...")
        response = requests.get(url, timeout=30); response.raise_for_status()
        with open("GeoLite2-City.tar.gz", "wb") as f: f.write(response.content)
        with tarfile.open("GeoLite2-City.tar.gz", "r:gz") as tar:
            db_member = next((m for m in tar.getmembers() if m.name.endswith(GEOIP_DB)), None)
            if db_member is None: return False
            db_member.name = os.path.basename(db_member.name); tar.extract(db_member, path=".")
            os.rename(db_member.name, GEOIP_DB)
        os.remove("GeoLite2-City.tar.gz"); print(f"✅ GeoIP database successfully downloaded.")
        return True
    except Exception as e: print(f"An error occurred during GeoIP download: {e}"); return False


def get_country_code(ip, reader):
    # ... (این تابع بدون تغییر باقی می‌ماند) ...
    try: return reader.city(ip).country.iso_code
    except Exception: return None

def test_service_access(ip):
    # ... (این تابع بدون تغییر باقی می‌ماند) ...
    try:
        response = requests.head(TEST_URL, headers=HEADERS, timeout=5, allow_redirects=True)
        return response.status_code in (200, 301, 302)
    except requests.RequestException: return False

def main():
    if not os.path.exists(GEOIP_DB):
        print(f"GeoIP database not found in cache. Attempting to download...")
        if not download_geoip_database():
            print("❌ ERROR: Failed to download GeoIP database. Cannot continue.")
            exit(1)

    try:
        reader = geoip2.database.Reader(GEOIP_DB)
        print("✅ Successfully loaded GeoIP database.")
    except Exception as e:
        print(f"❌ ERROR: Could not read '{GEOIP_DB}'. It might be corrupt. {e}")
        exit(1)

    if not os.path.exists(SUB_URL):
        print(f"Source file '{SUB_URL}' not found. Skipping country exportation.")
        return

    with open(SUB_URL, 'r', encoding='utf-8') as f:
        connections = f.read().strip().splitlines()

    country_connections = {country_code: [] for country_code in COUNTRIES}

    for conn in connections:
        host = extract_ip_from_connection(conn)
        if host:
            ip = resolve_to_ip(host)
            if ip:
                country_code = get_country_code(ip, reader)
                if country_code in COUNTRIES and test_service_access(ip):
                    country_connections[country_code].append(conn)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(LOG_FILE, "w") as f:
        f.write(f"Log generated at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        for country_code, country_info in COUNTRIES.items():
            filename = country_info['sub_file']
            output_path = os.path.join(OUTPUT_DIR, filename)
            with open(output_path, "w") as out_f:
                out_f.write("\n".join(country_connections[country_code]))
            log_msg = f"Saved {len(country_connections[country_code])} configs for {country_code} to {output_path}\n"
            f.write(log_msg)
            print(log_msg.strip())

    reader.close()
    print("Process finished successfully.")

if __name__ == "__main__":
    main()
