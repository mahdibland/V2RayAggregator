import requests

# List of URLs containing proxy configurations
urls = [
    "https://raw.githubusercontent.com/barry-far/V2ray-Config/refs/heads/main/All_Configs_Sub.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/all_configs.txt",
    "https://raw.githubusercontent.com/mahdibland/SSAggregator/master/sub/sub_merge.txt",
    "https://raw.githubusercontent.com/mrvcoder/V2rayCollector/refs/heads/main/mixed_iran.txt",
    "https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/v2ray/all_sub.txt",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/xray/normal/reality",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/xray/normal/reality_domain",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/xray/normal/reality_ipv4",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/xray/normal/ss",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/xray/normal/ss_domain",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/xray/normal/ss_ipv4",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/xray/normal/vless",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/xray/normal/vless_ipv4",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/xray/normal/vmess",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/xray/normal/vmess_domain",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/subscriptions/xray/normal/reality",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/subscriptions/xray/normal/reality_domain",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/subscriptions/xray/normal/reality_ipv4",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/subscriptions/xray/normal/ss",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/subscriptions/xray/normal/ss_domain",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/subscriptions/xray/normal/ss_ipv4",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/subscriptions/xray/normal/vless",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/subscriptions/xray/normal/vless_domain",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/subscriptions/xray/normal/vmess",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/subscriptions/xray/normal/vmess_domain",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/location/normal/US",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/subscriptions/location/normal/US",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/location/normal/DE",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/subscriptions/location/normal/DE",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/location/normal/SE",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/subscriptions/location/normal/SE",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/location/normal/NL",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/subscriptions/location/normal/NL",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/location/normal/FR",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/subscriptions/location/normal/FR",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/location/normal/AT",
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/subscriptions/location/normal/AT"
]

# List of allowed protocols
ALLOWED_PROTOCOLS = {
    "vmess://", "vless://", "ss://", "ssr://", "trojan://", 
    "hysteria://", "hysteria2://", "brook://", "tuic://", 
    "socks://", "http://", "wireguard://"
}

def fetch_configs():
    all_configs = set()
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise an error for bad status codes
            # Split the content by lines and add non-empty, valid protocol configs to the set
            configs = response.text.splitlines()
            for config in configs:
                config = config.strip()
                # Check if the config starts with an allowed protocol
                if config and any(config.startswith(protocol) for protocol in ALLOWED_PROTOCOLS):
                    all_configs.add(config)
                elif config:  # Log non-matching configs for debugging
                    print(f"Skipped non-matching config from {url}: {config}")
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
    return all_configs

def save_configs(configs):
    with open("merged_configs.txt", "w", encoding="utf-8") as f:
        for config in sorted(configs):  # Sort for consistency
            f.write(config + "\n")

if __name__ == "__main__":
    configs = fetch_configs()
    print(f"Fetched {len(configs)} unique configurations with allowed protocols")
    save_configs(configs)
    print(f"Merged {len(configs)} unique configurations into merged_configs.txt")
