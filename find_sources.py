import requests
import os
import re
from urllib.parse import unquote
import time

# ====================================================================
# تنظیمات اسکریپت
# ====================================================================
SEARCH_PROTOCOLS = [
    'vmess', 'vless', 'ss', 'ssr', 'trojan', 'hysteria', 
    'hysteria2', 'tuic', 'brook', 'socks', 'wireguard'
]

EXISTING_SOURCES_FILE = "merge_configs.py"
OUTPUT_FILE = "discovered_sources.txt"
CRAWLED_URLS_STATE_FILE = "crawled_urls.txt"
GITHUB_TOKEN = os.getenv("GH_PAT")

# --- تنظیمات بهینه‌سازی ---
MAX_DEPTH = 10
REQUEST_TIMEOUT = 15
TOTAL_TIMEOUT_SECONDS = 5 * 60 * 60

# --- متغیرهای سراسری ---
START_TIME = time.time()
URL_REGEX = re.compile(r'https?://raw\.githubusercontent\.com/[^\s"\'`<>]+')
PROXY_PROTOCOL_REGEX = re.compile(r'^(vmess|vless|ss|ssr|trojan|hysteria|hysteria2|tuic|brook|socks|wireguard)://')

# ====================================================================

def clean_url(url):
    """URL را با حذف کاراکترهای اضافی بعد از .txt پاک‌سازی می‌کند."""
    try:
        txt_position = url.index('.txt')
        return url[:txt_position + 4]
    except ValueError:
        return url

def is_timeout():
    """چک می‌کند که آیا زمان کلی اسکریپت تمام شده است یا نه"""
    if time.time() - START_TIME > TOTAL_TIMEOUT_SECONDS:
        print("⏰ Global timeout reached. Finalizing the process...")
        return True
    return False

def load_state(file_path):
    """مجموعه‌ای از URLها را از یک فایل مشخص بارگذاری می‌کند"""
    urls = set()
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                urls.add(line.strip())
    return urls

def save_state(urls, file_path):
    """مجموعه‌ای از URLها را در یک فایل مشخص ذخیره می‌کند"""
    # تضمین می‌کند که فایل همیشه ساخته شود، حتی اگر خالی باشد
    with open(file_path, "w", encoding="utf-8") as f:
        if urls:
            for url in sorted(list(urls)):
                f.write(url + "\n")

def search_github(query, token):
    """در API گیت‌هاب برای پیدا کردن فایل‌های .txt جستجو می‌کند"""
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token: headers["Authorization"] = f"token {token}"
    params = {"q": f'"{query}" extension:txt', "per_page": 100}
    try:
        response = requests.get("https://api.github.com/search/code", headers=headers, params=params, timeout=20)
        response.raise_for_status()
        return response.json().get("items", [])
    except requests.RequestException: return []

def process_url_recursively(url, final_sources, visited_urls, depth):
    """یک URL را به صورت بازگشتی بررسی می‌کند"""
    if (depth > MAX_DEPTH or url in visited_urls or is_timeout() or
            not url.startswith("https://raw.githubusercontent.com/")):
        return

    indent = "  " * depth
    print(f"{indent}Processing (Depth {depth}): {url[:90]}...")
    visited_urls.add(url)

    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        content = response.text
    except requests.RequestException:
        return

    if any(line.strip().startswith(tuple(p + '://' for p in SEARCH_PROTOCOLS)) for line in content.splitlines()):
        print(f"{indent}  -> ✅ Found direct configs. Adding to final list.")
        final_sources.add(url)
        return

    nested_urls_raw = URL_REGEX.findall(content)
    if nested_urls_raw:
        cleaned_nested_urls = {clean_url(u) for u in nested_urls_raw}
        print(f"{indent}  -> 📄 Found {len(cleaned_nested_urls)} nested links to crawl.")
        for new_url in cleaned_nested_urls:
            process_url_recursively(new_url, final_sources, visited_urls, depth + 1)

def main():
    """تابع اصلی برای اجرای کل فرآیند"""
    if not GITHUB_TOKEN:
        print("❌ ERROR: GH_PAT environment variable is not set."); return

    final_sources = set()
    visited_urls = set()
    try:
        print("1. Loading previous state...")
        existing_urls_in_config = load_state(EXISTING_SOURCES_FILE)
        crawled_urls = load_state(CRAWLED_URLS_STATE_FILE)
        visited_urls = existing_urls_in_config.union(crawled_urls)
        print(f"Loaded {len(crawled_urls)} previously crawled URLs.")

        print("\n2. Searching GitHub for initial seed URLs...")
        initial_seed_urls = set()
        for protocol in SEARCH_PROTOCOLS:
            if is_timeout(): break
            print(f"   - Searching for files containing: '{protocol}'")
            for item in search_github(protocol, GITHUB_TOKEN):
                raw_url = item.get("html_url").replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
                cleaned_url = clean_url(unquote(raw_url))
                initial_seed_urls.add(cleaned_url)
        
        print(f"\n3. Starting deep crawl from {len(initial_seed_urls)} seed URLs...")
        for url in initial_seed_urls:
            if is_timeout(): break
            process_url_recursively(url, final_sources, visited_urls, depth=1)

    finally:
        print("\nSaving state before exiting...")
        save_state(visited_urls, CRAWLED_URLS_STATE_FILE)
        print(f"Saved {len(visited_urls)} total crawled URLs to '{CRAWLED_URLS_STATE_FILE}'.")

        new_final_sources = final_sources - existing_urls_in_config
        
        # تضمین می‌کند که فایل خروجی همیشه ساخته شود
        all_discovered = load_state(OUTPUT_FILE).union(new_final_sources)
        save_state(all_discovered, OUTPUT_FILE)
        
        if new_final_sources:
            print(f"\nDiscovered {len(new_final_sources)} new final source URLs in this run!")
            print(f"✅ Successfully updated '{OUTPUT_FILE}'.")
        else:
            print("\n✅ No new sources found in this run.")

if __name__ == "__main__":
    main()
