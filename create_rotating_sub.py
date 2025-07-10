import os
import random

# --- تنظیمات ---
SOURCE_FILE = "subscription/US_sub.txt"
SHUFFLED_FILE = "subscription/US_sub_shuffled.txt"
INDEX_FILE = "subscription/US_sub_index.txt"
OUTPUT_FILE = "subscription/US_sub_100.txt"
CHUNK_SIZE = 100

def run():
    # ۱. خواندن کانفیگ‌های اصلی از فایل منبع
    try:
        with open(SOURCE_FILE, "r", encoding="utf-8") as f:
            all_configs = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"❌ Source file not found: {SOURCE_FILE}")
        return

    if not all_configs:
        print("❌ Source file is empty. Nothing to do.")
        return

    # ۲. خواندن لیست بُر خورده قبلی (در صورت وجود)
    shuffled_configs = []
    if os.path.exists(SHUFFLED_FILE):
        with open(SHUFFLED_FILE, "r", encoding="utf-8") as f:
            shuffled_configs = [line.strip() for line in f if line.strip()]

    # ۳. خواندن ایندکس فعلی
    current_index = 0
    if os.path.exists(INDEX_FILE):
        try:
            with open(INDEX_FILE, "r") as f:
                current_index = int(f.read().strip())
        except (ValueError, FileNotFoundError):
            current_index = 0
            
    # ۴. بررسی اینکه آیا باید لیست را دوباره بُر بزنیم
    # اگر ایندکس از تعداد کل کانفیگ‌ها بیشتر شده یا لیست بُرخورده وجود ندارد
    if current_index >= len(shuffled_configs) or not shuffled_configs:
        print("🌀 Reached end of the list or first run. Re-shuffling...")
        random.shuffle(all_configs)
        shuffled_configs = all_configs
        current_index = 0
        with open(SHUFFLED_FILE, "w", encoding="utf-8") as f:
            f.write("\n".join(shuffled_configs))
        print(f"✅ Saved {len(shuffled_configs)} shuffled configs to {SHUFFLED_FILE}")

    # ۵. جدا کردن ۱۰۰ کانفیگ بعدی
    start_index = current_index
    end_index = start_index + CHUNK_SIZE
    new_chunk = shuffled_configs[start_index:end_index]

    # ۶. ذخیره کردن ۱۰۰ کانفیگ جدید
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(new_chunk))
    print(f"✅ Saved {len(new_chunk)} configs to {OUTPUT_FILE}")

    # ۷. آپدیت کردن ایندکس برای اجرای بعدی
    next_index = end_index
    with open(INDEX_FILE, "w") as f:
        f.write(str(next_index))
    print(f"➡️ Next run will start from index: {next_index}")


if __name__ == "__main__":
    run()
