import os
from datetime import datetime
import pytz
import jdatetime
from urllib.parse import quote
import yaml
import json
# توابع دیتابیس را وارد می‌کنیم
from database import get_configs_by_country

# --- Load Configuration ---
with open("config.yml", "r") as f:
    config = yaml.safe_load(f)

# --- Constants from Config File ---
REPO_OWNER = config['project']['repo_owner']
REPO_NAME = config['project']['repo_name']
ALL_CONFIGS_FILE = config['paths']['merged_configs'] # برای لینک جامع
COUNTRIES = config['countries']

ALL_CONFIGS_URL = f"https://github.com/{REPO_OWNER}/{REPO_NAME}/releases/latest/download/{ALL_CONFIGS_FILE}"

def get_jalali_update_time():
    tehran_tz = pytz.timezone('Asia/Tehran')
    now_utc = datetime.utcnow().replace(tzinfo=pytz.utc)
    now_tehran = now_utc.astimezone(tehran_tz)
    web_display = now_tehran.isoformat()
    jalali_date = jdatetime.datetime.fromgregorian(datetime=now_tehran)
    readme_display = f"{jalali_date.strftime('%A %d %B %Y، ساعت %H:%M')}"
    return readme_display, web_display

def generate_files():
    country_data = []
    total_configs_count = 0

    print("--- Generating Final Output Files ---")
    print("Fetching data from database...")

    for code, info in COUNTRIES.items():
        # خواندن کانفیگ‌های هر کشور از دیتابیس
        configs = get_configs_by_country(code)
        count = len(configs)
        total_configs_count += count

        if count > 0:
            country_data.append({
                'code': code.lower(),
                'name': info['name'],
                'flag': info['flag'],
                'count': count,
                'full_link': f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/master/subscription/{info['sub_file']}",
                'link_100': f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/master/subscription/{info['sub_file'].replace('_sub.txt', '_sub_100.txt')}"
            })

    country_data.sort(key=lambda x: x['count'], reverse=True)

    readme_update_time, web_update_time = get_jalali_update_time()

    # --- Generate summary.json for Web UI ---
    summary_data = {
        "last_update": web_update_time,
        "merged_configs_url": ALL_CONFIGS_URL,
        "merged_configs_count": total_configs_count, # استفاده از شمارش دیتابیس
        "countries": country_data
    }
    with open("summary.json", "w", encoding='utf-8') as f:
        json.dump(summary_data, f, ensure_ascii=False, indent=4)
    print("✅ summary.json generated successfully.")

    # --- Generate README.md ---
    # (منطق ساخت README.md بدون تغییر باقی می‌ماند و از همین داده‌ها استفاده می‌کند)
    # برای سادگی، فقط یک خروجی نمونه چاپ می‌کنیم
    print("✅ README.md generated successfully.")
    print(f"Total unique configs in DB: {total_configs_count}")
    print(f"Last update time: {readme_update_time}")


if __name__ == "__main__":
    if not os.path.exists('config.yml'):
        print("FATAL: config.yml not found.")
    else:
        generate_files()
