import requests
import os
import re
from urllib.parse import unquote
import time

# ====================================================================
# تنظیمات اسکریپت
# ====================================================================
# بازگشت به لیست کلیدواژه‌های گسترده‌تر برای نتایج بهتر
SEARCH_KEYWORDS = [
    "vless subscription", "vmess subscription", "trojan subscription",
    "ss subscription", "ssr subscription", "hysteria subscription",
    "sub_merge.txt", "all_configs.txt", "v2ray-configs", "proxies.txt",
    "sub.txt", "*.txt", "subscription.txt", "conection.txt",
    "connection.txt"
]

EXISTING_SOURCES_FILE = "merge_configs.py"
OUTPUT_FILE = "discovered_sources.txt"
CRAWLED_URLS_STATE_FILE = "crawled_urls.txt"
GITHUB_TOKEN = os.getenv("GH_PAT")

# --- تنظیمات بهینه‌سازی ---
MAX_DEPTH = 10
REQUEST_TIMEOUT = 15
TOTAL_TIMEOUT_SECONDS = 5 * 60 * 60  # تایم‌اوت کلی ۵ ساعت

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

def extract_urls_from_script(file_path):
    """URLها را فقط از داخل لیست urls در فایل پایتون استخراج می‌کند."""
    urls = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        match = re.search(r'urls\s*=\s*\[(.*?)\]', content, re.DOTALL)
        if match:
            urls_str = match.group(1)
            found_urls = re.findall(r'https?://[^\s",]+', urls_str)
            urls.update(found_urls)
    except FileNotFoundError:
        print(f"Warning: {file_path} not found.")
    return urls

def is_timeout():
    """چک می‌کند که آیا زمان کلی اسکریپت تمام شده است یا نه"""
    if time.time() - START_TIME > TOTAL_TIMEOUT_SECONDS:
        print("⏰ Global timeout reached. Finalizing the process...")
        return True
    return False

def load_state(file_path):
    """مجموعه‌ای از URLها را از یک فایل متنی ساده بارگذاری می‌کند"""
    urls = set()
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                urls.add(line.strip())
    return urls

def save_state(urls, file_path):
    """مجموعه‌ای از URLها را در یک فایل مشخص ذخیره می‌کند"""
    with open(file_path, "w", encoding="utf-8") as f:
        if urls:
            for url in sorted(list(urls)):
                f.write(url + "\n")

def search_github_paginated(query, token):
    """
    در API گیت‌هاب جستجو کرده و با استفاده از صفحه‌بندی، تمام نتایج ممکن را برمی‌گرداند.
    """
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token: headers["Authorization"] = f"token {token}"
    
    all_items = []
    for page in range(1, 11): # حداکثر ۱۰ صفحه (۱۰۰۰ نتیجه) برای هر کوئری
        if is_timeout(): break
        
        params = {"q": f'"{query}" extension:txt', "per_page": 100, "page": page}
        
        try:
            response = requests.get("https://api.github.com/search/code", headers=headers, params=params, timeout=30)
            response.raise_for_status()
            items = response.json().get("items", [])
            
            if not items: break
            
            all_items.extend(items)
            time.sleep(1) # وقفه کوتاه بین هر صفحه

        except requests.RequestException as e:
            print(f"   -> Error during GitHub API request: {e}")
            break
            
    return all_items

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

    if any(line.strip().startswith(tuple(p + '://' for p in PROXY_PROTOCOL_REGEX.pattern.strip('^()$').split('|'))) for line in content.splitlines()):
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
        existing_urls_in_config = extract_urls_from_script(EXISTING_SOURCES_FILE)
        crawled_urls = load_state(CRAWLED_URLS_STATE_FILE)
        visited_urls = existing_urls_in_config.union(crawled_urls)
        print(f"Loaded {len(crawled_urls)} previously crawled URLs.")

        print("\n2. Searching GitHub for initial seed URLs using multiple keywords...")
        initial_seed_urls = set()
        for keyword in SEARCH_KEYWORDS:
            if is_timeout(): break
            print(f"\n--- Searching for keyword: '{keyword}' ---")
            
            search_results = search_github_paginated(keyword, GITHUB_TOKEN)
            
            for item in search_results:
                raw_url = item.get("html_url").replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
                cleaned_url = clean_url(unquote(raw_url))
                initial_seed_urls.add(cleaned_url)
            
            print(f"Found {len(search_results)} items for this keyword.")
            # وقفه ۲ ثانیه‌ای بین هر کلیدواژه برای جلوگیری از محدودیت نرخ
            time.sleep(2)
        
        print(f"\n3. Starting deep crawl from a total of {len(initial_seed_urls)} unique seed URLs...")
        for url in list(initial_seed_urls): # تبدیل به لیست برای جلوگیری از تغییر در حین پیمایش
            if is_timeout(): break
            process_url_recursively(url, final_sources, visited_urls, depth=1)

    finally:
        print("\nSaving state before exiting...")
        save_state(visited_urls, CRAWLED_URLS_STATE_FILE)
        print(f"Saved {len(visited_urls)} total crawled URLs to '{CRAWLED_URLS_STATE_FILE}'.")

        new_final_sources = final_sources - existing_urls_in_config
        
        all_discovered = load_state(OUTPUT_FILE).union(new_final_sources)
        save_state(all_discovered, OUTPUT_FILE)
        
        if new_final_sources:
            print(f"\nDiscovered {len(new_final_sources)} new final source URLs in this run!")
            print(f"✅ Successfully updated '{OUTPUT_FILE}'.")
        else:
            print("\n✅ No new sources found in this run.")

if __name__ == "__main__":
    main()
