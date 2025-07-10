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
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/subscriptions/location/normal/AT",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Albania.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Argentina.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Armenia.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Au.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Australia.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Azerbaijan.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Bahrain.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Belgium.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Bolivia.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Bosnia_And_Herzegovina.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Brazil.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Bulgaria.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Canada.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Chile.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/China.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Colombia.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Costa_Rica.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Cr.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Croatia.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Cyprus.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Czechia.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/De.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Denmark.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Ecuador.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Estonia.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Finland.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Gibraltar.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Greece.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Hong_Kong.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Hungary.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Iceland.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/India.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Indonesia.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Iran.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Ireland.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Israel.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Italy.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Japan.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Jordan.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Kazakhstan.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Latvia.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Lithuania.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Luxembourg.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Malaysia.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Malta.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Mauritius.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Mexico.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Moldova.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/New_Zealand.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/North_Macedonia.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Norway.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Paraguay.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Poland.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Portugal.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Romania.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Russia.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Saudi_Arabia.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Serbia.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Seychelles.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Singapore.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Slovakia.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Slovenia.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/South_Africa.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/South_Korea.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Spain.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Switzerland.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Taiwan.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Thailand.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/The_Netherlands.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/T%C3%BCrkiye.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Ukraine.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/United_Arab_Emirates.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/United_Kingdom.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/United_States.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Unknown.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Us.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Vietnam.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Vn.txt",
    "https://github.com/Epodonios/v2ray-configs/raw/refs/heads/main/All_Configs_Sub.txt"
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
