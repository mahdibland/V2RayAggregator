import os
import random

# --- لیست کشورها ---
# این لیست باید با لیست فایل exp_country.py شما هماهنگ باشد
COUNTRIES = {
    "US": "US_sub.txt", "NL": "NL_sub.txt", "DE": "DE_sub.txt",
    "GB": "GB_sub.txt", "FR": "FR_sub.txt", "CA": "CA_sub.txt",
    "TR": "TR_sub.txt", "AE": "AE_sub.txt", "SE": "SE_sub.txt",
    "IR": "IR_sub.txt"
}

CHUNK_SIZE = 100

def process_country(country_code: str):
    """این تابع عملیات را برای یک کشور مشخص انجام می‌دهد"""
    print(f"\n--- Processing country: {country_code} ---")
    
    # تعریف نام فایل‌ها به صورت داینامیک برای هر کشور
    source_file = f"subscription/{country_code}_sub.txt"
    shuffled_file = f"subscription/{country_code}_sub_shuffled.txt"
    index_file = f"subscription/{country_code}_sub_index.txt"
    output_file = f"subscription/{country_code}_sub_100.txt"

    # ۱. خواندن کانفیگ‌های اصلی
    try:
        with open(source_file, "r", encoding="utf-8") as f:
            all_configs = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"🟡 Source file for {country_code} not found, skipping.")
        return

    if not all_configs:
        print(f"🟡 Source file for {country_code} is empty, skipping.")
        return

    # ۲. خواندن لیست بُر خورده قبلی
    shuffled_configs = []
    if os.path.exists(shuffled_file):
        with open(shuffled_file, "r", encoding="utf-8") as f:
            shuffled_configs = [line.strip() for line in f if line.strip()]

    # ۳. خواندن ایندکس
    current_index = 0
    if os.path.exists(index_file):
        try:
            with open(index_file, "r") as f:
                current_index = int(f.read().strip())
        except (ValueError, FileNotFoundError):
            current_index = 0
            
    # ۴. بررسی برای بُر زدن مجدد
    if current_index >= len(shuffled_configs) or not shuffled_configs:
        print(f"🌀 Re-shuffling configs for {country_code}...")
        random.shuffle(all_configs)
        shuffled_configs = all_configs
        current_index = 0
        with open(shuffled_file, "w", encoding="utf-8") as f:
            f.write("\n".join(shuffled_configs))

    # ۵. جدا کردن ۱۰۰ کانفیگ بعدی
    start_index = current_index
    end_index = start_index + CHUNK_SIZE
    new_chunk = shuffled_configs[start_index:end_index]

    # ۶. ذخیره کردن خروجی
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(new_chunk))
    print(f"✅ Saved {len(new_chunk)} configs to {output_file}")

    # ۷. آپدیت کردن ایندکس
    next_index = end_index
    with open(index_file, "w") as f:
        f.write(str(next_index))
    print(f"➡️ Next run for {country_code} will start from index: {next_index}")


if __name__ == "__main__":
    # ایجاد پوشه subscription در صورت عدم وجود
    if not os.path.exists("subscription"):
        os.makedirs("subscription")
        
    # اجرای عملیات برای تمام کشورها در لیست
    for code in COUNTRIES.keys():
        process_country(code)
    
    print("\nAll countries processed successfully.")
