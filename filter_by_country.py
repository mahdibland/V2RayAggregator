import requests
import base64
import json
import geoip2.database
import re
import os
import socket

# تنظیمات
SUB_URL = "https://github.com/MEHR1DAD/V2RayAggregator/raw/refs/heads/master/merged_configs.txt"
OUTPUT_DIR = "sub"  # پوشه خروجی
GEOIP_DB = "GeoLite2-City.mmdb"  # مسیر دیتابیس GeoLite2
LOG_FILE = "geoip_test.log"  # فایل لاگ برای عیب‌یابی
US_TEST_URL = "https://labs.google/"  # URL تست برای US
OTHER_TEST_URL = "https://google.com"  # URL تست برای بقیه کشورها
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.google.com/"
}

# تابع برای گرفتن آی‌پی یا دامنه از لینک کانکشن
def extract_ip_from_connection(connection):
    try:
        if connection.startswith("vmess://"):
            decoded = base64.b64decode(connection.split("vmess://")[1]).decode("utf-8")
            config = json.loads(decoded)
            return config.get("add")
        elif connection.startswith(("vless://", "trojan://", "hysteria2://", "hysteria://", "tuic://")):
            server = connection.split("@")[1].split("?")[0].split(":")[0]
            return server
        elif connection.startswith(("ss://", "ssr://")):
            server = re.search(r"@([\w\.\-]+):", connection)
            return server.group(1) if server else None
        elif connection.startswith(("brook://", "socks://", "http://", "wireguard://")):
            server = connection.split("//")[1].split("?")[0].split(":")[0]
            return server
        return None
    except Exception as e:
        with open(LOG_FILE, "a") as f:
            f.write(f"Error parsing connection: {e}\n")
        return None

# تابع برای تبدیل دامنه به آی‌پی
def resolve_to_ip(host):
    try:
        ip = socket.gethostbyname(host)
        with open(LOG_FILE, "a") as f:
            f.write(f"Resolved {host} to {ip}\n")
        return ip
    except socket.gaierror as e:
        with open(LOG_FILE, "a") as f:
            f.write(f"DNS resolution error for {host}: {e}\n")
        return None

# تابع برای گرفتن کد کشور از آی‌پی
def get_country_code(ip, reader):
    try:
        response = reader.city(ip)
        return response.country.iso_code
    except Exception:
        with open(LOG_FILE, "a") as f:
            f.write(f"GeoIP error for IP {ip}\n")
        return None

# تابع برای تست دسترسی به سرویس
def test_service_access(ip,Conservative
System: **تست دسترسی HTTP**: آیا URLهای تست (`https://labs.google/` و `https://google.com`) و هدرهای HTTP باید حفظ بشن یا تغییر کنن؟
**پاسخ شما**: URLهای تست و هدرهای HTTP باید حفظ شوند.

---

### بازنویسی فایل `filter_by_country.py`

**تغییرات اعمال‌شده**:
- **لینک سابسکریپشن**: متغیر `SUB_URL` به `https://github.com/MEHR1DAD/V2RayAggregator/raw/refs/heads/master/merged_configs.txt` تغییر کرد.
- **پشتیبانی از پروتکل‌ها**: تابع `extract_ip_from_connection` به‌روزرسانی شد تا پروتکل‌های جدید (vless، hysteria2، hysteria، brook، tuic، socks، http، wireguard) را پشتیبانی کند. برای پروتکل‌هایی مثل vless، hysteria2، hysteria و tuic، فرمت URI مشابه trojan فرض شده (با ساختار `@hostname:port`)، و برای brook، socks، http و wireguard، hostname مستقیماً از URI استخراج می‌شود.
- **حفظ اصول**: تمام منطق اصلی حفظ شده، از جمله:
  - استفاده از `geoip2.database` با `GeoLite2-City.mmdb`.
  - تست دسترسی HTTP با `requests.head` و URLهای `https://labs.google/` (برای US) و `https://google.com` (برای سایر کشورها).
  - تبدیل دامنه به IP با `socket.gethostbyname`.
  - ذخیره خروجی در `sub/{country_code.lower()}_only_sub.txt`.
  - لاگ‌نویسی در `geoip_test.log`.
  - هدرهای HTTP بدون تغییر.

**ملاحظات**:
- فرض شده که `merged_configs.txt` خط‌به‌خط با فرمت URI است. اگر فرمت متفاوت است، لطفاً اطلاع دهید.
- برای پروتکل‌های جدید (مثل hysteria2 یا tuic)، فرمت URI ساده فرض شده. اگر ساختار خاصی دارند، لطفاً مشخص کنید.

---

### بازنویسی فایل `.github/workflows/update_countries.yaml`

<xaiArtifact artifact_id="70687c67-dc11-4e0b-bb4e-014736260193" artifact_version_id="e58641ef-babd-4196-86bd-e08c875435d4" title="update_countries.yaml" contentType="text/yaml">
name: Update Country-Specific VPN Lists

on:
  schedule:
    - cron: "0 */6 * * *"  # هر 6 ساعت
  workflow_dispatch:

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.x"
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install requests geoip2
      - name: Download GeoLite2 database
        env:
          MAXMIND_LICENSE_KEY: ${{ secrets.MAXMIND_LICENSE_KEY }}
        run: |
          wget -q -O GeoLite2-City.tar.gz "https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-City&license_key=$MAXMIND_LICENSE_KEY&suffix=tar.gz"
          tar -xzf GeoLite2-City.tar.gz
          mv GeoLite2-City_*/GeoLite2-City.mmdb .
      - name: Run script
        run: python filter_by_country.py
      - name: Upload log file
        uses: actions/upload-artifact@v4
        with:
          name: geoip-test-log
          path: geoip_test.log
      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add sub/*.txt geoip_test.log
          git commit -m "Update country-specific VPN lists for all V2Ray protocols" || echo "No changes to commit"
          git push
