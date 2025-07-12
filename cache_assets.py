import os
import requests

# دیکشنری لوگوها: نام فایل برای ذخیره و URL برای دانلود
ASSETS = {
    "hiddify_logo.png": "https://play-lh.googleusercontent.com/Dm_6ugf7Wwib_A3AFFdtkktufYGGOamhb072Ii46zYyb__qZHSocnJGErEUWxp7UWaGG",
    "v2rayng_logo.png": "https://raw.githubusercontent.com/2dust/v2rayNG/master/app/src/main/ic_launcher-playstore.png",
    "nekoray_logo.png": "https://raw.githubusercontent.com/MatsuriDayo/nekoray/master/res/logo/nekoray.png"
}

# مسیری که تصاویر در آن ذخیره می‌شوند
ASSETS_DIR = ".github/assets"

def download_assets():
    """تصاویر را در صورت عدم وجود، دانلود و ذخیره می‌کند"""
    print(f"Checking asset directory: {ASSETS_DIR}")
    os.makedirs(ASSETS_DIR, exist_ok=True)

    for filename, url in ASSETS.items():
        output_path = os.path.join(ASSETS_DIR, filename)
        
        if os.path.exists(output_path):
            print(f"✅ Asset '{filename}' already exists. Skipping.")
            continue

        print(f"⬇️ Downloading '{filename}'...")
        try:
            response = requests.get(url, timeout=15, stream=True)
            response.raise_for_status()
            
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"   -> Successfully saved to {output_path}")

        except requests.RequestException as e:
            print(f"   -> ❌ Failed to download {filename}: {e}")

if __name__ == "__main__":
    download_assets()
    print("\nAsset download process complete.")
    print("Please run 'git add .github/assets' and commit the new images to your repository.")

