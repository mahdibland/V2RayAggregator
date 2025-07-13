import requests
import os
import re
import json

# ====================================================================
# تنظیمات اسکریپت
# ====================================================================
MERGE_CONFIG_PY_FILE = "merge_configs.py" # برای خواندن منابع اولیه
ACTIVE_SOURCES_FILE = "active_sources.json" # فایل خروجی جدید
DISCOVERED_SOURCES_FILE = "discovered_sources.txt"
DEAD_SOURCES_FILE = "dead_sources.txt"

VALID_PROTOCOLS = ('vmess://', 'vless://', 'ss://', 'ssr://', 'trojan://',
                   'hysteria://', 'hysteria2://', 'tuic://', 'brook://',
                   'socks://', 'wireguard://')

REQUEST_TIMEOUT = 10
# ====================================================================

def extract_urls_from_script(file_path):
    """URLها را از لیست urls در فایل پایتون استخراج می‌کند (فقط برای اجرای اولیه)"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        match = re.search(r'urls\s*=\s*\[(.*?)\]', content, re.DOTALL)
        if not match:
            return set()
        urls_str = match.group(1)
        urls = re.findall(r'https?://[^\s",]+', urls_str)
        return set(urls)
    except FileNotFoundError:
        return set()

def read_urls_from_txt(file_path):
    if not os.path.exists(file_path):
        return set()
    with open(file_path, 'r', encoding='utf-8') as f:
        return {line.strip() for line in f if line.strip()}

def is_source_valid(url):
    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        content = response.text
        return any(line.strip().startswith(VALID_PROTOCOLS) for line in content.splitlines())
    except requests.RequestException:
        return False

def main():
    print("Starting source management process...")

    # اگر فایل JSON وجود داشت از آن بخوان، اگر نه از فایل پایتون اولیه
    if os.path.exists(ACTIVE_SOURCES_FILE):
        with open(ACTIVE_SOURCES_FILE, 'r', encoding='utf-8') as f:
            current_urls = set(json.load(f))
    else:
         # این فقط برای اولین اجراست تا لیست اولیه را از کد قدیمی استخراج کند
        current_urls = extract_urls_from_script(MERGE_CONFIG_PY_FILE)

    discovered_urls = read_urls_from_txt(DISCOVERED_SOURCES_FILE)
    all_potential_urls = current_urls.union(discovered_urls)

    print(f"Found {len(current_urls)} existing sources and {len(discovered_urls)} new potential sources.")

    active_urls = set()
    dead_urls = set()

    print("\nValidating all potential sources...")
    for i, url in enumerate(all_potential_urls):
        print(f"  ({i+1}/{len(all_potential_urls)}) Checking: {url[:80]}...")
        if is_source_valid(url):
            active_urls.add(url)
            print("   -> ✅ Valid")
        else:
            dead_urls.add(url)
            print("   -> ❌ Invalid or dead")

    print(f"\nProcess finished. Found {len(active_urls)} active sources and {len(dead_urls)} dead sources.")

    print(f"Updating {ACTIVE_SOURCES_FILE}...")
    with open(ACTIVE_SOURCES_FILE, 'w', encoding='utf-8') as f:
        # ذخیره لیست فعال به صورت JSON
        json.dump(sorted(list(active_urls)), f, indent=4)

    previous_dead_urls = read_urls_from_txt(DEAD_SOURCES_FILE)
    all_dead_urls = dead_urls.union(previous_dead_urls)

    with open(DEAD_SOURCES_FILE, 'w', encoding='utf-8') as f:
        for url in sorted(list(all_dead_urls)):
            f.write(url + "\n")
    print(f"Updated {DEAD_SOURCES_FILE} with all dead links.")

    open(DISCOVERED_SOURCES_FILE, 'w').close()
    print(f"Cleared {DISCOVERED_SOURCES_FILE}.")

if __name__ == "__main__":
    main()
