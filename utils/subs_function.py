import requests
import urllib.parse


class subs_function:
    def convert_sub(url: str, output: str, convertor_host: "http://0.0.0.0:25500"):
        url = urllib.parse.quote(url, safe='')
        try:
            result = requests.get(
                f'{convertor_host}/sub?target={output}&url={url}&insert=false&emoji=true&list=true').text

            if result == "No nodes were found!":
                return "Err: No nodes found"

            return result

        except Exception as e:
            print(e)
            return "Err: failed to parse sub"

    def is_line_valid(line, support_vless=False):
        if (line.__contains__("ssr://") or line.__contains__("ss://")
                or line.__contains__("trojan://") or line.__contains__("vmess://")):
            return line

        if(support_vless and line.__contains__("vless://")):
            return line

        return ''
