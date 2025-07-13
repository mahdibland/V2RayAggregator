import requests
import json
import os

# نام فایل منبع که لیست URL ها را در خود دارد
SOURCES_FILE = "active_sources.json"

# List of allowed protocols
ALLOWED_PROTOCOLS = {
    "vmess://", "vless://", "ss://", "ssr://", "trojan://",
    "hysteria://", "hysteria2://", "brook://", "tuic://",
    "socks://", "wireguard://"
}

def load_urls():
    """Loads subscription URLs from the json file."""
    if not os.path.exists(SOURCES_FILE):
        print(f"Error: Source file '{SOURCES_FILE}' not found.")
        return []
    try:
        with open(SOURCES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, TypeError):
        print(f"Error: Could not decode JSON from '{SOURCES_FILE}'.")
        return []

def fetch_configs(urls):
    all_configs = set()
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            configs = response.text.splitlines()
            for config in configs:
                config = config.strip()
                if config and any(config.startswith(protocol) for protocol in ALLOWED_PROTOCOLS):
                    all_configs.add(config)
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
    return all_configs

def save_configs(configs):
    with open("merged_configs.txt", "w", encoding="utf-8") as f:
        for config in sorted(configs):
            f.write(config + "\n")

if __name__ == "__main__":
    urls = load_urls()
    if urls:
        print(f"Loaded {len(urls)} sources from '{SOURCES_FILE}'")
        configs = fetch_configs(urls)
        print(f"Fetched {len(configs)} unique configurations.")
        save_configs(configs)
        print(f"Merged configurations into merged_configs.txt")
    else:
        print("No sources to process. Exiting.")
