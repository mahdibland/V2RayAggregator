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

# تنظیمات (بدون تغییر)
SUB_URL = "https://raw.githubusercontent.com/MEHR1DAD/V2RayAggregator/refs/heads/master/merged_configs.txt"
OUTPUT_DIR = "subscription"
GEOIP_DB = "GeoLite2-City.mmdb"
GEOIP_URL = "https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-City&license_key={}&suffix=tar.gz"
MAXMIND_LICENSE_KEY = os.getenv("MAXMIND_LICENSE_KEY")
TEST_URL = "https://labs.google.com/"
LOG_FILE = "http_test.log"
CACHE_DURATION = 24 * 60 * 60  # 24 hours
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
COUNTRIES = {
    "US": "US_sub.txt", "NL": "NL_sub.txt", "DE": "DE_sub.txt",
    "GB": "UK_sub.txt", "FR": "FR_sub.txt", "CA": "CA_sub.txt",
    "TR": "TR_sub.txt", "AE": "UE_sub.txt", "SE": "SE_sub.txt"
}

# ----------------------------------------------------------------------------------
# تابع جدید و هوشمند برای استخراج آدرس سرور از تمام پروتکل‌ها
def extract_ip_from_connection(connection: str) -> str | None:
    """
    Parses various proxy protocols to extract the server address (IP or domain).
    """
    if not connection or not isinstance(connection, str):
        return None

    try:
        # vmess
        if connection.startswith("vmess://"):
            encoded_part = connection.split("vmess://")[1]
            padding = len(encoded_part) % 4
            if padding:
                encoded_part += "=" * (4 - padding)
            decoded_json = base64.b64decode(encoded_part).decode("utf-8")
            config = json.loads(decoded_json)
            return config.get("add")

        # vless, trojan, tuic, hysteria2, wireguard (user@server:port)
        elif connection.startswith(("vless://", "trojan://", "tuic://", "hysteria2://", "wireguard://")):
            return connection.split("@")[1].split("?")[0].split("#")[0].split(":")[0]

        # ss, brook (can have @ or be fully encoded)
        elif connection.startswith(("ss://", "brook://")):
            # Format: protocol://<user-info>@<server>:<port>
            if "@" in connection:
                return re.search(r"@([\w\.\-]+):", connection).group(1)
            # Format: ss://<base64_full_config>
            else:
                encoded_part = connection.split("://")[1].split("#")[0]
                padding = len(encoded_part) % 4
                if padding:
                    encoded_part += "=" * (4 - padding)
                decoded_part = base64.b64decode(encoded_part).decode("utf-8")
                # Decoded format: method:password@server:port
                return decoded_part.split("@")[1].split(":")[0]

        # ssr (fully encoded)
        elif connection.startswith("ssr://"):
            encoded_part = connection.split("ssr://")[1]
            padding = len(encoded_part) % 4
            if padding:
                encoded_part += "=" * (4 - padding)
            decoded_part = base64.b64decode(encoded_part).decode("utf-8")
            # Decoded format: server:port:protocol:method:obfs:password/?<params>
            return decoded_part.split(":")[0]

        # hysteria, socks, http (server:port or user@server:port)
        elif connection.startswith(("hysteria://", "socks://", "http://")):
            address_part = connection.split("://")[1]
            if "@" in address_part:
                address_part = address_part.split("@")[1]
            return address_part.split(":")[0]

    except Exception:
        # Return None for any parsing error on any protocol
        return None
    return None
# ----------------------------------------------------------------------------------


def download_geoip_database():
    # (این تابع بدون تغییر باقی می‌ماند)
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
            if db_member is None: return False
            db_member.name = os.path.basename(db_member.name)
            tar.extract(db_member, path=".")
            os.rename(db_member.name, GEOIP_DB)
        os.remove("GeoLite2-City.tar.gz")
        print(f"✅ GeoIP database successfully updated to {GEOIP_DB}")
        return True
    except Exception as e:
        print(f"An error occurred during GeoIP download: {e}")
        return False

def resolve_to_ip(host):
    # (این تابع بدون تغییر باقی می‌ماند)
    try: return socket.gethostbyname(host)
    except socket.gaierror: return None

def get_country_code(ip, reader):
    # (این تابع بدون تغییر باقی می‌ماند)
    try: return reader.city(ip).country.iso_code
    except Exception: return None

def test_service_access(ip):
    # (این تابع بدون تغییر باقی می‌ماند)
    try:
        response = requests.head(TEST_URL, headers=HEADERS, timeout=5, allow_redirects=True)
        return response.status_code in (200, 301, 302)
    except requests.RequestException:
        return False

def main():
    # (تابع main با منطق کش و fallback بدون تغییر باقی می‌ماند)
    with open(LOG_FILE, "w") as f:
        f.write(f"Starting process at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

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
    
    if not os.path.exists(GEOIP_DB):
        print(f"❌ ERROR: GeoIP database '{GEOIP_DB}' is missing and download failed. Cannot continue.")
        return

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
