import os
import glob
from datetime import datetime
import pytz
import jdatetime
from urllib.parse import quote
import yaml
import json

# --- Load Configuration ---
with open("config.yml", "r") as f:
    config = yaml.safe_load(f)

# --- Constants from Config File ---
SUB_DIR = config['paths']['output_dir']
REPO_OWNER = config['project']['repo_owner']
REPO_NAME = config['project']['repo_name']
ALL_CONFIGS_FILE = config['paths']['merged_configs']
COUNTRIES = config['countries']

ALL_CONFIGS_URL = f"https://github.com/{REPO_OWNER}/{REPO_NAME}/releases/latest/download/{ALL_CONFIGS_FILE}"

def count_connections(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return sum(1 for line in f if line.strip())
    except FileNotFoundError:
        return 0

def get_jalali_update_time():
    tehran_tz = pytz.timezone('Asia/Tehran')
    now_utc = datetime.utcnow().replace(tzinfo=pytz.utc)
    now_tehran = now_utc.astimezone(tehran_tz)
    # برای نمایش در وب
    web_display = now_tehran.strftime("%Y-%m-%dT%H:%M:%S%z")
    # برای نمایش در README
    jalali_date = jdatetime.datetime.fromgregorian(datetime=now_tehran)
    readme_display = f"{jalali_date.strftime('%A %d %B %Y، ساعت %H:%M')}"
    return readme_display, web_display

def generate_files():
    country_data = []
    for code, info in COUNTRIES.items():
        file_path = os.path.join(SUB_DIR, info['sub_file'])
        count = count_connections(file_path)
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

    all_connections_count = count_connections(ALL_CONFIGS_FILE)
    readme_update_time, web_update_time = get_jalali_update_time()

    # --- Generate summary.json for Web UI ---
    summary_data = {
        "last_update": web_update_time,
        "merged_configs_url": ALL_CONFIGS_URL,
        "merged_configs_count": all_connections_count,
        "countries": country_data
    }
    with open("summary.json", "w", encoding='utf-8') as f:
        json.dump(summary_data, f, ensure_ascii=False, indent=4)
    print("✅ summary.json generated successfully.")

    # --- Generate README.md ---
    encoded_date = quote(readme_update_time)
    readme_content = f"""
