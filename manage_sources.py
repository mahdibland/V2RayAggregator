import requests
import os
import re

# ====================================================================
# تنظیمات اسکریپت
# ====================================================================
MERGE_CONFIG_FILE = "merge_configs.py"
DISCOVERED_SOURCES_FILE = "discovered_sources.txt"
DEAD_SOURCES_FILE = "dead_sources.txt"

# پروتکل‌های معتبر برای اعتبارسنجی یک منبع
VALID_PROTOCOLS = ('vmess://', 'vless://', 'ss://', 'ssr://', 'trojan://', 
                   'hysteria://', 'hysteria2://', 'tuic://', 'brook://', 
                   'socks://', 'wireguard://')

REQUEST_TIMEOUT = 10

# ====================================================================

def extract_urls_from_script(file_path):
    """URLها را از لیست urls در فایل پایتون استخراج می‌کند"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # پیدا کردن بلاک لیست urls با استفاده از عبارت منظم
        match = re.search(r'urls\s*=\s*\[(.*?)\]', content, re.DOTALL)
        if not match:
            return set()
        
        # استخراج تمام URLها از بلاک پیدا شده
        urls_str = match.group(1)
        urls = re.findall(r'https?://[^\s",]+', urls_str)
        return set(urls)
    except FileNotFoundError:
        print(f"Warning: {file_path} not found. Returning empty set.")
        return set()

def read_urls_from_txt(file_path):
    """URLها را از یک فایل متنی ساده می‌خواند"""
    if not os.path.exists(file_path):
        return set()
    with open(file_path, 'r', encoding='utf-8') as f:
        return {line.strip() for line in f if line.strip()}

def is_source_valid(url):
    """چک می‌کند که آیا یک URL حاوی حداقل یک کانفیگ معتبر است یا نه"""
    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        content = response.text
        # اگر حتی یک خط با یکی از پروتکل‌های معتبر شروع شود، منبع معتبر است
        return any(line.strip().startswith(VALID_PROTOCOLS) for line in content.splitlines())
    except requests.RequestException:
        return False

def update_script_file(file_path, active_urls):
    """فایل merge_configs.py را با لیست URLهای جدید بازنویسی می‌کند"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # ساختن رشته جدید برای لیست URLها
    # هر URL در یک خط جدید با تورفتگی و کاما قرار می‌گیرد
    new_urls_str = "[\n"
    for url in sorted(list(active_urls)):
        new_urls_str += f'    "{url}",\n'
    new_urls_str += "]"

    # جایگزین کردن بلاک urls قدیمی با بلاک جدید
    new_content = re.sub(r'urls\s*=\s*\[.*?\]', f'urls = {new_urls_str}', content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    print("Starting source management process...")

    # ۱. خواندن تمام URLهای موجود و جدید
    current_urls = extract_urls_from_script(MERGE_CONFIG_FILE)
    discovered_urls = read_urls_from_txt(DISCOVERED_SOURCES_FILE)
    all_potential_urls = current_urls.union(discovered_urls)

    print(f"Found {len(current_urls)} existing sources and {len(discovered_urls)} new potential sources.")

    active_urls = set()
    dead_urls = set()

    # ۲. اعتبارسنجی تمام URLها
    print("\nValidating all potential sources...")
    for i, url in enumerate(all_potential_urls):
        print(f"  ({i+1}/{len(all_potential_urls)}) Checking: {url[:80]}...")
        if is_source_valid(url):
            active_urls.add(url)
            print("    -> ✅ Valid")
        else:
            dead_urls.add(url)
            print("    -> ❌ Invalid or dead")

    # ۳. ذخیره کردن نتایج
    print(f"\nProcess finished. Found {len(active_urls)} active sources and {len(dead_urls)} dead sources.")
    
    print(f"Updating {MERGE_CONFIG_FILE}...")
    update_script_file(MERGE_CONFIG_FILE, active_urls)
    
    # اضافه کردن لینک‌های مرده جدید به فایل قبلی (در صورت وجود)
    previous_dead_urls = read_urls_from_txt(DEAD_SOURCES_FILE)
    all_dead_urls = dead_urls.union(previous_dead_urls)
    
    with open(DEAD_SOURCES_FILE, 'w', encoding='utf-8') as f:
        for url in sorted(list(all_dead_urls)):
            f.write(url + "\n")
    print(f"Updated {DEAD_SOURCES_FILE} with all dead links.")

    # خالی کردن فایل منابع کشف شده چون همگی پردازش شدند
    open(DISCOVERED_SOURCES_FILE, 'w').close()
    print(f"Cleared {DISCOVERED_SOURCES_FILE}.")


if __name__ == "__main__":
    main()
