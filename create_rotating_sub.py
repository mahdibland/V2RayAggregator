import os
import random
import yaml
# تابع جدید برای خواندن کانفیگ‌ها از دیتابیس
from database import get_configs_by_country

# --- Load Configuration ---
with open("config.yml", "r") as f:
    config = yaml.safe_load(f)

# --- Constants from Config File ---
OUTPUT_DIR = config['paths']['output_dir']
COUNTRIES = config['countries']
CHUNK_SIZE = config['settings']['create_rotating_sub']['chunk_size'] # خواندن اندازه از کانفیگ
# --- End of Constants ---

def create_subscription_files():
    """
    Fetches configs from the database and creates final subscription files
    for both the full list and a rotating random chunk.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("--- Creating Final Subscription Files ---")

    for country_code, country_info in COUNTRIES.items():
        print(f"\nProcessing country: {country_code}")

        # ۱. خواندن تمام کانفیگ‌های سالم و مرتب‌شده بر اساس سرعت از دیتابیس
        # ما تعداد بیشتری از ۱۰۰ تا می‌خوانیم تا بتوانیم لیست چرخشی بسازیم
        all_configs = get_configs_by_country(country_code, limit=500)

        if not all_configs:
            print(f"🟡 No configs found in database for {country_code}. Skipping.")
            continue

        # ۲. ذخیره فایل اشتراک کامل (شامل تمام کانفیگ‌های سالم)
        full_sub_filename = country_info['sub_file']
        full_sub_path = os.path.join(OUTPUT_DIR, full_sub_filename)
        with open(full_sub_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(all_configs))
        print(f"✅ Saved {len(all_configs)} configs to {full_sub_filename}")

        # ۳. ساخت و ذخیره فایل چرخشی ۱۰۰تایی
        # از لیست کامل، به صورت رندوم ۱۰۰ تا انتخاب می‌کنیم
        if len(all_configs) > CHUNK_SIZE:
            rotating_chunk = random.sample(all_configs, CHUNK_SIZE)
        else:
            rotating_chunk = all_configs

        rotating_sub_filename = full_sub_filename.replace('_sub.txt', '_sub_100.txt')
        rotating_sub_path = os.path.join(OUTPUT_DIR, rotating_sub_filename)
        with open(rotating_sub_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(rotating_chunk))
        print(f"✅ Saved {len(rotating_chunk)} random configs to {rotating_sub_filename}")

if __name__ == "__main__":
    if not os.path.exists('config.yml'):
        print("FATAL: config.yml not found.")
    else:
        create_subscription_files()
        print("\nAll subscription files created successfully.")
