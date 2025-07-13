import requests
import base64
import json
import geoip2.database
import re
import os
import socket
import tarfile
import time
from datetime import datetime
from utils import extract_ip_from_connection, resolve_to_ip

# =================================================================================
# بخش تعریف متغیرهای سراسری (Constants)
# این بخش به بالای اسکریپت منتقل شد تا خطا برطرف شود
# =================================================================================
SUB_URL = "https://raw.githubusercontent.com/MEHR1DAD/V2RayAggregator/refs/heads/master/merged_configs.txt"
OUTPUT_DIR = "subscription"
GEOIP_DB = "GeoLite2-City.mmdb"
GEOIP_URL = "https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-City&license_key={}&suffix=tar.gz"
MAXMIND_LICENSE_KEY = os.getenv("MAXMIND_LICENSE_KEY")
TEST_URL = "https://labs.google.com/"
LOG_FILE = "http_test.log"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
COUNTRIES = {
    "US": "US_sub.txt", "NL": "NL_sub.txt", "DE": "DE_sub.txt",
    "GB": "GB_sub.txt", "FR": "FR_sub.txt", "CA": "CA_sub.txt",
    "TR": "TR_sub.txt", "AE": "AE_sub.txt", "SE": "SE_sub.txt",
    "IR": "IR_sub.txt"
}
# =================================================================================

def download_geoip_database():
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
    try: return reader.city(ip).country.iso_code
    except Exception: return None

def test_service_access(ip):
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

    try:
        response = requests.get(SUB_URL, timeout=10)
        response.raise_for_status()
        connections = response.text.strip().splitlines()
    except requests.RequestException as e:
        print(f"Error fetching subscription URL: {e}")
        return

    country_connections = {country: [] for country in COUNTRIES}
    for conn in connections:
        host = extract_ip_from_connection(conn)
        if host:
            ip = host if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", host) else resolve_to_ip(host)
            if ip:
                country_code = get_country_code(ip, reader)
                if country_code in COUNTRIES and test_service_access(ip):
                    country_connections[country_code].append(conn)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(LOG_FILE, "w") as f:
        f.write(f"Log generated at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        for country_code, filename in COUNTRIES.items():
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
