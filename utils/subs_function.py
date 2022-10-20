import requests
import urllib.parse
import yaml
import json
import base64
import socket
import geoip2.database


class subs_function:
    def convert_sub(url: str, output: str, convertor_host: "http://0.0.0.0:25500"):
        url = urllib.parse.quote(url, safe='')
        try:
            convert_url = f'{convertor_host}/sub?target={output}&url={url}&insert=false&emoji=true&list=true'
            result = requests.get(convert_url).text
            print(f"url to host: {convert_url}")
            if result == "No nodes were found!":
                return "Err: No nodes found"
            return result

        except Exception as e:
            print(e)
            return "Err: failed to parse sub"

    def is_line_valid(line, support_vless=False):
        if (line.startswith("ssr://") or line.startswith("ss://")
                or line.startswith("trojan://") or line.startswith("vmess://")):
            return line

        if(support_vless and line.startswith("vless://")):
            return line

        return ''

    def fix_proxies_name(corresponding_proxies: []):
        emoji = {
            'AD': '🇦🇩', 'AE': '🇦🇪', 'AF': '🇦🇫', 'AG': '🇦🇬',
            'AI': '🇦🇮', 'AL': '🇦🇱', 'AM': '🇦🇲', 'AO': '🇦🇴',
            'AQ': '🇦🇶', 'AR': '🇦🇷', 'AS': '🇦🇸', 'AT': '🇦🇹',
            'AU': '🇦🇺', 'AW': '🇦🇼', 'AX': '🇦🇽', 'AZ': '🇦🇿',
            'BA': '🇧🇦', 'BB': '🇧🇧', 'BD': '🇧🇩', 'BE': '🇧🇪',
            'BF': '🇧🇫', 'BG': '🇧🇬', 'BH': '🇧🇭', 'BI': '🇧🇮',
            'BJ': '🇧🇯', 'BL': '🇧🇱', 'BM': '🇧🇲', 'BN': '🇧🇳',
            'BO': '🇧🇴', 'BQ': '🇧🇶', 'BR': '🇧🇷', 'BS': '🇧🇸',
            'BT': '🇧🇹', 'BV': '🇧🇻', 'BW': '🇧🇼', 'BY': '🇧🇾',
            'BZ': '🇧🇿', 'CA': '🇨🇦', 'CC': '🇨🇨', 'CD': '🇨🇩',
            'CF': '🇨🇫', 'CG': '🇨🇬', 'CH': '🇨🇭', 'CI': '🇨🇮',
            'CK': '🇨🇰', 'CL': '🇨🇱', 'CM': '🇨🇲', 'CN': '🇨🇳',
            'CO': '🇨🇴', 'CR': '🇨🇷', 'CU': '🇨🇺', 'CV': '🇨🇻',
            'CW': '🇨🇼', 'CX': '🇨🇽', 'CY': '🇨🇾', 'CZ': '🇨🇿',
            'DE': '🇩🇪', 'DJ': '🇩🇯', 'DK': '🇩🇰', 'DM': '🇩🇲',
            'DO': '🇩🇴', 'DZ': '🇩🇿', 'EC': '🇪🇨', 'EE': '🇪🇪',
            'EG': '🇪🇬', 'EH': '🇪🇭', 'ER': '🇪🇷', 'ES': '🇪🇸',
            'ET': '🇪🇹', 'EU': '🇪🇺', 'FI': '🇫🇮', 'FJ': '🇫🇯',
            'FK': '🇫🇰', 'FM': '🇫🇲', 'FO': '🇫🇴', 'FR': '🇫🇷',
            'GA': '🇬🇦', 'GB': '🇬🇧', 'GD': '🇬🇩', 'GE': '🇬🇪',
            'GF': '🇬🇫', 'GG': '🇬🇬', 'GH': '🇬🇭', 'GI': '🇬🇮',
            'GL': '🇬🇱', 'GM': '🇬🇲', 'GN': '🇬🇳', 'GP': '🇬🇵',
            'GQ': '🇬🇶', 'GR': '🇬🇷', 'GS': '🇬🇸', 'GT': '🇬🇹',
            'GU': '🇬🇺', 'GW': '🇬🇼', 'GY': '🇬🇾', 'HK': '🇭🇰',
            'HM': '🇭🇲', 'HN': '🇭🇳', 'HR': '🇭🇷', 'HT': '🇭🇹',
            'HU': '🇭🇺', 'ID': '🇮🇩', 'IE': '🇮🇪', 'IL': '🇮🇱',
            'IM': '🇮🇲', 'IN': '🇮🇳', 'IO': '🇮🇴', 'IQ': '🇮🇶',
            'IR': '🇮🇷', 'IS': '🇮🇸', 'IT': '🇮🇹', 'JE': '🇯🇪',
            'JM': '🇯🇲', 'JO': '🇯🇴', 'JP': '🇯🇵', 'KE': '🇰🇪',
            'KG': '🇰🇬', 'KH': '🇰🇭', 'KI': '🇰🇮', 'KM': '🇰🇲',
            'KN': '🇰🇳', 'KP': '🇰🇵', 'KR': '🇰🇷', 'KW': '🇰🇼',
            'KY': '🇰🇾', 'KZ': '🇰🇿', 'LA': '🇱🇦', 'LB': '🇱🇧',
            'LC': '🇱🇨', 'LI': '🇱🇮', 'LK': '🇱🇰', 'LR': '🇱🇷',
            'LS': '🇱🇸', 'LT': '🇱🇹', 'LU': '🇱🇺', 'LV': '🇱🇻',
            'LY': '🇱🇾', 'MA': '🇲🇦', 'MC': '🇲🇨', 'MD': '🇲🇩',
            'ME': '🇲🇪', 'MF': '🇲🇫', 'MG': '🇲🇬', 'MH': '🇲🇭',
            'MK': '🇲🇰', 'ML': '🇲🇱', 'MM': '🇲🇲', 'MN': '🇲🇳',
            'MO': '🇲🇴', 'MP': '🇲🇵', 'MQ': '🇲🇶', 'MR': '🇲🇷',
            'MS': '🇲🇸', 'MT': '🇲🇹', 'MU': '🇲🇺', 'MV': '🇲🇻',
            'MW': '🇲🇼', 'MX': '🇲🇽', 'MY': '🇲🇾', 'MZ': '🇲🇿',
            'NA': '🇳🇦', 'NC': '🇳🇨', 'NE': '🇳🇪', 'NF': '🇳🇫',
            'NG': '🇳🇬', 'NI': '🇳🇮', 'NL': '🇳🇱', 'NO': '🇳🇴',
            'NP': '🇳🇵', 'NR': '🇳🇷', 'NU': '🇳🇺', 'NZ': '🇳🇿',
            'OM': '🇴🇲', 'PA': '🇵🇦', 'PE': '🇵🇪', 'PF': '🇵🇫',
            'PG': '🇵🇬', 'PH': '🇵🇭', 'PK': '🇵🇰', 'PL': '🇵🇱',
            'PM': '🇵🇲', 'PN': '🇵🇳', 'PR': '🇵🇷', 'PS': '🇵🇸',
            'PT': '🇵🇹', 'PW': '🇵🇼', 'PY': '🇵🇾', 'QA': '🇶🇦',
            'RE': '🇷🇪', 'RO': '🇷🇴', 'RS': '🇷🇸', 'RU': '🇷🇺',
            'RW': '🇷🇼', 'SA': '🇸🇦', 'SB': '🇸🇧', 'SC': '🇸🇨',
            'SD': '🇸🇩', 'SE': '🇸🇪', 'SG': '🇸🇬', 'SH': '🇸🇭',
            'SI': '🇸🇮', 'SJ': '🇸🇯', 'SK': '🇸🇰', 'SL': '🇸🇱',
            'SM': '🇸🇲', 'SN': '🇸🇳', 'SO': '🇸🇴', 'SR': '🇸🇷',
            'SS': '🇸🇸', 'ST': '🇸🇹', 'SV': '🇸🇻', 'SX': '🇸🇽',
            'SY': '🇸🇾', 'SZ': '🇸🇿', 'TC': '🇹🇨', 'TD': '🇹🇩',
            'TF': '🇹🇫', 'TG': '🇹🇬', 'TH': '🇹🇭', 'TJ': '🇹🇯',
            'TK': '🇹🇰', 'TL': '🇹🇱', 'TM': '🇹🇲', 'TN': '🇹🇳',
            'TO': '🇹🇴', 'TR': '🇹🇷', 'TT': '🇹🇹', 'TV': '🇹🇻',
            'TW': '🇹🇼', 'TZ': '🇹🇿', 'UA': '🇺🇦', 'UG': '🇺🇬',
            'UM': '🇺🇲', 'US': '🇺🇸', 'UY': '🇺🇾', 'UZ': '🇺🇿',
            'VA': '🇻🇦', 'VC': '🇻🇨', 'VE': '🇻🇪', 'VG': '🇻🇬',
            'VI': '🇻🇮', 'VN': '🇻🇳', 'VU': '🇻🇺', 'WF': '🇼🇫',
            'WS': '🇼🇸', 'XK': '🇽🇰', 'YE': '🇾🇪', 'YT': '🇾🇹',
            'ZA': '🇿🇦', 'ZM': '🇿🇲', 'ZW': '🇿🇼',
            'RELAY': '🏁',
            'NOWHERE': '🇦🇶',
        }

        for (index, c_proxy) in corresponding_proxies:
            proxy = c_proxy['c_clash']
            decoded_yaml = yaml.safe_load(proxy)
            # for safety i add both scenario
            if type(decoded_yaml) == list:
                proxy = decoded_yaml[0]
            else:
                proxy = decoded_yaml

            server = proxy['server']

            if server.replace('.', '').isdigit():
                ip = server
            else:
                try:
                    # https://cloud.tencent.com/developer/article/1569841
                    ip = socket.gethostbyname(server)
                except Exception:
                    ip = server

            with geoip2.database.Reader('./utils/Country.mmdb') as ip_reader:
                try:
                    response = ip_reader.country(ip)
                    country_code = response.country.iso_code
                except Exception:
                    ip = '0.0.0.0'
                    country_code = 'NOWHERE'

            if country_code == 'CLOUDFLARE':
                country_code = 'RELAY'
            elif country_code == 'PRIVATE':
                country_code = 'RELAY'

            if country_code in emoji:
                name_emoji = emoji[country_code]
            else:
                name_emoji = emoji['NOWHERE']

            # proxy_index = proxies_list.index(proxy)
            if len(corresponding_proxies) >= 999:
                proxy['name'] = f'{name_emoji}{country_code}-{ip}-{index:0>4d}'
            elif len(corresponding_proxies) <= 999 and len(corresponding_proxies) > 99:
                proxy['name'] = f'{name_emoji}{country_code}-{ip}-{index:0>3d}'
            elif len(corresponding_proxies) <= 99:
                proxy['name'] = f'{name_emoji}{country_code}-{ip}-{index:0>2d}'

            # corresponding_proxies[index]["c_clash"] = f"  - {proxy}"
            corresponding_proxies[index]["c_clash"] = f"{proxy}"

        return corresponding_proxies

    def fix_proxies_duplication(corresponding_proxies: []):
        print("\nBefore was " + str(corresponding_proxies.__len__()) + "\n")
        begin = 0
        raw_length = len(corresponding_proxies)
        length = len(corresponding_proxies)
        while begin < length:
            if (begin + 1) == 1:
                print(f'\n-----Restart-----\nStarting Quantity {length}')
            elif (begin + 1) % 100 == 0:
                print(
                    f'Current Benchmark {begin + 1}-----Current Quantity {length}')
            elif (begin + 1) == length and (begin + 1) % 100 != 0:
                repetition = raw_length - length
                print(
                    f'Current Benchmark {begin + 1}-----Current Quantity {length}\nNumber of Repetition {repetition}\n-----Deduplication Completed-----\n')
            proxy_compared = corresponding_proxies[begin]["c_clash"]

            begin_2 = begin + 1
            while begin_2 <= (length - 1):
                check = False
                if proxy_compared['server'] == corresponding_proxies[begin_2]["c_clash"]['server'] and proxy_compared['port'] == corresponding_proxies[begin_2]["c_clash"]['port']:
                    check = True
                    if 'net' in corresponding_proxies[begin_2]["c_clash"] and 'net' in proxy_compared:
                        if proxy_compared['net'] != corresponding_proxies[begin_2]["c_clash"]['net']:
                            check = False

                    if 'tls' in corresponding_proxies[begin_2]["c_clash"] and 'tls' in proxy_compared:
                        if proxy_compared['tls'] != corresponding_proxies[begin_2]["c_clash"]['tls']:
                            check = False

                    if 'id' in corresponding_proxies[begin_2]["c_clash"] and 'id' in proxy_compared:
                        if proxy_compared['id'] != corresponding_proxies[begin_2]["c_clash"]['id']:
                            check = False

                    if 'password' in corresponding_proxies[begin_2]["c_clash"] and 'password' in proxy_compared:
                        if proxy_compared['password'] != corresponding_proxies[begin_2]["c_clash"]['password']:
                            check = False

                    if 'cipher' in corresponding_proxies[begin_2]["c_clash"] and 'cipher' in proxy_compared:
                        if proxy_compared['cipher'] != corresponding_proxies[begin_2]["c_clash"]['cipher']:
                            check = False

                    if 'type' in corresponding_proxies[begin_2]["c_clash"] and 'type' in proxy_compared:
                        if proxy_compared['type'] != corresponding_proxies[begin_2]["c_clash"]['type']:
                            check = False

                    if check:
                        corresponding_proxies.pop(begin_2)
                        length -= 1

                begin_2 += 1
            begin += 1

        print("\nNow is " + str(corresponding_proxies.__len__()) + "\n")

        return corresponding_proxies
