#!/usr/bin/env python3


import os
import yaml
import json
import base64
import requests
from requests.adapters import HTTPAdapter
from urllib.parse import quote


class sub_convert(): # 将订阅链接中YAML，Base64等内容转换为 Url 链接内容
    
    def convert(content, input_type='url', output_type='url'): # convert Url to YAML or Base64

        if input_type == 'url':
            s = requests.Session()
            s.mount('http://', HTTPAdapter(max_retries=5))
            s.mount('https://', HTTPAdapter(max_retries=5))
            try:
                print('Downloading from:' + content)
                resp = s.get(content, timeout=5)
                sub_content = resp.content.decode('utf-8') 

                if 'proxies:' in sub_content: # 判断字符串是否在文本中，是，判断为YAML。https://cloud.tencent.com/developer/article/1699719
                    url_content = sub_convert.yaml_decode(sub_content)
                    #return self.url_content.replace('\r','') # 去除‘回车\r符’ https://blog.csdn.net/jerrygaoling/article/details/81051447
                elif '://'  in sub_content: # 同上，是，判断为 Url 链接内容。
                    url_content = sub_content.replace('\r','')
                else: # 判断 Base64.
                    try:
                        url_content = sub_convert.base64_decode(sub_content).replace('\r','')
                    except Exception: # 万能异常 https://blog.csdn.net/Candance_star/article/details/94135515
                        url_content = 'Url 订阅内容无法解析'
                        print('Url 订阅内容无法解析')
                
                if output_type == 'url' and url_content != 'Url 订阅内容无法解析':
                    return url_content
                elif output_type == 'Base64' and url_content != 'Url 订阅内容无法解析':
                    return sub_convert.base64_encode(url_content)
                elif output_type == 'YAML' and url_content != 'Url 订阅内容无法解析':
                    return sub_convert.yaml_encode(url_content)
                else:
                    print('Pleae define your output type.')
                    return 'Url 订阅内容无法解析'

            except Exception as err:
                print(err)
                return 'Url 解析错误'

        elif input_type == 'content':
            if 'proxies:' in content: # 判断字符串是否在文本中，是，判断为YAML。https://cloud.tencent.com/developer/article/1699719
                url_content = sub_convert.yaml_decode(content)
                #return self.url_content.replace('\r','') # 去除‘回车\r符’ https://blog.csdn.net/jerrygaoling/article/details/81051447
            elif '://'  in content: # 同上，是，判断为 Url 链接内容。
                url_content = content.replace('\r','')
            else: # 判断 Base64.
                try:
                    url_content = sub_convert.base64_decode(content).replace('\r','')
                except Exception: # 万能异常 https://blog.csdn.net/Candance_star/article/details/94135515
                    url_content = 'Url 订阅内容无法解析'
                    print('Url 订阅内容无法解析')
            if output_type == 'YAML':
                return sub_convert.yaml_encode(url_content)
            elif output_type == 'Base64':
                return sub_convert.base64_encode(url_content)
            elif output_type == 'url':
                url_content = content.replace('\r','')
                return url_content
            else:
                print('Please define your output type.')
                return 'Url 订阅内容无法解析'
                
        else:
            print('Please define your input type')


    def yaml_decode(url_content): # YAML 转换为 Url 链接内容
        
        """yaml_tmp = TemporaryFile('w+t', encoding='utf-8', errors='ignore') # 生成临时文件 https://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p19_make_temporary_files_and_directories.html
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
        base64_content = base64.b64decode(url_content.encode('utf-8')).decode('utf-8')
        return base64_content

    def yaml_encode(content): # 将 Url 内容转换为 YAML 
        url_list = []
        
        lines = content.split('\n')
        for line in lines:
            if 'vmess://' in line:
                vmess_raw_config_str = sub_convert.base64_decode(line.replace('vmess://', ''))
                vmess_raw_config = json.loads(vmess_raw_config_str)

                yaml_url = {}
                #yaml_config_str = ['name', 'server', 'port', 'type', 'uuid', 'alterId', 'cipher', 'tls', 'skip-cert-verify', 'network', 'ws-path', 'ws-headers']
                #vmess_config_str = ['ps', 'add', 'port', 'id', 'aid', 'scy', 'tls', 'net', 'host', 'path']
                # 生成 yaml 节点字典
                yaml_url.setdefault('name', vmess_raw_config['ps'])
                yaml_url.setdefault('server', vmess_raw_config['add'])
                yaml_url.setdefault('port', int(vmess_raw_config['port']))
                yaml_url.setdefault('type', 'vmess')
                yaml_url.setdefault('uuid', vmess_raw_config['id'])
                yaml_url.setdefault('alterId', int(vmess_raw_config['aid']))
                try :
                    yaml_url.setdefault('cipher', vmess_raw_config['scy'])
                except Exception:
                    yaml_url.setdefault('cipher', 'auto')
                if vmess_raw_config['tls'] == '':
                    yaml_url.setdefault('tls', False)
                else:
                    yaml_url.setdefault('tls', True)
                yaml_url.setdefault('skip-cert-vertify', False)
                yaml_url.setdefault('network', vmess_raw_config['net'])
                try:
                    yaml_url.setdefault('ws-path', vmess_raw_config['path'])
                except Exception:
                    yaml_url.setdefault('ws-path', '/')
                yaml_url.setdefault('ws-headers', {'Host': vmess_raw_config['add']})

                yaml_url_str = str(yaml_url)

                url_list.append(yaml_url_str)

            #if 'ss://' in line or 'ssr://' in line:
            #if 'trojan://' in line:

        yaml_content_dic = {'proxies': url_list}
        yaml_content_raw = yaml.dump(yaml_content_dic, default_flow_style=False, sort_keys=False, allow_unicode=True, width=500) # yaml.dump 显示中文方法 https://blog.csdn.net/weixin_41548578/article/details/90651464 yaml.dump 各种参数 https://blog.csdn.net/swinfans/article/details/88770119
        yaml_content = yaml_content_raw.replace('\'', '')

        # yaml.dump 返回格式不理想，正在参考 https://mrchi.cc/posts/444aa/ 改善。
        
        return yaml_content
    def base64_encode(content): # 将 Url 内容转换为 Base64
        base64_content = base64.b64encode(content.encode('utf-8')).decode('ascii')
        return base64_content
    

#Debug
""" with open('./list/00.txt', 'r', encoding='utf-8') as f: # 将 sub_list.json Url 内容读取为列表
    content = f.read()

a = sub_convert.convert(content,'YAML')
print(a) """