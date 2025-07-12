import os
import glob
from datetime import datetime
import pytz
import jdatetime

# ====================================================================
# تنظیمات اسکریپت
# ====================================================================
SUB_DIR = "subscription"
REPO_OWNER = "MEHR1DAD"
REPO_NAME = "V2RayAggregator"
ALL_CONFIGS_FILE = "merged_configs.txt"

# لینک دانلود جدید از بخش Releases
ALL_CONFIGS_URL = f"https://github.com/{REPO_OWNER}/{REPO_NAME}/releases/latest/download/{ALL_CONFIGS_FILE}"

# نام کشور و پرچم برای کدهای ISO 3166-1 alpha-2
COUNTRY_NAMES = {
    "us": ("ایالات متحده", "🇺🇸"), "ae": ("امارات", "🇦🇪"), "ca": ("کانادا", "🇨🇦"),
    "de": ("آلمان", "🇩🇪"), "fr": ("فرانسه", "🇫🇷"), "gb": ("بریتانIA", "🇬🇧"),
    "ir": ("ایران", "🇮🇷"), "nl": ("هلند", "🇳🇱"), "se": ("سوئد", "🇸🇪"),
    "tr": ("ترکیه", "🇹🇷")
}

# ====================================================================

def count_connections(file_path):
    """تعداد کانکشن‌ها (خطوط غیرخالی) در یک فایل را می‌شمارد"""
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
    jalali_date = jdatetime.datetime.fromgregorian(datetime=now_tehran)
    
    day_name = jalali_date.strftime("%A")
    day = jalali_date.day
    month_name = jalali_date.strftime('%B')
    year = jalali_date.year
    time_str = now_tehran.strftime("%H:%M")
    
    return f"{day_name} {day} {month_name} {year} - ساعت {time_str}"

def generate_readme():
    """فایل README.md اصلی را تولید می‌کند"""
    country_data = []
    
    # پیدا کردن تمام فایل‌های اصلی کشورها
    for file_path in glob.glob(os.path.join(SUB_DIR, "*_sub.txt")):
        file_name = os.path.basename(file_path)
        country_code = file_name.replace('_sub.txt', '').lower()
        
        if country_code in COUNTRY_NAMES:
            full_sub_count = count_connections(file_path)
            sub_100_path = file_path.replace('_sub.txt', '_sub_100.txt')
            
            country_data.append({
                'code': country_code,
                'name': COUNTRY_NAMES[country_code][0],
                'flag': COUNTRY_NAMES[country_code][1],
                'full_count': full_sub_count,
                'full_link': f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/master/subscription/{file_name}",
                '100_link': f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/master/subscription/{os.path.basename(sub_100_path)}"
            })

    # مرتب‌سازی کشورها بر اساس نام فارسی
    country_data.sort(key=lambda x: x['name'])

    # شمارش تعداد کل کانکشن‌ها
    all_connections_count = count_connections(ALL_CONFIGS_FILE)
    update_time_str = get_jalali_update_time()

    # --- شروع ساخت محتوای README ---
    readme_content = f"""
<div dir="rtl" align="center">

# V2RayAggregator | تجمیع‌کننده کانفیگ‌های V2Ray

این پروژه به صورت خودکار کانفیگ‌های فعال V2Ray را از منابع عمومی مختلف جمع‌آوری، تست و دسته‌بندی می‌کند.

</div>

<div align="center">

[![Update-Subscription](https://img.shields.io/github/actions/workflow/status/{REPO_OWNER}/{REPO_NAME}/update_all_proxies.yml?style=for-the-badge&logo=githubactions&logoColor=white&label=Update-Status)](https://github.com/{REPO_OWNER}/{REPO_NAME}/actions/workflows/update_all_proxies.yml)
[![Configs-Count](https://img.shields.io/badge/dynamic/json?label=Configs&query=message&url=https%3A%2F%2Fraw.githubusercontent.com%2F{REPO_OWNER}%2F{REPO_NAME}%2Fmaster%2F.github%2Fbadges%2Fconfigs_count.json&style=for-the-badge&logo=server&logoColor=white&color=blueviolet)](https://github.com/{REPO_OWNER}/{REPO_NAME}/releases/latest/download/{ALL_CONFIGS_FILE})
[![Last-Update](https://img.shields.io/badge/dynamic/json?label=Last-Update&query=message&url=https%3A%2F%2Fraw.githubusercontent.com%2F{REPO_OWNER}%2F{REPO_NAME}%2Fmaster%2F.github%2Fbadges%2Flast_update.json&style=for-the-badge&logo=clock&logoColor=white&color=informational)](https://github.com/{REPO_OWNER}/{REPO_NAME}/commits/master)
[![LICENSE](https://img.shields.io/github/license/{REPO_OWNER}/{REPO_NAME}?style=for-the-badge&color=lightgrey)](https://github.com/{REPO_OWNER}/{REPO_NAME}/blob/master/LICENSE)

</div>

<div dir="rtl">

---

## 📥 لینک‌های اشتراک (Subscription Links)

برای استفاده، یکی از لینک‌های زیر را کپی کرده و در کلاینت خود وارد کنید.

### 🌐 لینک جامع (همه کانفیگ‌ها)

این لینک شامل **{all_connections_count:,}** کانفیگ از تمام کشورها است. **(ممکن است برای برخی کلاینت‌ها سنگین باشد)**

<div align="center">

```
{ALL_CONFIGS_URL}
```

</div>

---

### 🌍 لینک‌های تفکیک شده بر اساس کشور

- **لینک کامل:** شامل تمام کانفیگ‌های موجود برای آن کشور.
- **لینک ۱۰۰تایی:** یک لیست چرخشی شامل ۱۰۰ کانفیگ رندوم که هر ساعت به‌روز می‌شود. (**پیشنهاد شده برای استفاده روزمره**)

| پرچم | کشور | تعداد کل | لینک کامل | لینک ۱۰۰تایی |
|:---:|:---|:---:|:---:|:---:|
"""

    for country in country_data:
        readme_content += (
            f"| {country['flag']} | **{country['name']}** | `{country['full_count']:,}` "
            f"| [Full]({country['full_link']}) "
            f"| [100 Configs]({country['100_link']}) |\n"
        )

    readme_content += """
---

## ✅ کلاینت‌های پیشنهادی

برای بهترین عملکرد، از کلاینت‌های زیر استفاده کنید:

| Hiddify | v2rayNG |
| :---: | :---: |
| <a href="https://hiddify.com/next"><img src="https://hiddify.com/img/hiddify-logo-128.png" width="60"></a> | <a href="https://github.com/2dust/v2rayNG/releases"><img src="https://raw.githubusercontent.com/2dust/v2rayNG/master/app/src/main/ic_launcher-playstore.png" width="60"></a> |
| **(پیشنهاد شده)** | **(محبوب)** |

<div align="center">

| [**Windows**](https://github.com/hiddify/hiddify-next/releases) | [**Android**](https://play.google.com/store/apps/details?id=app.hiddify.com) | [**iOS**](https://apps.apple.com/us/app/hiddify-next/id6476113229) | [**macOS**](https://github.com/hiddify/hiddify-next/releases) | [**Linux**](https://github.com/hiddify/hiddify-next/releases) |
| :---: | :---: | :---: | :---: | :---: |
| <img src="https://hiddify.com/assets/platforms/windows.svg" width="30"> | <img src="https://hiddify.com/assets/platforms/android.svg" width="30"> | <img src="https://hiddify.com/assets/platforms/apple.svg" width="30"> | <img src="https://hiddify.com/assets/platforms/mac.svg" width="30"> | <img src="https://hiddify.com/assets/platforms/linux.svg" width="30"> |

</div>

</div>
"""
    # --- پایان ساخت محتوای README ---

    # ذخیره فایل README.md
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    # ساخت فایل‌های بج (برای نمایش در README)
    os.makedirs(".github/badges", exist_ok=True)
    with open(".github/badges/configs_count.json", "w") as f:
        f.write(f'{{"schemaVersion": 1, "label": "Configs", "message": "{all_connections_count:,}", "color": "blueviolet"}}')
    with open(".github/badges/last_update.json", "w") as f:
        f.write(f'{{"schemaVersion": 1, "label": "Last Update", "message": "{update_time_str.split(" - ")[1]}", "color": "informational"}}')

    print("✅ README.md and badge files generated successfully.")

if __name__ == "__main__":
    generate_readme()
