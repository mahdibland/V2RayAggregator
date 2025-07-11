import requests
import os
import re
from urllib.parse import unquote
import time

# ====================================================================
# تنظیمات اسکریپت
# ====================================================================
SEARCH_KEYWORDS = [
    "v2ray config", "vless sub", "vmess subscription", "ss sub",
    "trojan subscription", "all_configs.txt", "sub_merge.txt"
]
EXISTING_SOURCES_FILE = "merge_configs.py"
OUTPUT_FILE = "discovered_sources.txt"
GITHUB_TOKEN = os.getenv("GH_PAT")

# --- تنظیمات جدید ---
MAX_DEPTH = 10  # حداکثر عمق برای دنبال کردن لینک‌های تودرتو
REQUEST_TIMEOUT = 10  # زمان انتظار برای هر درخواست (به ثانیه)

# عبارت منظم برای پیدا کردن URLهای http/https
URL_REGEX = re.compile(r'https?://[^\s"\'`<>]+')

# عبارت منظم برای تشخیص پروتکل‌های پروکسی
PROXY_PROTOCOL_REGEX = re.compile(r'^(vmess|vless|ss|ssr|trojan|hysteria|hysteria2|tuic|brook)://')

# ====================================================================

def get_existing_urls(file_path):
    """لیست URLهای موجود را از فایل merge_configs.py استخراج می‌کند"""
    urls = set()
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            found_urls = re.findall(r'https?://[^\s"]+', content)
            for url in found_urls:
                urls.add(url.strip(',"\''))
    except FileNotFoundError:
        print(f"Warning: File {file_path} not found.")
    return urls

def search_github(query, token):
    """یک کوئری را در API جستجوی کد گیت‌هاب اجرا می‌کند"""
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"token {token}"
    search_query = f'{query} extension:txt'
    params = {"q": search_query, "per_page": 100}
    try:
        response = requests.get("https://api.github.com/search/code", headers=headers, params=params, timeout=20)
        response.raise_for_status()
        return response.json().get("items", [])
    except requests.RequestException as e:
        print(f"Error during GitHub API request: {e}")
        return []

def process_url_recursively(url, final_sources, visited_urls, depth):
    """یک URL را به صورت بازگشتی بررسی کرده و منابع نهایی را پیدا می‌کند"""
    if depth > MAX_DEPTH or url in visited_urls:
        return

    # نمایش وضعیت پردازش
    indent = "  " * depth
    print(f"{indent}Processing URL (Depth {depth}): {url}")
    visited_urls.add(url)

    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        content = response.text
    except requests.RequestException:
        return

    lines = content.splitlines()
    is_direct_config_source = False
    potential_new_urls = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # اگر خط یک کانفیگ مستقیم بود، این URL یک منبع نهایی است
        if PROXY_PROTOCOL_REGEX.match(line):
            is_direct_config_source = True
            break
        
        # در غیر این صورت، به دنبال لینک‌های دیگر در این خط بگرد
        found_urls_in_line = URL_REGEX.findall(line)
        for found_url in found_urls_in_line:
            # فقط لینک‌هایی را در نظر بگیر که به نظر لینک اشتراک هستند
            # (مثلاً به .txt ختم می‌شوند یا پسوند خاصی ندارند)
            path = os.path.basename(unquote(found_url.split('?')[0]))
            if path.endswith('.txt') or '.' not in path:
                 potential_new_urls.append(found_url)

    if is_direct_config_source:
        print(f"{indent}  -> ✅ Found direct configs. Adding parent URL to final sources.")
        final_sources.add(url)
    else:
        # اگر کانفیگ مستقیمی پیدا نشد، لینک‌های جدید را دنبال کن
        print(f"{indent}  -> 📄 Not a direct config source. Found {len(potential_new_urls)} potential new URLs to crawl.")
        for new_url in set(potential_new_urls): # set() for uniqueness in this level
            time.sleep(0.1)  # فاصله کوتاه برای جلوگیری از فشار به سرور
            process_url_recursively(new_url, final_sources, visited_urls, depth + 1)

def main():
    if not GITHUB_TOKEN:
        print("❌ ERROR: GH_PAT environment variable is not set.")
        return

    print("1. Getting existing URLs...")
    existing_urls = get_existing_urls(EXISTING_SOURCES_FILE)
    
    final_sources = set()
    visited_urls = set(existing_urls) # لینک‌های موجود را از ابتدا به لیست دیده‌شده اضافه کن

    print("\n2. Searching GitHub for initial seed URLs...")
    initial_seed_urls = set()
    for keyword in SEARCH_KEYWORDS:
        print(f"   - Searching for: '{keyword}'")
        results = search_github(keyword, GITHUB_TOKEN)
        for item in results:
            raw_url = item.get("html_url").replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
            initial_seed_urls.add(unquote(raw_url))
    
    print(f"\n3. Starting deep crawl from {len(initial_seed_urls)} seed URLs...")
    for url in initial_seed_urls:
        process_url_recursively(url, final_sources, visited_urls, depth=1)

    # فیلتر کردن لینک‌هایی که از قبل داشتید
    new_final_sources = final_sources - existing_urls

    if not new_final_sources:
        print("\n✅ No new sources found after deep crawl.")
        return

    print(f"\n4. Discovered {len(new_final_sources)} new final source URLs!")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for url in sorted(list(new_final_sources)):
            f.write(url + "\n")

    print(f"\n✅ Successfully saved new sources to '{OUTPUT_FILE}'.")

if __name__ == "__main__":
    main()
