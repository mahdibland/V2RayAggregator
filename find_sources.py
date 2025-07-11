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
CRAWLED_URLS_STATE_FILE = "crawled_urls.txt"  # فایل جدید برای حفظ وضعیت
GITHUB_TOKEN = os.getenv("GH_PAT")

# --- تنظیمات بهینه‌سازی ---
MAX_DEPTH = 10  # عمق ۱۰ باقی می‌ماند
REQUEST_TIMEOUT = 15
TOTAL_TIMEOUT_SECONDS = 5 * 60 * 60  # تایم‌اوت کلی ۵ ساعت

# --- متغیرهای سراسری ---
START_TIME = time.time()
URL_REGEX = re.compile(r'https?://[^\s"\'`<>]+')
PROXY_PROTOCOL_REGEX = re.compile(r'^(vmess|vless|ss|ssr|trojan|hysteria|hysteria2|tuic|brook)://')

# ====================================================================

def is_timeout():
    if time.time() - START_TIME > TOTAL_TIMEOUT_SECONDS:
        print("⏰ Global timeout reached. Finalizing the process...")
        return True
    return False

def load_state(file_path):
    urls = set()
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                urls.add(line.strip())
    return urls

def save_state(urls, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        for url in sorted(list(urls)):
            f.write(url + "\n")

def search_github(query, token):
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token: headers["Authorization"] = f"token {token}"
    params = {"q": f'{query} extension:txt', "per_page": 100}
    try:
        response = requests.get("https://api.github.com/search/code", headers=headers, params=params, timeout=20)
        response.raise_for_status()
        return response.json().get("items", [])
    except requests.RequestException: return []

def process_url_recursively(url, final_sources, visited_urls, depth):
    if depth > MAX_DEPTH or url in visited_urls or is_timeout():
        return

    indent = "  " * depth
    print(f"{indent}Processing (Depth {depth}): {url[:80]}...")
    visited_urls.add(url)

    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        content = response.text
    except requests.RequestException: return

    lines, is_direct_config, potential_urls = content.splitlines(), False, []
    for line in lines:
        if PROXY_PROTOCOL_REGEX.match(line.strip()):
            is_direct_config = True
            break
        for found_url in URL_REGEX.findall(line):
            path = os.path.basename(unquote(found_url.split('?')[0]))
            if path.endswith('.txt') or '.' not in path:
                potential_urls.append(found_url)

    if is_direct_config:
        final_sources.add(url)
    else:
        for new_url in set(potential_urls):
            process_url_recursively(new_url, final_sources, visited_urls, depth + 1)

def main():
    if not GITHUB_TOKEN:
        print("❌ ERROR: GH_PAT environment variable is not set."); return

    final_sources = set()
    try:
        print("1. Loading previous state...")
        existing_urls = load_state(EXISTING_SOURCES_FILE)
        crawled_urls = load_state(CRAWLED_URLS_STATE_FILE)
        visited_urls = existing_urls.union(crawled_urls)
        print(f"Loaded {len(crawled_urls)} previously crawled URLs.")

        print("\n2. Searching GitHub for initial seed URLs...")
        initial_seed_urls = set()
        for keyword in SEARCH_KEYWORDS:
            if is_timeout(): break
            print(f"   - Searching for: '{keyword}'")
            for item in search_github(keyword, GITHUB_TOKEN):
                raw_url = item.get("html_url").replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
                initial_seed_urls.add(unquote(raw_url))
        
        print(f"\n3. Starting deep crawl from {len(initial_seed_urls)} new seed URLs...")
        for url in initial_seed_urls:
            if is_timeout(): break
            process_url_recursively(url, final_sources, visited_urls, depth=1)

    finally:
        print("\nSaving state before exiting...")
        save_state(visited_urls, CRAWLED_URLS_STATE_FILE)
        print(f"Saved {len(visited_urls)} total crawled URLs to '{CRAWLED_URLS_STATE_FILE}'.")

        new_final_sources = final_sources - existing_urls
        if new_final_sources:
            print(f"\nDiscovered {len(new_final_sources)} new final source URLs in this run!")
            # فایل خروجی را با تمام یافته‌های جدید آپدیت می‌کند (نه فقط یافته‌های این اجرا)
            all_discovered = load_state(OUTPUT_FILE).union(new_final_sources)
            save_state(all_discovered, OUTPUT_FILE)
            print(f"✅ Successfully updated '{OUTPUT_FILE}'.")
        else:
            print("\n✅ No new sources found in this run.")

if __name__ == "__main__":
    main()
```

---
### ۲. کد اصلاح شده `find_new_sources.yml`
این ورک‌فلو اکنون فایل وضعیت `crawled_urls.txt` را هم همراه با نتایج، `commit` و `push` می‌کند.


```yaml
name: Find New Proxy Sources Daily

on:
  schedule:
    # هر روز در ساعت 00:00 UTC اجرا می‌شود
    - cron: '0 0 * * *'
  workflow_dispatch:

concurrency:
  group: ${{ github.workflow }}
  cancel-in-progress: true

jobs:
  find-sources:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install requests

      - name: Run script to find new sources
        run: python find_sources.py
        env:
          GH_PAT: ${{ secrets.GH_PAT }}

      - name: Commit and push discovered sources
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          
          # اضافه کردن فایل خروجی و فایل وضعیت
          git add discovered_sources.txt crawled_urls.txt
          
          if git diff --staged --quiet; then
            echo "✅ No new sources or state changes. Skipping commit."
          else
            git commit -m "Update discovered sources and crawl state"
            git push
          fi
