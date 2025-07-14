import geoip2.database
import os
import tarfile
from datetime import datetime
import yaml 
from utils import extract_ip_from_connection, resolve_to_ip
import random
# توابع دیتابیس را وارد می‌کنیم
from database import initialize_db, bulk_update_configs

# --- Load Configuration ---
with open("config.yml", "r") as f:
    config = yaml.safe_load(f)

# --- Constants from Config File ---
GEOIP_DB = config['paths']['geoip_database']
GEOIP_URL = config['urls']['geoip_download']
MAXMIND_LICENSE_KEY = os.getenv("MAXMIND_LICENSE_KEY")
COUNTRIES = config['countries']

# ... (توابع download_geoip_database و get_country_code و test_proxy_speed بدون تغییر هستند) ...
def download_geoip_database():
    if not MAXMIND_LICENSE_KEY: print("Error: MAXMIND_LICENSE_KEY not set."); return False
    # ... (full function code)
    try:
        url = GEOIP_URL.format(MAXMIND_LICENSE_KEY)
        print("Downloading fresh GeoIP database from MaxMind...")
        # ... (rest of the function)
        return True
    except Exception as e:
        print(f"An error occurred during GeoIP download: {e}")
        return False

def get_country_code(ip, reader):
    try:
        return reader.city(ip).country.iso_code
    except geoip2.errors.AddressNotFoundError:
        return None
    except Exception:
        return None

def test_proxy_speed(proxy_config: str) -> float:
    # Placeholder for real speed test
    if random.random() > 0.3:
        return round(random.uniform(50.0, 2000.0), 2)
    else:
        return 0.0

def main():
    # 1. اطمینان از وجود دیتابیس و جداول
    initialize_db()

    if not os.path.exists(GEOIP_DB):
        print(f"GeoIP database not found, downloading...")
        if not download_geoip_database():
            print("❌ ERROR: Failed to download GeoIP database.")
            exit(1)

    try:
        reader = geoip2.database.Reader(GEOIP_DB)
    except Exception as e:
        print(f"❌ ERROR: Could not read '{GEOIP_DB}'.")
        exit(1)

    merged_configs_path = config['paths']['merged_configs']
    if not os.path.exists(merged_configs_path):
        print(f"Source file '{merged_configs_path}' not found. Run merge_configs.py first.")
        return

    with open(merged_configs_path, 'r', encoding='utf-8') as f:
        connections = f.read().strip().splitlines()

    # لیستی برای نگهداری تمام نتایج موفق
    successful_configs_data = []
    now = datetime.utcnow().isoformat()

    for conn in connections:
        host = extract_ip_from_connection(conn)
        if host:
            ip = resolve_to_ip(host)
            if ip:
                country_code = get_country_code(ip, reader)
                # ما فقط کانفیگ‌هایی را تست می‌کنیم که کشورشان برای ما مهم است
                if country_code in COUNTRIES:
                    speed = test_proxy_speed(conn)
                    if speed > 0:
                        # افزودن نتیجه موفق به لیست برای ذخیره در دیتابیس
                        successful_configs_data.append(
                            (conn, 'unknown', country_code, speed, now)
                        )
                        print(f"✅ Success | Country: {country_code} | Speed: {speed:.2f} KB/s")
                    else:
                        print(f"❌ Failed | Config: {conn[:30]}...")

    # 2. ذخیره تمام نتایج موفق در دیتابیس به صورت یکجا
    if successful_configs_data:
        print(f"\nSaving {len(successful_configs_data)} tested configs to database...")
        bulk_update_configs(successful_configs_data)
    else:
        print("\nNo new working configs found to save.")

    reader.close()
    print("\nProcess finished successfully.")

if __name__ == "__main__":
    if not os.path.exists('config.yml'):
        print("FATAL: config.yml not found. Please create it first.")
    else:
        main()
