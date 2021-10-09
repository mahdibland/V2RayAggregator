#!/usr/bin/env python3


import yaml
import json
import base64
import requests
from requests.adapters import HTTPAdapter
from urllib.parse import quote


class sub_convert():# 将订阅链接中YAML，Base64等内容转换为 Url 链接内容
    
    def url_decode(sub_url):# 读取订阅内容，并转化为 Url 链接内容

        s = requests.Session()
        s.mount('http://', HTTPAdapter(max_retries=3))
        s.mount('https://', HTTPAdapter(max_retries=3))
        try:
            print('Downloading from:' + sub_url)
            resp = s.get(sub_url, timeout=5)
            sub_content = resp.content.decode('utf-8') 

            if 'proxies:' in sub_content: # 判断字符串是否在文本中，是，判断为YAML。https://cloud.tencent.com/developer/article/1699719
                url_content = sub_convert.yaml_decode(sub_content)
                return url_content
                #return self.url_content.replace('\r','') # 去除‘回车\r符’ https://blog.csdn.net/jerrygaoling/article/details/81051447
            elif '://'  in sub_content: # 同上，是，判断为 Url 链接内容。
                url_content = sub_content
                return url_content.replace('\r','')
            else: # 判断 Base64.
                try:
                    url_content = sub_convert.base64_decode(sub_content)
                    return url_content.replace('\r','')
                except Exception: # 万能异常 https://blog.csdn.net/Candance_star/article/details/94135515
                    print('Url 订阅内容无法解析')
                    return 'Url 订阅内容无法解析'

        except Exception as err:
            print(err)
            return 'Url 解析错误'

    def yaml_decode(url_content): # YAML 转换为 Url 链接内容
        
        """yaml_tmp = TemporaryFile('w+t', encoding='utf-8', errors='ignore') # 生成临时文件https://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p19_make_temporary_files_and_directories.html
        yaml_tmp.write(url_content)
        yaml_data = yaml_tmp.read() """
        raw_yaml_content = yaml.safe_load(url_content) # 将 YAML 内容生成 Python 字典
        proxies_list = raw_yaml_content['proxies'] # YAML 节点列表

        protocol_list = []
        for index in range(len(proxies_list)):
            proxy = proxies_list[index]
            if proxy['type'] == 'vmess': # Vmess 节点提取 , 由 Vmess 所有参数 dump JSON 后 base64 得来。
                raw_config_value = []
                raw_config_str = ['v~', 'name', 'server', 'port', 'uuid', 'alterId', 'cipher', 'network', 'type~', 'server', 'ws-path', 'tls~', 'sni~']
                
                # 生成 Vmess 参数值列表
                raw_config_value.append(2)
                for num in range(2,9):
                    raw_config_value.append(proxies_list[index][raw_config_str[num - 1]])
                raw_config_value.append('')
                for num in range(10,12):
                    raw_config_value.append(proxies_list[index][raw_config_str[num - 1]])
                raw_config_value.append('')
                raw_config_value.append(None)
                
                config_str = ['v', 'ps', 'add', 'port', 'id', 'aid', 'scy', 'net', 'type', 'host', 'path', 'tls', 'sni']
                config_value_dic = {}
                for num in range(1, len(config_str) + 1):
                    config_value_dic.setdefault(config_str[num - 1],raw_config_value[num - 1])
                vmess_raw_proxy = json.dumps(config_value_dic, sort_keys=False, indent=2, ensure_ascii=False)
                vmess_proxy = str('vmess://' + sub_convert.base64_encode(vmess_raw_proxy) + '\n')
                protocol_list.append(vmess_proxy)

            if proxy['type'] == 'ss' or proxy['type'] == 'ssr': # SS 节点提取 ， 由 ss_base64_decoded 部分(参数：'cipher', 'password', 'server', 'port') Base64 编码后 加 # 加注释(URL_encode) 
                ss_base64_decoded = str(proxy['cipher']) + ':' + str(proxy['password']) + '@' + str(proxy['server']) + ':' + str(proxy['port'])
                ss_base64 = sub_convert.base64_encode(ss_base64_decoded)
                ss_proxy = str('ss://' + ss_base64 + '#' + str(quote(proxy['name'])) + '\n')
                protocol_list.append(ss_proxy)

            if proxy['type'] == 'trojan': # Trojan 节点提取 ， 最简单 ， 由 trojan_proxy 中参数再加上 # 加注释(URL_encode)
                trojan_proxy = str('trojan://' + str(proxy['password']) + '@' + str(proxy['server']) + ':' + str(proxy['port']) + '#' + str(quote(proxy['name'])) + '\n')
                protocol_list.append(trojan_proxy)


        yaml_content = ''.join(protocol_list)
        return yaml_content
    def base64_decode(url_content): # Base64 转换为 Url 链接内容
        base64_content = base64.b64decode(url_content.encode('utf-8')).decode('ascii')
        return base64_content

    def yaml_encode(url_content): # 将 Url 内容转换为 YAML 
        yaml_content = url_content
        return yaml_content
    def base64_encode(url_content): # 将 Url 内容转换为 Base64
        base64_content = base64.b64encode(url_content.encode('utf-8')).decode('ascii')
        return base64_content
    def convert(url_content,output_type): # convert Url to YAML or Base64

        if output_type == 'YAML':
            return sub_convert.yaml_encode(url_content)
        elif output_type == 'Base64':
            return sub_convert.base64_encode(url_content)
 
""" 
Debug
with open('test.yml', 'r', encoding='utf-8') as f: # 将 sub_list.json Url 内容读取为列表
    yaml_content = f.read()

a = sub_convert.yaml_decode(yaml_content)
print(a)
"""