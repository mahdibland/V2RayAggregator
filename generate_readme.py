import os
import glob
from datetime import datetime
import pytz
import jdatetime
from urllib.parse import quote

# ====================================================================
# تنظیمات اسکریپت
# ====================================================================
SUB_DIR = "subscription"
REPO_OWNER = "MEHR1DAD"
REPO_NAME = "V2RayAggregator"
ALL_CONFIGS_FILE = "merged_configs.txt"
TIMESTAMP_FILE = "last_update.txt" # نام فایل برای ذخیره زمان

# لینک دانلود از بخش Releases
ALL_CONFIGS_URL = f"https://github.com/{REPO_OWNER}/{REPO_NAME}/releases/latest/download/{ALL_CONFIGS_FILE}"

# نام کشور و پرچم
COUNTRY_NAMES = {
    "us": ("ایالات متحده", "🇺🇸"), "ae": ("امارات", "🇦🇪"), "ca": ("کانادا", "🇨🇦"),
    "de": ("آلمان", "🇩🇪"), "fr": ("فرانسه", "🇫🇷"), "gb": ("بریتانیا", "🇬🇧"),
    "ir": ("ایران", "🇮🇷"), "nl": ("هلند", "🇳🇱"), "se": ("سوئد", "🇸🇪"),
    "tr": ("ترکیه", "🇹🇷")
}

# ====================================================================

def count_connections(file_path):
    """تعداد کانکشن‌ها در یک فایل را می‌شمارد"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return sum(1 for line in f if line.strip())
    except FileNotFoundError:
        return 0
    return 0

def get_jalali_update_time():
    """زمان فعلی را به فرمت جلالی و خوانا برمی‌گرداند"""
    tehran_tz = pytz.timezone('Asia/Tehran')
    now_utc = datetime.utcnow().replace(tzinfo=pytz.utc)
    now_tehran = now_utc.astimezone(tehran_tz)
    jalali_date_obj = jdatetime.datetime.fromgregorian(datetime=now_tehran)
    
    day_name = jalali_date_obj.strftime("%A")
    day = jalali_date_obj.day
    month_name = jalali_date_obj.strftime('%B')
    year = jalali_date_obj.year
    time_str = now_tehran.strftime("%H:%M")
    
    # دو فرمت را برمی‌گرداند: یکی برای نمایش، یکی برای فایل
    full_display_str = f"{day_name} {day} {month_name} {year} - ساعت {time_str}"
    date_only_str = f"{day_name} {day} {month_name} {year}"
    return full_display_str, date_only_str

def generate_readme():
    """فایل README.md اصلی را تولید می‌کند"""
    country_data = []
    
    for file_path in glob.glob(os.path.join(SUB_DIR, "*_sub.txt")):
        file_name = os.path.basename(file_path)
        country_code = file_name.replace('_sub.txt', '').lower()
        
        if country_code in COUNTRY_NAMES:
            full_sub_count = count_connections(file_path)
            country_data.append({
                'code': country_code, 'name': COUNTRY_NAMES[country_code][0],
                'flag': COUNTRY_NAMES[country_code][1], 'full_count': full_sub_count,
                'full_link': f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/master/subscription/{file_name}",
                '100_link': f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/master/subscription/{file_name.replace('_sub.txt', '_sub_100.txt')}"
            })

    country_data.sort(key=lambda x: x['full_count'], reverse=True)
    all_connections_count = count_connections(ALL_CONFIGS_FILE)
    
    full_update_str, date_for_badge = get_jalali_update_time()
    
    # ذخیره کردن زمان کامل در فایل متنی
    with open(TIMESTAMP_FILE, "w", encoding="utf-8") as f:
        f.write(full_update_str)
    print(f"✅ Timestamp saved to {TIMESTAMP_FILE}")

    encoded_date = quote(date_for_badge)

    # --- شروع ساخت محتوای README ---
    readme_content = f"""
<div dir="rtl" align="center">

# تجمیع‌کننده کانفیگ‌های V2Ray
<p>این پروژه به صورت خودکار کانفیگ‌های فعال V2Ray را از منابع عمومی مختلف جمع‌آوری، تست و دسته‌بندی می‌کند.</p>
</div>

<div align="center">

[![Update-Status](https://img.shields.io/github/actions/workflow/status/{REPO_OWNER}/{REPO_NAME}/update_all_proxies.yml?style=for-the-badge&logo=githubactions&logoColor=white&label=Update%20Status)](https://github.com/{REPO_OWNER}/{REPO_NAME}/actions/workflows/update_all_proxies.yml)
[![Configs-Count](https://img.shields.io/badge/Configs-{all_connections_count:,}-blueviolet?style=for-the-badge&logo=server&logoColor=white)](https://github.com/{REPO_OWNER}/{REPO_NAME}/releases/latest/download/{ALL_CONFIGS_FILE})
[![Last-Update](https://img.shields.io/badge/Last%20Update-{encoded_date}-informational?style=for-the-badge&logo=clock&logoColor=white)](https://github.com/{REPO_OWNER}/{REPO_NAME}/commits/master)

</div>

<div dir="rtl">
# ... (بقیه محتوای README بدون تغییر باقی می‌ماند) ...
</div>
"""
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    print("✅ README.md generated successfully.")

if __name__ == "__main__":
    generate_readme()
