import socket
import requests
import re
from urllib.parse import urlparse

# فرض می‌کنیم این بخش از کد اصلی است
def resolve_to_ip(host):
    try:
        # بررسی اینکه هاست معتبر است یا نه
        if not host or host.strip() == "" or host == ".":
            return None
        # حذف فاصله‌های اضافی و کاراکترهای نامعتبر
        host = host.strip().lower()
        # بررسی فرمت هاست با regex ساده
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return None
        ip = socket.gethostbyname(host)
        return ip
    except (socket.gaierror, UnicodeEncodeError) as e:
        print(f"Error resolving host {host}: {e}")
        return None

# فرض می‌کنیم تابع اصلی اسکریپت این‌گونه است
def main():
    # لینک‌های ورودی از درخواست قبلی
    urls = [
        "https://raw.githubusercontent.com/barry-far/V2ray-Config/refs/heads/main/All_Configs_Sub.txt",
        "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/all_configs.txt",
        "https://raw.githubusercontent.com/mahdibland/SSAggregator/master/sub/sub_merge.txt",
        "https://raw.githubusercontent.com/mrvcoder/V2rayCollector/refs/heads/main/mixed_iran.txt",
        "https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/v2ray/all_sub.txt"
    ]

    all_configs = set()
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            configs = response.text.splitlines()
            for config in configs:
                config = config.strip()
                if config:
                    all_configs.add(config)
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")

    # فرض می‌کنیم اینجا کانکشن‌ها فیلتر می‌شوند
    filtered_configs = []
    target_country = "IR"  # مثلاً ایران
    for config in all_configs:
        # استخراج هاست از کانکشن (بسته به فرمت، مثلاً vmess یا ss)
        host = extract_host(config)  # باید این تابع را تعریف کنید
        ip = resolve_to_ip(host)
        if ip and is_country(ip, target_country):  # فرض بر وجود تابع is_country
            filtered_configs.append(config)

    # ذخیره فایل نهایی
    with open("filtered_configs.txt", "w", encoding="utf-8") as f:
        for config in sorted(filtered_configs):
            f.write(config + "\n")

# فرض می‌کنیم این تابع هاست را از کانکشن استخراج می‌کند
def extract_host(config):
    try:
        # مثال ساده برای استخراج هاست از لینک‌های vmess یا ss
        if config.startswith("vmess://") or config.startswith("vless://") or config.startswith("ss://"):
            # دیکد کردن یا پارس لینک (بسته به فرمت)
            parsed = urlparse(config)
            return parsed.hostname if parsed.hostname else None
        return None
    except Exception as e:
        print(f"Error parsing config {config}: {e}")
        return None

# فرض می‌کنیم تابع is_country برای بررسی کشور IP وجود دارد
def is_country(ip, country_code):
    # اینجا باید API یا دیتابیسی برای بررسی کشور IP استفاده شود
    # برای مثال، می‌توان از GeoIP API استفاده کرد
    try:
        response = requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey=YOUR_API_KEY&ip={ip}")
        data = response.json()
        return data.get("country_code2") == country_code
    except Exception:
        return False

if __name__ == "__main__":
    main()
