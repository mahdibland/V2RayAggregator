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

    # مرتب‌سازی کشورها بر اساس تعداد کانکشن (بیشترین به کمترین)
    country_data.sort(key=lambda x: x['full_count'], reverse=True)

    all_connections_count = count_connections(ALL_CONFIGS_FILE)
    jalali_date_str = get_jalali_update_time()
    
    # URL انکود کردن تاریخ برای بج
    encoded_date = quote(jalali_date_str)

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

---

### 💡 ویژگی‌ها

- <b>تجمیع خودکار:</b> جمع‌آوری روزانه کانفیگ از ده‌ها منبع عمومی.
- <b>پاک‌سازی هوشمند:</b> حذف خودکار منابع از کار افتاده و جایگزینی با منابع جدید.
- <b>تفکیک جغرافیایی:</b> دسته‌بندی کانفیگ‌ها بر اساس کشور برای دسترسی آسان.
- <b>لینک‌های چرخشی:</b> ارائه لیست‌های ۱۰۰تایی که <b>هر ساعت</b> به‌روز می‌شوند تا همیشه کانفیگ تازه در دسترس باشد.
- <b>آپدیت مداوم:</b> کل فرآیند به صورت خودکار و ساعتی توسط GitHub Actions اجرا می‌شود.

---

## 📥 لینک‌های اشتراک (Subscription Links)

<div align="center">

### 🌐 لینک جامع (همه کانفیگ‌ها)
<p dir="rtl">این لینک شامل <b>{all_connections_count:,}</b> کانفیگ از تمام کشورها است. (<b>ممکن است برای برخی کلاینت‌ها سنگین باشد</b>)</p>

```
{ALL_CONFIGS_URL}
```

---

### 🌍 لینک‌های تفکیک شده بر اساس کشور
<p dir="rtl">
برای مشاهده لینک‌ها، روی نام هر کشور کلیک کنید.
</p>
</div>

"""

    for country in country_data:
        readme_content += f"""
<details>
<summary>
  <div dir="rtl" align="right">
    <b>{country['flag']} {country['name']}</b> (تعداد کل: {country['full_count']:,})
  </div>
</summary>

<div dir="rtl">
<br>

<p>
- <b>لینک کامل:</b> شامل تمام کانفیگ‌های موجود برای این کشور.<br>
- <b>لینک ۱۰۰تایی:</b> یک لیست چرخشی شامل ۱۰۰ کانفیگ رندوم که هر ساعت به‌روز می‌شود. (<b>پیشنهاد شده</b>)
</p>

<p><b>لینک کامل:</b></p>
<div align="center">

```
{country['full_link']}
```
</div>

<p><b>لینک ۱۰۰تایی:</b></p>
<div align="center">

```
{country['100_link']}
```
</div>

</div>
</details>
"""

    readme_content += """
<div dir="rtl">

---

## ✅ نرم‌افزارهای پیشنهادی

<div align="center">

### لیست کلاینت‌های موبایل (Mobile Clients)

| iOS/iPadOS | Android | توضیحات مختصر |
| :---: | :---: | :---: |
| <b>[Hiddify](https://apps.apple.com/us/app/hiddify-next/id6476113229)</b> | <b>[Hiddify](https://play.google.com/store/apps/details?id=app.hiddify.com)</b> | <p dir="rtl">رایگان، چند پلتفرمی و با پشتیبانی از تمام پروتکل‌ها.</p> |
| [V2Box](https://apps.apple.com/us/app/v2box-v2ray-client/id6446814690) | [v2rayNG](https://github.com/2dust/v2rayNG/releases) | <p dir="rtl">کلاینت‌های محبوب و قدرتمند برای هر پلتفرم.</p> |
| [Shadowrocket](https://apps.apple.com/us/app/shadowrocket/id932747118) | [NekoBox](https://github.com/MatsuriDayo/NekoBoxForAndroid/releases) | <p dir="rtl">پشتیبانی از پروتکل‌های متنوع، نیازمند خرید یا تنظیمات پیشرفته.</p> |
| [Streisand](https://apps.apple.com/us/app/streisand/id6450534064) | [Clash For Android](https://github.com/Kr328/ClashForAndroid/releases) | <p dir="rtl">بر پایه Clash با قابلیت‌های مدیریت پروکسی حرفه‌ای.</p> |

<br>

### لیست کلاینت‌های دسکتاپ (Desktop Clients)

| Windows | macOS | Linux | توضیحات مختصر |
| :---: | :---: | :---: | :---: |
| <b>[Hiddify](https://github.com/hiddify/hiddify-next/releases)</b> | <b>[Hiddify](https://github.com/hiddify/hiddify-next/releases)</b> | <b>[Hiddify](https://github.com/hiddify/hiddify-next/releases)</b> | <p dir="rtl">رایگان، چند پلتفرمی و با کاربری آسان. (پیشنهاد اصلی)</p> |
| [Nekoray](https://github.com/MatsuriDayo/nekoray/releases) | [V2Box](https://apps.apple.com/us/app/v2box-v2ray-client/id6446814690) | [Nekoray](https://github.com/MatsuriDayo/nekoray/releases) | <p dir="rtl">ابزارهای قدرتمند با قابلیت‌های پیشرفته برای مدیریت پروکسی.</p> |
| [v2rayN](https://github.com/2dust/v2rayN/releases) | [FoXray](https://github.com/Fndroid/Foxray/releases) | [Clash Verge](https://github.com/zzzgydi/clash-verge/releases) | <p dir="rtl">کلاینت‌های محبوب با جامعه کاربری بزرگ و پشتیبانی گسترده.</p> |

</div>

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
