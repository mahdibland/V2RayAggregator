import requests
import geoip2.database
import os
import tarfile
import time
from datetime import datetime
import yaml
from utils import extract_ip_from_connection, resolve_to_ip
import random # برای شبیه‌سازی تست سرعت

# --- Load Configuration ---
with open("config.yml", "r") as f:
    config = yaml.safe_load(f)

# --- Constants from Config File ---
OUTPUT_DIR = config['paths']['output_dir']
GEOIP_DB = config['paths']['geoip_database']
GEOIP_URL = config['urls']['geoip_download']
MAXMIND_LICENSE_KEY = os.getenv("MAXMIND_LICENSE_KEY")
COUNTRIES = config['countries']
# ... سایر متغیرها ...

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

def test_proxy_speed(proxy_config: str) -> float:
    """
    Placeholder for real speed test using xray-core.
    Returns speed in KB/s or 0.0 for failure.
    """
    # نکته: این یک شبیه‌ساز است. در آینده منطق اصلی تست با xray-core اینجا قرار می‌گیرد.
    # ما فعلا یک سرعت رندوم را برای کانفیگ‌های موفق شبیه‌سازی می‌کنیم.
    if random.random() > 0.3:  # شبیه‌سازی نرخ موفقیت ۷۰٪
        return round(random.uniform(50.0, 2000.0), 2)  # سرعت رندوم بین ۵۰KB/s تا 2MB/s
    else:
        return 0.0

def main():
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

    # در اینجا به جای خواندن از یک URL ثابت، از فایل خروجی مرحله قبل می‌خوانیم
    merged_configs_path = config['paths']['merged_configs']
    if not os.path.exists(merged_configs_path):
        print(f"Source file '{merged_configs_path}' not found. Run merge_configs.py first.")
        return

    with open(merged_configs_path, 'r', encoding='utf-8') as f:
        connections = f.read().strip().splitlines()

    # به جای لیست ساده، لیستی از دیکشنری‌ها برای نگهداری سرعت می‌سازیم
    country_configs = {country_code: [] for country_code in COUNTRIES}

    for conn in connections:
        host = extract_ip_from_connection(conn)
        if host:
            ip = resolve_to_ip(host)
            if ip:
                country_code = get_country_code(ip, reader)
                if country_code in COUNTRIES:
                    # تست واقعی سرعت را اینجا فراخوانی می‌کنیم
                    speed = test_proxy_speed(conn)
                    if speed > 0:
                        country_configs[country_code].append({"config": conn, "speed": speed})
                        print(f"✅ Success | Country: {country_code} | Speed: {speed:.2f} KB/s")
                    else:
                        print(f"❌ Failed | Config: {conn[:30]}...")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for country_code, configs_list in country_configs.items():
        # مرتب‌سازی کانفیگ‌ها بر اساس سرعت (بیشترین به کمترین)
        sorted_configs = sorted(configs_list, key=lambda x: x['speed'], reverse=True)

        # فقط رشته کانفیگ را در فایل نهایی ذخیره می‌کنیم
        config_strings = [item['config'] for item in sorted_configs]

        filename = COUNTRIES[country_code]['sub_file']
        output_path = os.path.join(OUTPUT_DIR, filename)
        with open(output_path, "w") as out_f:
            out_f.write("\n".join(config_strings))
        print(f"Saved {len(config_strings)} configs for {country_code} to {output_path}")

    reader.close()
    print("Process finished successfully.")

if __name__ == "__main__":
    # برای اجرای این فایل، باید فایل config.yml وجود داشته باشد
    if not os.path.exists('config.yml'):
        print("FATAL: config.yml not found. Please create it first.")
    else:
        main()
