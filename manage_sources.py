import requests
import os
import yaml
from database import initialize_db, get_all_sources_to_check, update_source_status

# --- Load Configuration ---
with open("config.yml", "r") as f:
    config = yaml.safe_load(f)

# --- Constants from Config File ---
DISCOVERED_SOURCES_FILE = config['paths']['discovered_sources']
REQUEST_TIMEOUT = config['settings']['request_timeout']
VALID_PROTOCOLS = ('vmess://', 'vless://', 'ss://', 'ssr://', 'trojan://',
                   'hysteria://', 'hysteria2://', 'tuic://', 'brook://',
                   'socks://', 'wireguard://')
# --- End of Constants ---

def read_urls_from_txt(file_path):
    """Reads newly discovered URLs from a text file."""
    if not os.path.exists(file_path):
        return set()
    with open(file_path, 'r', encoding='utf-8') as f:
        return {line.strip() for line in f if line.strip()}

def is_source_valid(url):
    """Checks if a URL contains at least one valid proxy config."""
    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        content = response.text
        return any(line.strip().startswith(VALID_PROTOCOLS) for line in content.splitlines())
    except requests.RequestException:
        return False

def main():
    """
    Main function to validate sources and update their status in the database.
    """
    print("--- Source Management Process Started ---")

    # 1. اطمینان از وجود دیتابیس و جداول
    initialize_db()

    # 2. خواندن تمام منابع از دیتابیس و فایل منابع جدید
    sources_from_db = set(get_all_sources_to_check())
    discovered_urls = read_urls_from_txt(DISCOVERED_SOURCES_FILE)
    all_potential_urls = sources_from_db.union(discovered_urls)

    if not all_potential_urls:
        print("No sources found to check. Exiting.")
        return

    print(f"Checking a total of {len(all_potential_urls)} potential sources...")

    # 3. اعتبارسنجی تمام URLها و آپدیت وضعیت در دیتابیس
    active_count = 0
    dead_count = 0
    for i, url in enumerate(all_potential_urls):
        print(f"  ({i+1}/{len(all_potential_urls)}) Checking: {url[:80]}...")
        if is_source_valid(url):
            update_source_status(url, 'active')
            active_count += 1
            print("   -> ✅ Valid, status set to 'active'")
        else:
            update_source_status(url, 'dead')
            dead_count += 1
            print("   -> ❌ Invalid, status set to 'dead'")

    # 4. پاک کردن فایل منابع کشف شده
    if os.path.exists(DISCOVERED_SOURCES_FILE):
        open(DISCOVERED_SOURCES_FILE, 'w').close()
        print(f"\nCleared '{DISCOVERED_SOURCES_FILE}'.")

    print(f"\nProcess finished. Active sources: {active_count}, Dead sources: {dead_count}")
    print("--- Source Management Process Finished ---")


if __name__ == "__main__":
    if not os.path.exists('config.yml'):
        print("FATAL: config.yml not found. Please create it first.")
    else:
        main()
