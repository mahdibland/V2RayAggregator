import requests
import json
import base64
import os
import geoip2.database
from urllib.parse import urlparse

# URL of the subscription to filter
SUBSCRIPTION_URL = "https://github.com/MEHR1DAD/V2RayAggregator/raw/refs/heads/master/merged_configs.txt"

# Path to GeoIP database (update with your GeoIP database path)
GEOIP_DB_PATH = "GeoLite2-Country.mmdb"

def get_country(ip):
    """Get country of an IP address using geoip2.database"""
    try:
        reader = geoip2.database.Reader(GEOIP_DB_PATH)
        response = reader.country(ip)
        return response.country.iso_code or "UNKNOWN"
    except Exception as e:
        print(f"Error getting country for {ip}: {e}")
        return "UNKNOWN"
    finally:
        reader.close()

def decode_config(config):
    """Decode and extract hostname/IP from config"""
    try:
        # Handle different protocols
        if config.startswith(("vmess://", "vless://", "trojan://", "ss://", "ssr://", "hysteria2://", "hysteria://", "brook://", "tuic://", "socks://", "http://", "wireguard://")):
            if config.startswith("vmess://"):
                # Decode vmess config
                config_data = base64.b64decode(config[8:]).decode("utf-8")
                return json.loads(config_data).get("add", None)
            elif config.startswith(("vless://", "trojan://", "hysteria2://", "hysteria://", "tuic://")):
                # Extract hostname/IP from URI
                parsed = urlparse(config)
                return parsed.hostname
            elif config.startswith("ss://"):
                # Shadowsocks: decode base64 or extract hostname
                if "@" in config:
                    hostname = config.split("@")[1].split(":")[0]
                    return hostname
                else:
                    decoded = base64.b64decode(config[5:].split("#")[0]).decode("utf-8")
                    return decoded.split("@")[1].split(":")[0]
            elif config.startswith("ssr://"):
                # ShadowsocksR: decode base64
                decoded = base64.b64decode(config[6:].split("#")[0]).decode("utf-8")
                return decoded.split(":")[3]
            elif config.startswith(("brook://", "socks://", "http://", "wireguard://")):
                parsed = urlparse(config)
                return parsed.hostname
        return None
    except Exception as e:
        print(f"Error decoding config: {e}")
        return None

def main():
    # Create output directory
    if not os.path.exists("sub"):
        os.makedirs("sub")

    # Download subscription
    try:
        response = requests.get(SUBSCRIPTION_URL, timeout=10)
        response.raise_for_status()
        configs = response.text.strip().split("\n")
    except Exception as e:
        print(f"Error downloading subscription: {e}")
        return

    # Dictionary to store configs by country
    country_configs = {}

    for config in configs:
        hostname = decode_config(config)
        if hostname:
            country = get_country(hostname)
            if country not in country_configs:
                country_configs[country] = []
            country_configs[country].append(config)

    # Save configs to files by country
    for country, configs in country_configs.items():
        with open(f"sub/{country}.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(configs))
        print(f"Saved {len(configs)} configs for {country}")

if __name__ == "__main__":
    main()
