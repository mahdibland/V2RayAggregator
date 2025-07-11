import requests
import os
import re
from urllib.parse import unquote

# ====================================================================
# تنظیمات اسکریپت
# ====================================================================

# کلیدواژه‌هایی که برای جستجو در گیت‌هاب استفاده می‌شوند
# می‌توانید این لیست را برای نتایج بهتر تغییر دهید
SEARCH_KEYWORDS = [
    "v2ray config", "vless sub", "vmess subscription", "ss sub", 
    "trojan subscription", "all_configs.txt", "sub_merge.txt"
]

# نام فایلی که لینک‌های اصلی شما در آن قرار دارد
EXISTING_SOURCES_FILE = "merge_configs.py"

# نام فایلی که لینک‌های جدید کشف شده در آن ذخیره می‌شوند
OUTPUT_FILE = "discovered_sources.txt"

# توکن دسترسی شخصی گیت‌هاب (برای جلوگیری از محدودیت API)
# این توکن را از طریق متغیر محیطی به اسکریپت بدهید
GITHUB_TOKEN = os.getenv("GITHUB_API_TOKEN")

# ====================================================================

def get_existing_urls(file_path):
    """لیست URLهای موجود را از فایل merge_configs.py استخراج می‌کند"""
    urls = set()
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            # پیدا کردن تمام URLها با استفاده از عبارت منظم
            found_urls = re.findall(r'https?://[^\s"]+', content)
            for url in found_urls:
                # حذف کاراکترهای اضافی مانند کاما یا پرانتز از انتهای URL
                urls.add(url.strip(',"\''))
    except FileNotFoundError:
        print(f"Warning: File {file_path} not found. Assuming no existing URLs.")
    return urls

def search_github(query, token):
    """یک کوئری را در API جستجوی کد گیت‌هاب اجرا می‌کند"""
    headers = {
        "Accept": "application/vnd.github.v3+json",
    }
    if token:
        headers["Authorization"] = f"token {token}"

    # جستجو برای فایل‌های .txt
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
        print("❌ ERROR: GITHUB_API_TOKEN environment variable is not set.")
        print("Please create a GitHub Personal Access Token and set it.")
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
            # استخراج لینک دانلود خام (raw)
            raw_url = item.get("html_url").replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
            # برخی URLها ممکن است انکود شده باشند
            raw_url = unquote(raw_url)
            discovered_urls.add(raw_url)

    print(f"\n3. Found a total of {len(discovered_urls)} unique potential URLs.")

    # فیلتر کردن URLهایی که از قبل وجود دارند
    new_urls = discovered_urls - existing_urls

    if not new_urls:
        print("\n✅ No new sources found. Your list is up to date!")
        return

    print(f"\n4. Discovered {len(new_urls)} new sources!")

    # ذخیره کردن لینک‌های جدید در فایل خروجی
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for url in sorted(list(new_urls)):
            f.write(url + "\n")

    print(f"\n✅ Successfully saved new sources to '{OUTPUT_FILE}'.")
    print("Please review this file and add the desired URLs to your merge_configs.py")

if __name__ == "__main__":
    main()
