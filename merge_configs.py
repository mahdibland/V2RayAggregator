import httpx  # کتابخانه جدید برای درخواست‌های همزمان و غیرهمزمان
import asyncio
import json
import os

# --- Constants ---
SOURCES_FILE = "active_sources.json"
MERGED_CONFIGS_FILE = "merged_configs.txt"
REQUEST_TIMEOUT = 10
ALLOWED_PROTOCOLS = {
    "vmess://", "vless://", "ss://", "ssr://", "trojan://",
    "hysteria://", "hysteria2://", "brook://", "tuic://",
    "socks://", "wireguard://"
}

def load_urls():
    """Loads subscription URLs from the json file."""
    if not os.path.exists(SOURCES_FILE):
        print(f"Error: Source file '{SOURCES_FILE}' not found.")
        return []
    try:
        with open(SOURCES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, TypeError):
        print(f"Error: Could not decode JSON from '{SOURCES_FILE}'.")
        return []

async def fetch_one(client, url):
    """Fetches content from a single URL asynchronously."""
    try:
        # ارسال درخواست غیرهمزمان
        response = await client.get(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        return response.text.splitlines()
    except (httpx.RequestError, httpx.HTTPStatusError) as e:
        print(f"Error fetching {url}: {e}")
        return []

async def fetch_all_configs(urls):
    """Gathers all configs from a list of URLs concurrently."""
    all_configs = set()
    # ایجاد یک کلاینت برای ارسال تمام درخواست‌ها
    async with httpx.AsyncClient() as client:
        # ساخت لیستی از تمام وظایف (Task) دانلود
        tasks = [fetch_one(client, url) for url in urls]
        # اجرای تمام وظایف به صورت همزمان
        results = await asyncio.gather(*tasks, return_exceptions=True)

    for result in results:
        if isinstance(result, list):
            for config in result:
                config = config.strip()
                if config and any(config.startswith(protocol) for protocol in ALLOWED_PROTOCOLS):
                    all_configs.add(config)
    return all_configs

def save_configs(configs):
    """Saves the merged configs to a file."""
    with open(MERGED_CONFIGS_FILE, "w", encoding="utf-8") as f:
        for config in sorted(configs):
            f.write(config + "\n")

async def main():
    """The main async function."""
    urls = load_urls()
    if urls:
        print(f"Loaded {len(urls)} sources from '{SOURCES_FILE}'")
        print("Fetching all sources concurrently...")
        configs = await fetch_all_configs(urls)
        print(f"Fetched {len(configs)} unique configurations.")
        save_configs(configs)
        print(f"Merged configurations into {MERGED_CONFIGS_FILE}")
    else:
        print("No sources to process. Exiting.")

if __name__ == "__main__":
    # اجرای تابع اصلی به صورت غیرهمزمان
    asyncio.run(main())
