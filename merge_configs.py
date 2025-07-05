import requests

# List of URLs containing proxy configurations
urls = [
    "https://raw.githubusercontent.com/barry-far/V2ray-Config/refs/heads/main/All_Configs_Sub.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/all_configs.txt",
    "https://raw.githubusercontent.com/mahdibland/SSAggregator/master/sub/sub_merge.txt",
    "https://raw.githubusercontent.com/mrvcoder/V2rayCollector/refs/heads/main/mixed_iran.txt",
    "https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/v2ray/all_sub.txt"
]

def fetch_configs():
    all_configs = set()
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise an error for bad status codes
            # Split the content by lines and add non-empty lines to the set
            configs = response.text.splitlines()
            for config in configs:
                config = config.strip()
                if config:  # Ignore empty lines
                    all_configs.add(config)
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
    return all_configs

def save_configs(configs):
    with open("merged_configs.txt", "w", encoding="utf-8") as f:
        for config in sorted(configs):  # Sort for consistency
            f.write(config + "\n")

if __name__ == "__main__":
    configs = fetch_configs()
    save_configs(configs)
    print(f"Merged {len(configs)} unique configurations into merged_configs.txt")
