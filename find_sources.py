import requests
import os
import re
from urllib.parse import unquote

# ====================================================================
# تنظیمات اسکریپت
# ====================================================================
SEARCH_KEYWORDS = [
    "v2ray config", "vless sub", "vmess subscription", "ss sub", 
    "trojan subscription", "all_configs.txt", "sub_merge.txt"
]
EXISTING_SOURCES_FILE = "merge_configs.py"
OUTPUT_FILE = "discovered_sources.txt"

# نام متغیر محیطی به GH_PAT تغییر کرد
GITHUB_TOKEN = os.getenv("GH_PAT")

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
        print(f"Warning: File {file_path} not found. Assuming no existing URLs.")
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

def main():
    """تابع اصلی برای اجرای کل فرآیند"""
    if not GITHUB_TOKEN:
        print("❌ ERROR: GH_PAT environment variable is not set.")
        print("Please create a GitHub Secret named GH_PAT and set its value.")
        return

    print("1. Getting existing URLs from your configuration...")
    existing_urls = get_existing_urls(EXISTING_SOURCES_FILE)
    print(f"Found {len(existing_urls)} existing URLs.")

    discovered_urls = set()
    print("\n2. Searching GitHub for new sources...")
    for keyword in SEARCH_KEYWORDS:
        print(f"   - Searching for: '{keyword}'")
        results = search_github(keyword, GITHUB_TOKEN)
        for item in results:
            raw_url = item.get("html_url").replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
            raw_url = unquote(raw_url)
            discovered_urls.add(raw_url)

    print(f"\n3. Found a total of {len(discovered_urls)} unique potential URLs.")
    new_urls = discovered_urls - existing_urls

    if not new_urls:
        print("\n✅ No new sources found. Your list is up to date!")
        return

    print(f"\n4. Discovered {len(new_urls)} new sources!")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for url in sorted(list(new_urls)):
            f.write(url + "\n")

    print(f"\n✅ Successfully saved new sources to '{OUTPUT_FILE}'.")

if __name__ == "__main__":
    main()
