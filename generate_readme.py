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
    jalali_date = jdatetime.datetime.fromgregorian(datetime=now_tehran)
    
    day_name = jalali_date.strftime("%A")
    day = jalali_date.day
    month_name = jalali_date.strftime('%B')
    year = jalali_date.year
    
    return f"{day_name} {day} {month_name} {year}"

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

    country_data.sort(key=lambda x: x['name'])
    all_connections_count = count_connections(ALL_CONFIGS_FILE)
    jalali_date_str = get_jalali_update_time()
    
    encoded_label_configs = quote("تعداد کانفیگ‌ها")
    encoded_label_update = quote("آخرین آپدیت")
    encoded_date = quote(jalali_date_str)

    # --- شروع ساخت محتوای README ---
    readme_content = f"""
<div dir="rtl" align="center">

# V2RayAggregator | تجمیع‌کننده کانفیگ‌های V2Ray

این پروژه به صورت خودکار کانفیگ‌های فعال V2Ray را از منابع عمومی مختلف جمع‌آوری، تست و دسته‌بندی می‌کند.

</div>

<div align="center">

[![Update-Subscription](https://img.shields.io/github/actions/workflow/status/{REPO_OWNER}/{REPO_NAME}/update_all_proxies.yml?style=for-the-badge&logo=githubactions&logoColor=white&label=وضعیت%20آپدیت)](https://github.com/{REPO_OWNER}/{REPO_NAME}/actions/workflows/update_all_proxies.yml)
[![Configs-Count](https://img.shields.io/badge/{encoded_label_configs}-{all_connections_count:,}-blueviolet?style=for-the-badge&logo=server&logoColor=white)](https://github.com/{REPO_OWNER}/{REPO_NAME}/releases/latest/download/{ALL_CONFIGS_FILE})
[![Last-Update](https://img.shields.io/badge/{encoded_label_update}-{encoded_date}-informational?style=for-the-badge&logo=clock&logoColor=white)](https://github.com/{REPO_OWNER}/{REPO_NAME}/commits/master)
[![LICENSE](https://img.shields.io/github/license/{REPO_OWNER}/{REPO_NAME}?style=for-the-badge&color=lightgrey)](https://github.com/{REPO_OWNER}/{REPO_NAME}/blob/master/LICENSE)

</div>

<div dir="rtl">

---

### 💡 ویژگی‌ها

- **تجمیع خودکار:** جمع‌آوری روزانه کانفیگ از ده‌ها منبع عمومی.
- **پاک‌سازی هوشمند:** حذف خودکار منابع از کار افتاده و جایگزینی با منابع جدید.
- **تفکیک جغرافیایی:** دسته‌بندی کانفیگ‌ها بر اساس کشور برای دسترسی آسان.
- **لینک‌های چرخشی:** ارائه لیست‌های ۱۰۰تایی که **هر ساعت** به‌روز می‌شوند تا همیشه کانفیگ تازه در دسترس باشد.
- **آپدیت مداوم:** کل فرآیند به صورت خودکار و ساعتی توسط GitHub Actions اجرا می‌شود.

---

## 📥 لینک‌های اشتراک (Subscription Links)

<div align="center">

### 🌐 لینک جامع (همه کانفیگ‌ها)
این لینک شامل **{all_connections_count:,}** کانفیگ از تمام کشورها است. **(ممکن است برای برخی کلاینت‌ها سنگین باشد)**

```
{ALL_CONFIGS_URL}
```

---

### 🌍 لینک‌های تفکیک شده بر اساس کشور
- **لینک کامل:** شامل تمام کانفیگ‌های موجود برای آن کشور.
- **لینک ۱۰۰تایی:** یک لیست چرخشی شامل ۱۰۰ کانفیگ رندوم که هر ساعت به‌روز می‌شود. (**پیشنهاد شده**)

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
</div>

---

## ✅ نرم‌افزارهای پیشنهادی

<div align="center">

### راهنمای تصویری کلاینت‌ها

| [**Hiddify**](https://hiddify.com/next) | [**v2rayNG**](https://github.com/2dust/v2rayNG/releases) | [**Nekoray**](https://github.com/MatsuriDayo/nekoray/releases) |
| :---: | :---: | :---: |
| <img src="https://raw.githubusercontent.com/hiddify/hiddify-next/main/assets/images/logo_128.png" width="80"> | <img src="https://raw.githubusercontent.com/2dust/v2rayNG/master/app/src/main/ic_launcher-playstore.png" width="80"> | <img src="https://raw.githubusercontent.com/MatsuriDayo/nekoray/master/res/logo/nekoray.png" width="80"> |
| **چند پلتفرمی (پیشنهاد اصلی)** | **اندروید (محبوب)** | **دسکتاپ (قدرتمند)** |

</div>

<br>

### لیست کلاینت‌های موبایل

| iOS/iPadOS | Android | توضیحات مختصر |
| :--- | :--- | :--- |
| **[Hiddify](https://apps.apple.com/us/app/hiddify-next/id6476113229)** | **[Hiddify](https://play.google.com/store/apps/details?id=app.hiddify.com)** | رایگان، چند پلتفرمی و با پشتیبانی از تمام پروتکل‌ها. |
| [V2Box](https://apps.apple.com/us/app/v2box-v2ray-client/id6446814690) | [v2rayNG](https://github.com/2dust/v2rayNG/releases) | کلاینت‌های محبوب و قدرتمند برای هر پلتفرم. |
| [Shadowrocket](https://apps.apple.com/us/app/shadowrocket/id932747118) | [NekoBox](https://github.com/MatsuriDayo/NekoBoxForAndroid/releases) | پشتیبانی از پروتکل‌های متنوع، نیازمند خرید یا تنظیمات پیشرفته. |
| [Streisand](https://apps.apple.com/us/app/streisand/id6450534064) | [Clash For Android](https://github.com/Kr328/ClashForAndroid/releases) | بر پایه Clash با قابلیت‌های مدیریت پروکسی حرفه‌ای. |

<br>

### لیست کلاینت‌های دسکتاپ

| Windows | macOS | Linux | توضیحات مختصر |
| :--- | :--- | :--- | :--- |
| **[Hiddify](https://github.com/hiddify/hiddify-next/releases)** | **[Hiddify](https://github.com/hiddify/hiddify-next/releases)** | **[Hiddify](https://github.com/hiddify/hiddify-next/releases)** | رایگان، چند پلتفرمی و با کاربری آسان. (پیشنهاد اصلی) |
| [Nekoray](https://github.com/MatsuriDayo/nekoray/releases) | [V2Box](https://apps.apple.com/us/app/v2box-v2ray-client/id6446814690) | [Nekoray](https://github.com/MatsuriDayo/nekoray/releases) | ابزارهای قدرتمند با قابلیت‌های پیشرفته برای مدیریت پروکسی. |
| [v2rayN](https://github.com/2dust/v2rayN/releases) | [FoXray](https://github.com/Fndroid/Foxray/releases) | [Clash Verge](https://github.com/zzzgydi/clash-verge/releases) | کلاینت‌های محبوب با جامعه کاربری بزرگ و پشتیبانی گسترده. |

---

### ⚠️ سلب مسئولیت

- این کانفیگ‌ها به صورت عمومی و خودکار جمع‌آوری شده‌اند و امنیت آن‌ها تضمین نمی‌شود.
- مسئولیت استفاده از این کانفیگ‌ها بر عهده کاربر است.
- این پروژه صرفاً برای اهداف آموزشی و تحقیقاتی ایجاد شده است.

</div>
"""
    # --- پایان ساخت محتوای README ---

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("✅ README.md generated successfully.")

if __name__ == "__main__":
    generate_readme()
