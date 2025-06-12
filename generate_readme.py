import os
import glob
from datetime import datetime
import pytz

# مسیر پوشه sub
SUB_DIR = "sub"
# آدرس پایه برای لینک‌های خام
BASE_URL = "https://raw.githubusercontent.com/MEHR1DAD/V2RayAggregator/refs/heads/master/sub"
# نام کشور برای کدهای ISO 3166-1 alpha-2
COUNTRY_NAMES = {
    "us": "ایالات متحده",
    "ae": "امارات متحده عربی",
    "al": "آلبانی",
    "am": "ارمنستان",
    "at": "اتریش",
    "au": "استرالیا",
    "az": "آذربایجان",
    "ba": "بوسنی و هرزگوین",
    "be": "بلژیک",
    "bg": "بلغارستان",
    "bo": "بولیوی",
    "br": "برزیل",
    "bz": "بلیز",
    "ca": "کانادا",
    "ch": "سوئیس",
    "cn": "چین",
    "co": "کلمبیا",
    "cr": "کاستاریکا",
    "cy": "قبرس",
    "cz": "جمهوری چک",
    "de": "آلمان",
    "dk": "دانمارک",
    "ec": "اکوادور",
    "ee": "استونی",
    "es": "اسپانیا",
    "fi": "فنلاند",
    "fr": "فرانسه",
    "gb": "بریتانیا",
    "gr": "یونان",
    "hk": "هنگ‌کنگ",
    "hr": "کرواسی",
    "id": "اندونزی",
    "ie": "ایرلند",
    "in": "هند",
    "ir": "ایران",
    "is": "ایسلند",
    "it": "ایتالیا",
    "jp": "ژاپن",
    "kr": "کره جنوبی",
    "kz": "قزاقستان",
    "lt": "لیتوانی",
    "lu": "لوکزامبورگ",
    "lv": "لتونی",
    "md": "مولداوی",
    "mk": "مقدونیه شمالی",
    "mn": "مغولستان",
    "mo": "ماکائو",
    "mt": "مالت",
    "mu": "موریس",
    "mx": "مکزیک",
    "my": "مالزی",
    "ng": "نیجریه",
    "nl": "هلند",
    "no": "نروژ",
    "pa": "پاناما",
    "pe": "پرو",
    "ph": "فیلیپین",
    "pl": "لهستان",
    "pr": "پورتوریکو",
    "pt": "پرتغال",
    "py": "پاراگوئه",
    "ro": "رومانی",
    "rs": "صربستان",
    "ru": "روسیه",
    "sc": "سیشل",
    "se": "سوئد",
    "sg": "سنگاپور",
    "si": "اسلوونی",
    "sk": "اسلواکی",
    "th": "تایلند",
    "tr": "ترکیه",
    "tw": "تایوان",
    "ua": "اوکراین",
    "vg": "جزایر ویرجین بریتانیا",
    "vn": "ویتنام",
    "za": "آفریقای جنوبی"
}

def count_connections(file_path):
    """شمردن تعداد خطوط (کانکشن‌ها) در یک فایل"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return sum(1 for line in f if line.strip())
    except Exception as e:
        print(f"خطا در خواندن فایل {file_path}: {e}")
        return 0

def generate_readme():
    """تولید فایل README.md"""
    # جمع‌آوری اطلاعات فایل‌ها
    country_data = []
    for file_path in glob.glob(os.path.join(SUB_DIR, "*_only_sub.txt")):
        file_name = os.path.basename(file_path)
        country_code = file_name.split('_')[0].lower()
        if country_code in COUNTRY_NAMES:
            connections = count_connections(file_path)
            country_data.append({
                'code': country_code,
                'name': COUNTRY_NAMES[country_code],
                'connections': connections,
                'file': file_name
            })

    # جدا کردن آمریکا و مرتب‌سازی بقیه بر اساس تعداد کانکشن‌ها
    us_data = next((item for item in country_data if item['code'] == 'us'), None)
    other_countries = [item for item in country_data if item['code'] != 'us']
    other_countries.sort(key=lambda x: x['connections'], reverse=True)

    # ترکیب لیست: آمریکا اول، بقیه به ترتیب
    sorted_data = ([us_data] if us_data else []) + other_countries

    # زمان فعلی به وقت تهران
    tehran_tz = pytz.timezone('Asia/Tehran')
    update_time = datetime.now(tehran_tz).strftime("%Y-%m-%d %H:%M:%S")

    # تولید محتوای README
    readme_content = f"""# لینک‌های وی‌پی‌ان اختصاصی هر کشور

این صفحه شامل لینک‌های خام برای فایل‌های کانکشن وی‌پی‌ان است که هر کدام به یک کشور خاص اختصاص دارند. این فایل‌ها هر ۶ ساعت به‌صورت خودکار به‌روزرسانی می‌شوند.

**آخرین به‌روزرسانی**: {update_time} (به وقت تهران)

| نام کشور | تعداد کانکشن‌ها | لینک کانکشن |
|----------|------------------|-------------|
"""

    for country in sorted_data:
        readme_content += f"| {country['name']} | {country['connections']} | [{country['file']}]({BASE_URL}/{country['file']}) |\n"

    readme_content += """
## نکات
- **ایالات متحده** همیشه در ابتدای لیست قرار دارد.
- سایر کشورها بر اساس تعداد کانکشن‌ها (از بیشترین به کمترین) مرتب شده‌اند.
- هر فایل شامل کانکشن‌های اختصاصی برای کشور مربوطه است که با کلاینت‌هایی مثل v2ray یا Shadowrocket سازگارند.
- این لیست به‌صورت خودکار هر ۶ ساعت به‌روزرسانی می‌شود.
- اگر کشور جدیدی به منبع داده اضافه شود، به‌طور خودکار در این لیست ظاهر خواهد شد.

## منبع داده
- داده‌ها از [SSAggregator](https://raw.githubusercontent.com/mahdibland/SSAggregator/master/sub/sub_merge.txt) استخراج شده‌اند.
"""

    # ذخیره فایل VPN_LINKS.md
    with open("VPN_LINKS.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

if __name__ == "__main__":
    generate_readme()
