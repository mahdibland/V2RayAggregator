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

# تمام ثابت‌ها و توابع دیگر بدون تغییر باقی می‌مانند
# ...

# --- تابع اصلاح شده برای استخراج آدرس سرور ---
def extract_ip_from_connection(connection: str) -> str | None:
    if not connection or not isinstance(connection, str):
        return None
    
    host = None
    try:
        if connection.startswith("vmess://"):
            encoded_part = connection.split("vmess://")[1]
            padding = len(encoded_part) % 4
            if padding: encoded_part += "=" * (4 - padding)
            config = json.loads(base64.b64decode(encoded_part).decode("utf-8"))
            host = config.get("add")
        elif connection.startswith(("vless://", "trojan://", "tuic://", "hysteria2://", "wireguard://")):
            host = connection.split("@")[1].split("?")[0].split("#")[0].split(":")[0]
        elif connection.startswith(("ss://", "brook://")):
            if "@" in connection:
                match = re.search(r"@([\w\.\-]+):", connection)
                if match: host = match.group(1)
            else:
                encoded_part = connection.split("://")[1].split("#")[0]
                padding = len(encoded_part) % 4
                if padding: encoded_part += "=" * (4 - padding)
                decoded_part = base64.b64decode(encoded_part).decode("utf-8")
                host = decoded_part.split("@")[1].split(":")[0]
        elif connection.startswith("ssr://"):
            encoded_part = connection.split("ssr://")[1]
            padding = len(encoded_part) % 4
            if padding: encoded_part += "=" * (4 - padding)
            decoded_part = base64.b64decode(encoded_part).decode("utf-8")
            host = decoded_part.split(":")[0]
        elif connection.startswith(("hysteria://", "socks://", "http://")):
            address_part = connection.split("://")[1]
            if "@" in address_part: address_part = address_part.split("@")[1]
            host = address_part.split(":")[0]
    except Exception:
        return None
    
    # اطمینان حاصل شود که خروجی خالی برگردانده نمی‌شود
    return host if host else None


# --- تابع اصلاح شده برای پیدا کردن IP ---
def resolve_to_ip(host: str) -> str | None:
    # جلوگیری از ارسال هاست خالی یا None به تابع
    if not host or not isinstance(host, str):
        return None
    try:
        return socket.gethostbyname(host)
    except (socket.gaierror, UnicodeError):
        # نادیده گرفتن خطاهای DNS و Unicode
        return None

#
# (بقیه توابع و main() بدون تغییر باقی می‌مانند)
#
def download_geoip_database():
    if not MAXMIND_LICENSE_KEY: print("Error: MAXMIND_LICENSE_KEY not set."); return False
    try:
        url = GEOIP_URL.format(MAXMIND_LICENSE_KEY)
        print("Downloading fresh GeoIP database from MaxMind...")
        response = requests.get(url, timeout=30); response.raise_for_status()
        with open("GeoLite2-City.tar.gz", "wb") as f: f.write(response.content)
        with tarfile.open("GeoLite2-City.tar.gz", "r:gz") as tar:
            db_member = next((m for m in tar.getmembers() if m.name.endswith("GeoLite2-City.mmdb")), None)
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
    # (بقیه تابع main بدون تغییر است)
    SUB_URL = "https://raw.githubusercontent.com/MEHR1DAD/V2RayAggregator/refs/heads/master/merged_configs.txt"
    OUTPUT_DIR = "subscription"
    LOG_FILE = "http_test.log"
    COUNTRIES = {
        "US": "US_sub.txt", "NL": "NL_sub.txt", "DE": "DE_sub.txt",
        "GB": "UK_sub.txt", "FR": "FR_sub.txt", "CA": "CA_sub.txt",
        "TR": "TR_sub.txt", "AE": "UE_sub.txt", "SE": "SE_sub.txt"
    }
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
