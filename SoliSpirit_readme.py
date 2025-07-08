import requests
from datetime import datetime
import pytz
import jdatetime

# تنظیمات
BASE_URL = "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/main/Countries"
ALL_COUNTRIES_URL = "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/main/all_configs.txt"
COUNTRY_NAMES = {
    "ar": ("آرژانتین", "🇦🇷"),
    "au": ("استرالیا", "🇦🇺"),
    "at": ("اتریش", "🇦🇹"),
    "be": ("بلژیک", "🇧🇪"),
    "br": ("برزیل", "🇧🇷"),
    "ca": ("کانادا", "🇨🇦"),
    "cl": ("شیلی", "🇨🇱"),
    "cn": ("چین", "🇨🇳"),
    "co": ("کلمبیا", "🇨🇴"),
    "cz": ("جمهوری چک", "🇨🇿"),
    "dk": ("دانمارک", "🇩🇰"),
    "fi": ("فنلاند", "🇫🇮"),
    "fr": ("فرانسه", "🇫🇷"),
    "de": ("آلمان", "🇩🇪"),
    "hk": ("هنگ‌کنگ", "🇭🇰"),
    "in": ("هند", "🇮🇳"),
    "id": ("اندونزی", "🇮🇩"),
    "ie": ("ایرلند", "🇮🇪"),
    "it": ("ایتالیا", "🇮🇹"),
    "jp": ("ژاپن", "🇯🇵"),
    "my": ("مالزی", "🇲🇾"),
    "mx": ("مکزیک", "🇲🇽"),
    "nl": ("هلند", "🇳🇱"),
    "nz": ("نیوزیلند", "🇳🇿"),
    "no": ("نروژ", "🇳🇴"),
    "ph": ("فیلیپین", "🇵🇭"),
    "pl": ("لهستان", "🇵🇱"),
    "pt": ("پرتغال", "🇵🇹"),
    "ru": ("روسیه", "🇷🇺"),
    "sg": ("سنگاپور", "🇸🇬"),
    "za": ("آفریقای جنوبی", "🇿🇦"),
    "kr": ("کره جنوبی", "🇰🇷"),
    "es": ("اسپانیا", "🇪🇸"),
    "se": ("سوئد", "🇸🇪"),
    "ch": ("سوئیس", "🇨🇭"),
    "tw": ("تایوان", "🇹🇼"),
    "th": ("تایلند", "🇹🇭"),
    "tr": ("ترکیه", "🇹🇷"),
    "ua": ("اوکراین", "🇺🇦"),
    "gb": ("بریتانیا", "🇬🇧"),
    "us": ("ایالات متحده", "🇺🇸"),
    "vn": ("ویتنام", "🇻🇳")
}

def count_connections(url):
    """شمردن تعداد کانکشن‌ها در یک فایل"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return len([line for line in response.text.splitlines() if line.strip()])
    except requests.RequestException as e:
        print(f"خطا در گرفتن {url}: {e}")
        return 0

def get_jalali_date():
    """گرفتن تاریخ و روز هفته به فرمت جلالی"""
    tehran_tz = pytz.timezone('Asia/Tehran')
    now = datetime.now(tehran_tz)
    jalali_date = jdatetime.datetime.fromgregorian(datetime=now)
    day_name = jalali_date.strftime("%A")
    day = jalali_date.day
    month = jalali_date.strftime('%B')
    year = jalali_date.year
    return f"{day_name} - {day} {month} {year}"

def generate_readme():
    """تولید فایل SoliSpirit.md برای مخزن SoliSpirit"""
    # جمع‌آوری اطلاعات کشورها
    country_data = []
    for country_code, (country_name, flag) in COUNTRY_NAMES.items():
        file_name = f"{country_code.capitalize()}.txt" if country_code != "hk" else "HongKong.txt"
        url = f"{BASE_URL}/{file_name}"
        connections = count_connections(url)
        country_data.append({
            'code': country_code,
            'name': country_name,
            'flag': flag,
            'connections': connections,
            'file': file_name,
            'link': url
        })

    # گرفتن تعداد کانکشن‌های همه کشورها
    all_connections = count_connections(ALL_COUNTRIES_URL)

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
            'file': 'all_configs.txt',
            'link': ALL_COUNTRIES_URL
        }
    ] + ([us_data] if us_data else []) + other_countries

    # زمان فعلی به وقت تهران
    tehran_tz = pytz.timezone('Asia/Tehran')
    update_time = datetime.now(tehran_tz).strftime("%Y-%m-%d %H:%M:%S")
    jalali_date = get_jalali_date()

    # تولید محتوای README
    readme_content = f"""# لینک‌های وی‌پی‌ان اختصاصی هر کشور

این صفحه شامل لینک‌های خام برای فایل‌های کانکشن وی‌پی‌ان است که هر کدام به یک کشور خاص اختصاص دارند. این فایل‌ها هر ۱۵ دقیقه به‌صورت خودکار به‌روزرسانی می‌شوند.

**آخرین به‌روزرسانی**: {jalali_date} - {update_time} (به وقت تهران)

| پرچم | نام کشور | کد کشور | تعداد کانکشن‌ها | لینک کانکشن |
|------|----------|---------|------------------|-------------|
"""
    for country in sorted_data:
        readme_content += f"| {country['flag']} | {country['name']} | {country['code'].upper()} | {country['connections']} | [{country['file']}]({country['link']}) |\n"

    readme_content += """
## نکات
- **همه کشورها** شامل تمام کانکشن‌های منبع است و در ابتدای لیست قرار دارد.
- **ایالات متحده** پس از همه کشورها و سایر کشورها بر اساس تعداد کانکشن‌ها (از بیشترین به کمترین) مرتب شده‌اند.
- برای **جستجوی کشور**، از Ctrl+F استفاده کنید و نام کشور (مثل «ایران») یا کد کشور (مثل «IR») را جستجو کنید.
- برای **مرتب‌سازی الفبایی**، جدول را کپی کرده و در یک ویرایشگر (مثل Excel یا Notepad) بر اساس نام کشور مرتب کنید.
- هر فایل شامل کانکشن‌های اختصاصی برای کشور مربوطه است که با کلاینت‌هایی مثل Hiddify سازگارند.

## منبع داده
- داده‌ها از [SoliSpirit/v2ray-configs](https://github.com/SoliSpirit/v2ray-configs) استخراج شده‌اند.

## استفاده از کانکشن‌ها
این کانکشن‌ها را می‌توانید به تناسب سیستم‌عامل خود در برنامه **Hiddify** استفاده کنید:

- ![Android](https://hiddify.com/assets/platforms/android.svg) [Hiddify برای Android](https://play.google.com/store/apps/details?id=app.hiddify.com)
- ![iOS](https://hiddify.com/assets/platforms/apple.svg) [Hiddify برای iOS](https://apps.apple.com/us/app/hiddify-proxy-vpn/id6596777532?platform=iphone)
- ![Windows](https://hiddify.com/assets/platforms/windows.svg) [Hiddify برای Windows](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Windows-Setup-x64.Msix)
- ![macOS](https://hiddify.com/assets/platforms/mac.svg) [Hiddify برای macOS](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-MacOS.dmg)
- ![Linux](https://hiddify.com/assets/platforms/linux.svg) [Hiddify برای Linux](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Linux-x64.AppImage)
"""

    # ذخیره فایل
    with open("SoliSpirit.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

if __name__ == "__main__":
    generate_readme()
