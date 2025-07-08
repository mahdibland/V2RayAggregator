import requests
from datetime import datetime
import pytz
import jdatetime

# تنظیمات
BASE_URL = "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/main/Countries"
ALL_COUNTRIES_URL = "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/main/all_configs.txt"
COUNTRY_NAMES = {
    "al": ("آلبانی", "🇦🇱"),
    "ar": ("آرژانتین", "🇦🇷"),
    "am": ("ارمنستان", "🇦🇲"),
    "au": ("استرالیا", "🇦🇺"),
    "at": ("اتریش", "🇦🇹"),
    "az": ("آذربایجان", "🇦🇿"),
    "bh": ("بحرین", "🇧🇭"),
    "be": ("بلژیک", "🇧🇪"),
    "bo": ("بولیوی", "🇧🇴"),
    "ba": ("بوسنی و هرزگوین", "🇧🇦"),
    "br": ("برزیل", "🇧🇷"),
    "bg": ("بلغارستان", "🇧🇬"),
    "ca": ("کانادا", "🇨🇦"),
    "cl": ("شیلی", "🇨🇱"),
    "cn": ("چین", "🇨🇳"),
    "co": ("کلمبیا", "🇨🇴"),
    "cr": ("کاستاریکا", "🇨🇷"),
    "hr": ("کرواسی", "🇭🇷"),
    "cy": ("قبرس", "🇨🇾"),
    "cz": ("جمهوری چک", "🇨🇿"),
    "de": ("آلمان", "🇩🇪"),
    "dk": ("دانمارک", "🇩🇰"),
    "ec": ("اکوادور", "🇪🇨"),
    "ee": ("استونی", "🇪🇪"),
    "fi": ("فنلاند", "🇫🇮"),
    "fr": ("فرانسه", "🇫🇷"),
    "gi": ("جبل‌الطارق", "🇬🇮"),
    "gr": ("یونان", "🇬🇷"),
    "hk": ("هنگ‌کنگ", "🇭🇰"),
    "hu": ("مجارستان", "🇭🇺"),
    "is": ("ایسلند", "🇮🇸"),
    "in": ("هند", "🇮🇳"),
    "id": ("اندونزی", "🇮🇩"),
    "ir": ("ایران", "🇮🇷"),
    "ie": ("ایرلند", "🇮🇪"),
    "il": ("اسرائیل", "🇮🇱"),
    "it": ("ایتالیا", "🇮🇹"),
    "jp": ("ژاپن", "🇯🇵"),
    "jo": ("اردن", "🇯🇴"),
    "kz": ("قزاقستان", "🇰🇿"),
    "lv": ("لتونی", "🇱🇻"),
    "lt": ("لیتوانی", "🇱🇹"),
    "lu": ("لوکزامبورگ", "🇱🇺"),
    "my": ("مالزی", "🇲🇾"),
    "mt": ("مالت", "🇲🇹"),
    "mu": ("موریس", "🇲🇺"),
    "mx": ("مکزیک", "🇲🇽"),
    "md": ("مولداوی", "🇲🇩"),
    "nz": ("نیوزیلند", "🇳🇿"),
    "mk": ("مقدونیه شمالی", "🇲🇰"),
    "no": ("نروژ", "🇳🇴"),
    "py": ("پاراگوئه", "🇵🇾"),
    "pl": ("لهستان", "🇵🇱"),
    "pt": ("پرتغال", "🇵🇹"),
    "ro": ("رومانی", "🇷🇴"),
    "ru": ("روسیه", "🇷🇺"),
    "sa": ("عربستان سعودی", "🇸🇦"),
    "rs": ("صربستان", "🇷🇸"),
    "sc": ("سیشل", "🇸🇨"),
    "sg": ("سنگاپور", "🇸🇬"),
    "sk": ("اسلواکی", "🇸🇰"),
    "si": ("اسلوونی", "🇸🇮"),
    "za": ("آفریقای جنوبی", "🇿🇦"),
    "kr": ("کره جنوبی", "🇰🇷"),
    "es": ("اسپانیا", "🇪🇸"),
    "se": ("سوئد", "🇸🇪"),
    "ch": ("سوئیس", "🇨🇭"),
    "tw": ("تایوان", "🇹🇼"),
    "th": ("تایلند", "🇹🇭"),
    "tr": ("ترکیه", "🇹🇷"),
    "ua": ("اوکراین", "🇺🇦"),
    "ae": ("امارات متحده عربی", "🇦🇪"),
    "gb": ("بریتانیا", "🇬🇧"),
    "us": ("ایالات متحده", "🇺🇸"),
    "un": ("نامشخص", "🌐"),
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
    # لیست فایل‌های کشورها
    COUNTRY_FILES = [
        "Albania.txt", "Argentina.txt", "Armenia.txt", "Au.txt", "Australia.txt", "Austria.txt",
        "Azerbaijan.txt", "Bahrain.txt", "Belgium.txt", "Bolivia.txt", "Bosnia_And_Herzegovina.txt",
        "Brazil.txt", "Bulgaria.txt", "Canada.txt", "Chile.txt", "China.txt", "Colombia.txt",
        "Costa_Rica.txt", "Cr.txt", "Croatia.txt", "Cyprus.txt", "Czechia.txt", "De.txt",
        "Denmark.txt", "Ecuador.txt", "Estonia.txt", "Finland.txt", "France.txt", "Germany.txt",
        "Gibraltar.txt", "Greece.txt", "Hong_Kong.txt", "Hungary.txt", "Iceland.txt", "India.txt",
        "Indonesia.txt", "Iran.txt", "Ireland.txt", "Israel.txt", "Italy.txt", "Japan.txt",
        "Jordan.txt", "Kazakhstan.txt", "Latvia.txt", "Lithuania.txt", "Luxembourg.txt",
        "Malaysia.txt", "Malta.txt", "Mauritius.txt", "Mexico.txt", "Moldova.txt", "New_Zealand.txt",
        "North_Macedonia.txt", "Norway.txt", "Paraguay.txt", "Poland.txt", "Portugal.txt",
        "Romania.txt", "Russia.txt", "Saudi_Arabia.txt", "Serbia.txt", "Seychelles.txt",
        "Singapore.txt", "Slovakia.txt", "Slovenia.txt", "South_Africa.txt", "South_Korea.txt",
        "Spain.txt", "Sweden.txt", "Switzerland.txt", "Taiwan.txt", "Thailand.txt",
        "The_Netherlands.txt", "Türkiye.txt", "Ukraine.txt", "United_Arab_Emirates.txt",
        "United_Kingdom.txt", "United_States.txt", "Unknown.txt", "Us.txt", "Vietnam.txt", "Vn.txt"
    ]

    # جمع‌آوری اطلاعات کشورها
    country_data = []
    for file_name in COUNTRY_FILES:
        # استخراج کد کشور
        country_code = file_name.lower().replace('.txt', '').replace('_', '')
        if file_name == "Hong_Kong.txt":
            country_code = "hk"
            name = COUNTRY_NAMES.get("hk", (file_name.replace('.txt', '').replace('_', ' '), ""))[0]
            flag = COUNTRY_NAMES.get("hk", ("", ""))[1]
        elif file_name == "Au.txt":
            country_code = "au"
            name = COUNTRY_NAMES.get("au", (file_name.replace('.txt', '').replace('_', ' '), ""))[0]
            flag = COUNTRY_NAMES.get("au", ("", ""))[1]
        elif file_name == "Cr.txt":
            country_code = "cr"
            name = COUNTRY_NAMES.get("cr", (file_name.replace('.txt', '').replace('_', ' '), ""))[0]
            flag = COUNTRY_NAMES.get("cr", ("", ""))[1]
        elif file_name == "De.txt":
            country_code = "de"
            name = COUNTRY_NAMES.get("de", (file_name.replace('.txt', '').replace('_', ' '), ""))[0]
            flag = COUNTRY_NAMES.get("de", ("", ""))[1]
        elif file_name in ["United_States.txt", "Us.txt"]:
            country_code = "us"
            name = COUNTRY_NAMES.get("us", (file_name.replace('.txt', '').replace('_', ' '), ""))[0]
            flag = COUNTRY_NAMES.get("us", ("", ""))[1]
        elif file_name in ["Vietnam.txt", "Vn.txt"]:
            country_code = "vn"
            name = COUNTRY_NAMES.get("vn", (file_name.replace('.txt', '').replace('_', ' '), ""))[0]
            flag = COUNTRY_NAMES.get("vn", ("", ""))[1]
        elif file_name == "Unknown.txt":
            country_code = "un"
            name = COUNTRY_NAMES.get("un", (file_name.replace('.txt', '').replace('_', ' '), ""))[0]
            flag = COUNTRY_NAMES.get("un", ("", ""))[1]
        else:
            country_code = country_code[:2]  # دو حرف اول برای کد کشور
            name = COUNTRY_NAMES.get(country_code, (file_name.replace('.txt', '').replace('_', ' '), ""))[0]
            flag = COUNTRY_NAMES.get(country_code, ("", ""))[1]

        url = f"{BASE_URL}/{file_name}"
        connections = count_connections(url)
        country_data.append({
            'code': country_code,
            'name': name,
            'flag': flag,
            'connections': connections,
            'file': file_name,
            'link': url
        })

    # گرفتن تعداد کانکشن‌های همه کشورها
    all_connections = count_connections(ALL_COUNTRIES_URL)

    # مرتب‌سازی بر اساس تعداد کانکشن‌ها
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
    ] + sorted(country_data, key=lambda x: x['connections'], reverse=True)

    # زمان فعلی به وقت تهران
    tehran_tz = pytz.timezone('Asia/Tehran')
    update_time = datetime.now(tehran_tz).strftime("%Y-%m-%d %H:%M:%S")
    jalali_date = get_jalali_date()

    # تولید محتوای README
    readme_content = f"""# لینک‌های وی‌پی‌ان اختصاصی هر کشور

این صفحه شامل لینک‌های خام برای فایل‌های کانکشن وی‌پی‌ان است که هر کدام به یک کشور خاص اختصاص دارند. این فایل‌ها هر ۱۵ دقیقه به‌صورت خودکار به‌روزرسانی می‌شوند.

**آخرین به‌روزرسانی**: {jalali_date} - {update_time} (به وقت تهران)

| پرچم | نام کشور | کد کشور | تعداد کانکشن‌ها | لینک کانکشن |
|:----:|:--------:|:------:|:---------------:|:-----------:|
"""
    for country in sorted_data:
        readme_content += f"| {country['flag']} | {country['name']} | {country['code'].upper()} | {country['connections']} | [{country['file']}]({country['link']}) |\n"

    readme_content += """
## نکات
- **همه کشورها** شامل تمام کانکشن‌های منبع است و در ابتدای لیست قرار دارد.
- **ایالات متحده** به‌صورت جداگانه با فایل‌های `United_States.txt` و `Us.txt` نمایش داده شده است.
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
