import os
import glob
from datetime import datetime, timedelta
import pytz
import requests

# مسیر پوشه sub
SUB_DIR = "sub"
# آدرس پایه برای لینک‌های خام
BASE_URL = "https://raw.githubusercontent.com/MEHR1DAD/V2RayAggregator/refs/heads/master/sub"
# لینک منبع همه کشورها
ALL_COUNTRIES_URL = "https://raw.githubusercontent.com/mahdibland/SSAggregator/master/sub/sub_merge.txt"
# نام کشور و پرچم برای کدهای ISO 3166-1 alpha-2
COUNTRY_NAMES = {
    "us": ("ایالات متحده", "🇺🇸"),
    "ae": ("امارات متحده عربی", "🇦🇪"),
    "al": ("آلبانی", "🇦🇱"),
    "am": ("ارمنستان", "🇦🇲"),
    "at": ("اتریش", "🇦🇹"),
    "au": ("استرالیا", "🇦🇺"),
    "az": ("آذربایجان", "🇦🇿"),
    "ba": ("بوسنی و هرزگوین", "🇧🇦"),
    "be": ("بلژیک", "🇧🇪"),
    "bg": ("بلغارستان", "🇧🇬"),
    "bo": ("بولیوی", "🇧🇴"),
    "br": ("برزیل", "🇧🇷"),
    "bz": ("بلیز", "🇧🇿"),
    "ca": ("کانادا", "🇨🇦"),
    "ch": ("سوئیس", "🇨🇭"),
    "cn": ("چین", "🇨🇳"),
    "co": ("کلمبیا", "🇨🇴"),
    "cr": ("کاستاریکا", "🇨🇷"),
    "cy": ("قبرس", "🇨🇾"),
    "cz": ("جمهوری چک", "🇨🇿"),
    "de": ("آلمان", "🇩🇪"),
    "dk": ("دانمارک", "🇩🇰"),
    "ec": ("اکوادور", "🇪🇨"),
    "ee": ("استونی", "🇪🇪"),
    "es": ("اسپانیا", "🇪🇸"),
    "fi": ("فنلاند", "🇫🇮"),
    "fr": ("فرانسه", "🇫🇷"),
    "gb": ("بریتانیا", "🇬🇧"),
    "gr": ("یونان", "🇬🇷"),
    "hk": ("هنگ‌کنگ", "🇭🇰"),
    "hr": ("کرواسی", "🇭🇷"),
    "id": ("اندونزی", "🇮🇩"),
    "ie": ("ایرلند", "🇮🇪"),
    "in": ("هند", "🇮🇳"),
    "ir": ("ایران", "🇮🇷"),
    "is": ("ایسلند", "🇮🇸"),
    "it": ("ایتالیا", "🇮🇹"),
    "jp": ("ژاپن", "🇯🇵"),
    "kr": ("کره جنوبی", "🇰🇷"),
    "kz": ("قزاقستان", "🇰🇿"),
    "lt": ("لیتوانی", "🇱🇹"),
    "lu": ("لوکزامبور", "🇱🇺"),
    "lv": ("لتونی", "🇵🇸"),
    "md": ("مولداوی", "🇲🇩"),
    "mk": ("مقدونیه شمالی", "🇲🇰"),
    "mn": ("مغولستان", "🇲🇳"),
    "mo": ("ماکاو", "🇲🇴"),
    "mt": ("مالت", "🇲🇹"),
    "mu": ("موریس", "🇲🇺"),
    "mx": ("مکزیک", "🇲🇽"),
 Lantigua    "my": ("مالزی", "🇲🇾"),
    "ng": ("نیجریه", "🇳🇬"),
    "nl": ("هلند", "🇳🇱"),
    "no": ("نروژ", "🇳🇴"),
    "pa": ("پاناما", "🇵🇦"),
    "pe": ("پرو", "🇵🇪"),
    "ph": ("فیلیپین", "🇵🇭"),
    "pl": ("لهستان", "🇵🇱"),
    "pr": ("پورتوریکو", "🇵🇷"),
    "pt": ("پرتغال", "🇵🇹"),
    "py": ("پاراگوئه", "🇵🇾"),
    "ro": ("رومانی", "🇷🇴"),
    "rs": ("صربستان", "🇷🇸"),
    "ru": ("روسیه", "🇷🇺"),
    "sc": ("سیشل", "🇸🇨"),
    "se": ("سوئد", "🇸🇪"),
    "sg": ("سنگاپور", "🇸🇬"),
    "si": ("اسلوونی", "🇸🇮"),
    "sk": ("اسلواکی", "🇸🇰"),
    "th": ("تایلند", "🇹🇭"),
    "tr": ("ترکیه", "🇹🇷"),
    "tw": ("تایوان", "🇹🇼"),
    "ua": ("اوکراین", "🇺🇦"),
    "vg": ("جزایر ویرجین بریتانیا", "🇻🇬"),
    "vn": ("ویتنام", "🇻🇳"),
    "za": ("آفریقای جنوبی", "🇿🇦")
}

def count_connections(file_path):
    """شمردن تعداد خطوط (کانکشن‌ها) در یک فایل"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return sum(1 for line in f if line.strip())
    except Exception as e:
        print(f"خطا در خواندن فایل {file_path}: {e}")
        return 0

def count_all_connections():
    """شمردن تعداد کانکشن‌ها در فایل منبع همه کشورها"""
    try:
        response = requests.get(ALL_COUNTRIES_URL, timeout=10)
        response.raise_for_status()
        return len([line for line in response.text.splitlines() if line.strip()])
    except requests.RequestException as e:
        print(f"خطا در گرفتن {ALL_COUNTRIES_URL}: {e}")
        return 0

def get_file_update_time(file_path):
    """گرفتن زمان آخرین به‌روزرسانی فایل به وقت تهران"""
    try:
        mtime = os.path.getmtime(file_path)
        tehran_tz = pytz.timezone('Asia/Tehran')
        update_time = datetime.fromtimestamp(mtime, tehran_tz)
        return update_time.strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        print(f"خطا در گرفتن زمان فایل {file_path}: {e}")
        return "نامشخص"

def get_relative_time():
    """محاسبه زمان نسبی (مثل امروز X ساعت پیش) نسبت به ساعت سرور"""
    tehran_tz = pytz.timezone('Asia/Tehran')
    now = datetime.now(tehran_tz)
    update_time = now  # فرض می‌کنیم به‌روزرسانی همین حالا انجام شده
    delta = now - update_time
    hours = int(delta.total_seconds() // 3600)
    days = delta.days

    if days == 0:
        day_str = "امروز"
    elif days == 1:
        day_str = "دیروز"
    elif days == 2:
        day_str = "پریروز"
    else:
        day_str = update_time.strftime("%Y-%m-%d")

    return f"{day_str} - {hours} ساعت پیش"

def generate_readme():
    """تولید فایل VPN_LINKS.md"""
    # جمع‌آوری اطلاعات فایل‌ها
    country_data = []
    for file_path in glob.glob(os.path.join(SUB_DIR, "*_only_sub.txt")):
        file_name = os.path.basename(file_path)
        country_code = file_name.split('_')[0].lower()
        if country_code in COUNTRY_NAMES:
            connections = count_connections(file_path)
            update_time = get_file_update_time(file_path)
            country_data.append({
                'code': country_code,
                'name': COUNTRY_NAMES[country_code][0],
                'flag': COUNTRY_NAMES[country_code][1],
                'connections': connections,
                'update_time': update_time,
                'file': file_name
            })

    # گرفتن تعداد کانکشن‌های همه کشورها
    all_connections = count_all_connections()

    # جدا کردن آمریکا و مرتب‌سازی بقیه بر اساس تعداد کانکشن‌ها
    us_data = next((item for item in country_data if item['code'] == 'us'), None)
    other_countries = [item for item in country_data if item['code'] != 'us']
    other_countries.sort(key=lambda x: x['connections'], reverse=True)

    # ترکیب لیست: همه کشورها، آمریکا، بقیه
    sorted_data = [
        {
            'code': 'all',
            'name': 'همه کشورها',
            'flag': '🌍',
            'connections': all_connections,
            'update_time': datetime.now(pytz.timezone('Asia/Tehran')).strftime("%Y-%m-%d %H:%M:%S"),
            'file': ALL_COUNTRIES_URL.split('/')[-1],
            'link': ALL_COUNTRIES_URL
        }
    ] + ([us_data] if us_data else []) + other_countries

    # زمان فعلی به وقت تهران
    tehran_tz = pytz.timezone('Asia/Tehran')
    update_time = datetime.now(tehran_tz).strftime("%Y-%m-%d %H:%M:%S")
    relative_time = get_relative_time()

    # تولید محتوای README
    readme_content = f"""# لینک‌های وی‌پی‌ان اختصاصی هر کشور

این صفحه شامل لینک‌های خام برای فایل‌های کانکشن وی‌پی‌ان است که هر کدام به یک کشور خاص اختصاص دارند. این فایل‌ها هر ۶ ساعت به‌صورت خودکار به‌روزرسانی می‌شوند.

**آخرین به‌روزرسانی**: {relative_time} - {update_time} (به وقت تهران)

| پرچم | نام کشور | کد کشور | تعداد کانکشن‌ها | آخرین به‌روزرسانی | لینک کانکشن |
|------|----------|---------|------------------|-------------------|-------------|
"""

    for country in sorted_data:
        link = country.get('link', f"{BASE_URL}/{country['file']}")
        readme_content += f"| {country['flag']} | {country['name']} | {country['code'].upper()} | {country['connections']} | {country['update_time']} | [{country['file']}]({link}) |\n"

    readme_content += """
## نکات
- **همه کشورها** شامل تمام کانکشن‌های منبع است و در ابتدای لیست قرار دارد.
- **ایالات متحده** پس از همه کشورها و سایر کشورها بر اساس تعداد کانکشن‌ها (از بیشترین به کمترین) مرتب شده‌اند.
- برای **جستجوی کشور**، از Ctrl+F استفاده کنید و نام کشور (مثل «ایران») یا کد کشور (مثل «IR») را جستجو کنید.
- برای **مرتب‌سازی الفبایی**، جدول را کپی کرده و در یک ویرایشگر (مثل Excel یا Notepad) بر اساس نام کشور مرتب کنید.
- هر فایل شامل کانکشن‌های اختصاصی برای کشور مربوطه است که با کلاینت‌هایی مثل Hiddify سازگارند.
- اگر کشور جدیدی به منبع داده اضافه شود، به‌طور خودکار در این لیست ظاهر خواهد شد.

## منبع داده
- داده‌ها از [SSAggregator](https://raw.githubusercontent.com/mahdibland/SSAggregator/master/sub/sub_merge.txt) استخراج شده‌اند.

## استفاده از کانکشن‌ها
این کانکشن‌ها را می‌توانید به تناسب سیستم‌عامل خود در برنامه **Hiddify** استفاده کنید:

- ![Android](https://hiddify.com/assets/platforms/android.svg) [Hiddify برای Android](https://play.google.com/store/apps/details?id=app.hiddify.com)
- ![iOS](https://hiddify.com/assets/platforms/apple.svg) [Hiddify برای iOS](https://apps.apple.com/us/app/hiddify-proxy-vpn/id6596777532?platform=iphone)
- ![Windows](https://hiddify.com/assets/platforms/windows.svg) [Hiddify برای Windows](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Windows-Setup-x64.Msix)
- ![macOS](https://hiddify.com/assets/platforms/mac.svg) [Hiddify برای macOS](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-MacOS.dmg)
- ![Linux](https://hiddify.com/assets/platforms/linux.svg) [Hiddify برای Linux](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Linux-x64.AppImage)
"""

    # ذخیره فایل VPN_LINKS.md
    with open("VPN_LINKS.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

if __name__ == "__main__":
    generate_readme()
