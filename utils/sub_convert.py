#!/usr/bin/env python3

import re
import yaml
import json
import base64
import requests
import urllib.parse
from requests.adapters import HTTPAdapter


class sub_convert(): # 将订阅链接中YAML，Base64等内容转换为 Url 链接内容

    # {'input_type': ['url', 'content'],'output_type': ['url', 'YAML', 'Base64']}

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
                elif '://'  in sub_content and '</html>' not in sub_content: # 同上，是，判断为 Url 链接内容。
                    url_content = sub_convert.url_format(sub_content)
                elif '</html>' in sub_content:
                    url_content = 'Url 解析错误'
                else: # 判断 Base64.
                    try:
                        url_content = sub_convert.base64_decode(sub_content)
                    except Exception: # 万能异常 https://blog.csdn.net/Candance_star/article/details/94135515
                        url_content = 'Url 订阅内容无法解析'
                        print('Url 订阅内容无法解析')

                if output_type == 'url' and url_content != 'Url 订阅内容无法解析':
                    return url_content
                elif output_type == 'Base64' and url_content != 'Url 订阅内容无法解析':
                    return sub_convert.base64_encode(url_content)
                elif output_type == 'YAML' and url_content != 'Url 订阅内容无法解析':
                    return sub_convert.yaml_encode(url_content)
                elif output_type == '':
                    print('Pleae define your output type.')
                    return 'Url 订阅内容无法解析'

            except Exception as err:
                print(err)
                return 'Url 解析错误'

        elif input_type == 'content':
            if 'proxies:' in content: # 判断字符串是否在文本中，是，判断为YAML。https://cloud.tencent.com/developer/article/1699719
                url_content = sub_convert.yaml_decode(content)
                #return self.url_content.replace('\r','') # 去除‘回车\r符’ https://blog.csdn.net/jerrygaoling/article/details/81051447
            elif '://'  in content and '</html>' not in content: # 同上，是，判断为 Url 链接内容。
                url_content = sub_convert.url_format(content)
            else: # 判断 Base64.
                try:
                    url_content = sub_convert.base64_decode(content)
                except Exception: # 万能异常 https://blog.csdn.net/Candance_star/article/details/94135515
                    url_content = 'Url 订阅内容无法解析'
                    print('Url 订阅内容无法解析')
            if output_type == 'YAML':
                return sub_convert.yaml_encode(url_content)
            elif output_type == 'Base64':
                return sub_convert.base64_encode(url_content)
            elif output_type == 'url':
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
        raw_yaml_content = yaml.safe_load(url_content.replace('?', '\question')) # 将 YAML 内容生成 Python 字典
        proxies_list = raw_yaml_content['proxies'] # YAML 节点列表

        protocol_url = []
        for index in range(len(proxies_list)): # 不同节点订阅链接内容 https://github.com/hoochanlon/fq-book/blob/master/docs/append/srvurl.md
            proxy = proxies_list[index]

            if proxy['type'] == 'vmess': # Vmess 节点提取 , 由 Vmess 所有参数 dump JSON 后 base64 得来。

                yaml_default_config = {
                    'name': 'Vmess Node', 'server': '0.0.0.0', 'port': 0, 'uuid': '', 'alterId': 0,
                    'cipher': 'auto', 'network': 'tcp', 'ws-headers': {'Host': proxy['server']},
                    'ws-path': '/', 'tls': ''
                }

                config_value_dic = {}
                yaml_default_config.update(proxy)
                proxy_config = yaml_default_config

                # 转换过程中出现的不标准配置格式转换
                if 'HOST' in proxy_config['ws-headers'].keys():
                    proxy_config['ws-headers']['Host'] = proxy_config['ws-headers'].pop("HOST")

                raw_config_value = []
                raw_config_str = ['v~', 'name', 'server', 'port', 'uuid', 'alterId', 'cipher', 'network', 'type~', 'ws-headers', 'ws-path', 'tls', 'sni~']

                # 生成 Vmess 参数值列表
                raw_config_value.append(2)
                for num in range(2,8):
                    raw_config_value.append(proxy_config[raw_config_str[num - 1]])
                raw_config_value.append('')
                raw_config_value.append('')
                raw_config_value.append(proxy_config['ws-headers']['Host']) # 字典模糊搜索 https://www.coder.work/article/2428703
                raw_config_value.append(proxy_config['ws-path'])
                raw_config_value.append(proxy_config['tls'])
                raw_config_value.append(None)
                
                config_str = ['v', 'ps', 'add', 'port', 'id', 'aid', 'scy', 'net', 'type', 'host', 'path', 'tls', 'sni']
                for num in range(1, 13):
                    config_value_dic.setdefault(config_str[num - 1], raw_config_value[num - 1])

                vmess_raw_proxy = json.dumps(config_value_dic, sort_keys=False, indent=2, ensure_ascii=False)
                vmess_proxy = str('vmess://' + sub_convert.base64_encode(vmess_raw_proxy) + '\n')
                protocol_url.append(vmess_proxy)

            elif proxy['type'] == 'ss': # SS 节点提取 ， 由 ss_base64_decoded 部分(参数：'cipher', 'password', 'server', 'port') Base64 编码后 加 # 加注释(URL_encode) 
                ss_base64_decoded = str(proxy['cipher']) + ':' + str(proxy['password']) + '@' + str(proxy['server']) + ':' + str(proxy['port'])
                ss_base64 = sub_convert.base64_encode(ss_base64_decoded)
                ss_proxy = str('ss://' + ss_base64 + '#' + str(urllib.parse.quote(proxy['name'])) + '\n')
                protocol_url.append(ss_proxy)

            elif proxy['type'] == 'trojan': # Trojan 节点提取 ， 最简单 ， 由 trojan_proxy 中参数再加上 # 加注释(URL_encode)
                trojan_proxy = str('trojan://' + str(proxy['password']) + '@' + str(proxy['server']) + ':' + str(proxy['port']) + '#' + str(urllib.parse.quote(proxy['name'])) + '\n')
                protocol_url.append(trojan_proxy)
            
            #elif proxy['type'] == 'ssr':
                #ssr_base64_decoded = str(proxy['server']) + ':' + str(proxy['port']) + ':' + str(proxy['protocol']) 
                #ssr_base64_decoded = ssr_base64_decoded + ':' + str(proxy['cipher']) + ':' + str(proxy['obfs']) + ':' + str(sub_convert.base64_encode(proxy['password'])) + '/?'
                #protocol_url.append(vmessr_proxy) 

        yaml_content = ''.join(protocol_url)
        yaml_content = yaml_content.replace('\question', '?')
        return yaml_content
    def base64_decode(url_content): # Base64 转换为 Url 链接内容
        if '-' in url_content:
            url_content = url_content.replace('-', '+')
        elif '_' in url_content:
            url_content = url_content.replace('_', '/')
        #print(len(url_content))
        missing_padding = len(url_content) % 4
        if missing_padding != 0:
            url_content += '='*(4 - missing_padding) # 不是4的倍数后加= https://www.cnblogs.com/wswang/p/7717997.html
        """ elif(len(url_content)%3 == 1):
            url_content += '=='
        elif(len(url_content)%3 == 2): 
            url_content += '=' """
        #print(url_content)
        #print(len(url_content))
        try:
            base64_content = base64.b64decode(url_content.encode('utf-8')).decode('utf-8','ignore') # https://www.codenong.com/42339876/
            return base64_content
        except UnicodeDecodeError:
            base64_content = base64.b64decode(url_content)
            return base64_content

    def yaml_encode(content): # 将 Url 内容转换为 YAML URLencode&decode https://blog.csdn.net/wf592523813/article/details/79141463
        url_content =  sub_convert.url_format(content)
        
        url_list = []
        
        lines = url_content.split('\n')
        for line in lines:
            if 'vmess://' in line:
                try:
                    vmess_json_config = json.loads(sub_convert.base64_decode(line.replace('vmess://', '')))
                    vmess_default_config = {
                        'v': 2, 'ps': 'Vmess Node', 'add': '0.0.0.0', 'port': 0, 'id': '',
                        'aid': 0,'scy': 'auto', 'net': '', 'type': '', 'host': vmess_json_config['add'], 'path': '/', 'tls': ''
                    }
                    vmess_default_config.update(vmess_json_config)
                    vmess_config = vmess_default_config

                    yaml_url = {}
                    #yaml_config_str = ['name', 'server', 'port', 'type', 'uuid', 'alterId', 'cipher', 'tls', 'skip-cert-verify', 'network', 'ws-path', 'ws-headers']
                    #vmess_config_str = ['ps', 'add', 'port', 'id', 'aid', 'scy', 'tls', 'net', 'host', 'path']
                    # 生成 yaml 节点字典
                    yaml_url.setdefault('name', urllib.parse.unquote(vmess_config['ps']))
                    yaml_url.setdefault('server', vmess_config['add'])
                    yaml_url.setdefault('port', int(vmess_config['port']))
                    yaml_url.setdefault('type', 'vmess')
                    yaml_url.setdefault('uuid', vmess_config['id'])
                    yaml_url.setdefault('alterId', int(vmess_config['aid']))
                    yaml_url.setdefault('cipher', vmess_config['scy'])
                    if vmess_config['tls'] == '':
                        yaml_url.setdefault('tls', False)
                    else:
                        yaml_url.setdefault('tls', True)
                    yaml_url.setdefault('skip-cert-vertify', False)
                    yaml_url.setdefault('network', vmess_config['net'])
                    yaml_url.setdefault('ws-path', vmess_config['path'])
                    if vmess_config['host'] == '':
                        yaml_url.setdefault('ws-headers', {'Host': vmess_config['add']})
                    else:
                        yaml_url.setdefault('ws-headers', {'Host': vmess_config['host']})

                    if '|' in yaml_url['name'] or '[' in yaml_url['name'] or '[' in yaml_url['name']:
                        yaml_url['name'] = '"' + yaml_url['name'] + '"'
                    yaml_url_str = str(yaml_url)

                    url_list.append(yaml_url_str)
                except Exception as err:
                    print(f'yaml_encode 解析 vmess 节点发生错误：{err}')
                    pass

            if 'ss://' in line and '#' in line and 'trojan://' not in line:
                try:
                    yaml_url = {}

                    ss_content =  line.replace('ss://', '')
                    part_list = re.split('#', ss_content, maxsplit=1) # https://www.runoob.com/python/att-string-split.html
                    yaml_url.setdefault('name', urllib.parse.unquote(part_list[1]))
                    if '@' in part_list[0]:
                        mix_part = re.split('@', part_list[0], maxsplit=1)
                        method_part = sub_convert.base64_decode(mix_part[0])
                        server_part = f'{method_part}@{mix_part[1]}'
                    else:
                        server_part = sub_convert.base64_decode(part_list[0])

                    server_part_list = re.split(':|@', server_part) # 使用多个分隔符 https://blog.csdn.net/shidamowang/article/details/80254476 https://zhuanlan.zhihu.com/p/92287240
                    #print(server_part_list)
                    yaml_url.setdefault('server', server_part_list[2])
                    yaml_url.setdefault('port', server_part_list[3])
                    yaml_url.setdefault('type', 'ss')
                    yaml_url.setdefault('cipher', server_part_list[0])
                    yaml_url.setdefault('password', server_part_list[1])

                    if '|' in yaml_url['name'] or '[' in yaml_url['name'] or '[' in yaml_url['name']:
                        yaml_url['name'] = '"' + yaml_url['name'] + '"'
                    yaml_url_str = str(yaml_url)

                    url_list.append(yaml_url_str)
                except Exception as err:
                    print(f'yaml_encode 解析 ss 节点发生错误：{err}')
                    pass
            
            if 'ssr://' in line:
                try:
                    yaml_url = {}

                    ssr_content = sub_convert.base64_decode(line.replace('ssr://', ''))
                
                    part_list = re.split('/\?', ssr_content)
                    if '&' in part_list[1]:
                        ssr_part = re.split('&', part_list[1]) # 将 SSR content /？后部分参数分割
                        for item in ssr_part:
                            if 'remarks=' in item:
                                remarks_part = item.replace('remarks=', '')
                        try:
                            remarks = sub_convert.base64_decode(remarks_part)
                        except Exception:
                            remarks = 'ssr'
                    else:
                        remarks_part = part_list[1].replace('remarks=', '')
                        try:
                            remarks = sub_convert.base64_decode(remarks_part)
                        except Exception:
                            remarks = 'ssr'
                            print(f'SSR format error, content:{remarks_part}')
                    yaml_url.setdefault('name', urllib.parse.unquote(remarks))

                    server_part_list = re.split(':', part_list[0])
                    yaml_url.setdefault('server', server_part_list[0])
                    yaml_url.setdefault('port', server_part_list[1])
                    yaml_url.setdefault('type', 'ssr')
                    yaml_url.setdefault('cipher', server_part_list[3])
                    yaml_url.setdefault('password', server_part_list[5])

                    if '|' in yaml_url['name'] or '[' in yaml_url['name'] or '[' in yaml_url['name']:
                        yaml_url['name'] = '"' + yaml_url['name'] + '"'
                    yaml_url_str = str(yaml_url)

                    url_list.append(yaml_url_str)
                except Exception as err:
                    print(f'yaml_encode 解析 ssr 节点发生错误：{err}')
                    pass

            if 'trojan://' in line:
                try:
                    yaml_url = {}

                    url_content = line.replace('trojan://', '')
                    part_list = re.split('#', url_content, maxsplit=1) # https://www.runoob.com/python/att-string-split.html
                    yaml_url.setdefault('name', urllib.parse.unquote(part_list[1]))

                    server_part = part_list[0].replace('trojan://', '')
                    server_part_list = re.split(':|@|\?sni=', server_part) # 使用多个分隔符 https://blog.csdn.net/shidamowang/article/details/80254476 https://zhuanlan.zhihu.com/p/92287240
                    yaml_url.setdefault('server', server_part_list[1])
                    yaml_url.setdefault('port', server_part_list[2])
                    yaml_url.setdefault('type', 'trojan')
                    yaml_url.setdefault('password', server_part_list[0])
                    if '?sni=' in server_part:
                        yaml_url.setdefault('sni', server_part_list[3])
                    yaml_url.setdefault('skip-cert-verify', 'false')

                    if '|' in yaml_url['name'] or '[' in yaml_url['name'] or '[' in yaml_url['name']:
                        yaml_url['name'] = '"' + yaml_url['name'] + '"'
                    yaml_url_str = str(yaml_url)

                    url_list.append(yaml_url_str)
                except Exception as err:
                    print(f'yaml_encode 解析 trojan 节点发生错误：{err}')
                    pass

        yaml_content_dic = {'proxies': url_list}
        yaml_content_raw = yaml.dump(yaml_content_dic, default_flow_style=False, sort_keys=False, allow_unicode=True, width=750, indent=2) # yaml.dump 显示中文方法 https://blog.csdn.net/weixin_41548578/article/details/90651464 yaml.dump 各种参数 https://blog.csdn.net/swinfans/article/details/88770119
        yaml_content = yaml_content_raw.replace('\'', '')
        yaml_content = yaml_content.replace('False', 'false')
        # yaml.dump 返回格式不理想，正在参考 https://mrchi.cc/posts/444aa/ 改善。
        return yaml_content
    def base64_encode(content): # 将 Url 内容转换为 Base64
        base64_content = base64.b64encode(sub_convert.url_format(content).encode('utf-8')).decode('ascii')
        return base64_content

    def proxies_filter(urls, dup_rm_enabled=True, format_name_enabled=True): # 对节点进行区域的筛选和重命名，区域判断(Clash YAML)：https://blog.csdn.net/CSDN_duomaomao/article/details/89712826 (ip-api)
        if 'proxies:' in urls:
            yaml_content = urls
        else:
            yaml_content = sub_convert.convert(urls, 'content', 'YAML')

        raw_yaml_content = yaml.safe_load(yaml_content.replace('?', '\question')) # 将 YAML 内容生成 Python 字典, 除去 YAML 中 ？ 的错误
        url_list = []
        proxies_list = raw_yaml_content['proxies']

        # 去重
        if dup_rm_enabled == True:
            begin = 0
            raw_length = len(proxies_list)
            length = len(proxies_list)
            while begin < length:
                if (begin + 1) == 1:
                    print(f'起始数量{length}')
                elif (begin + 1) % 50 == 0:
                    print(f'当前基准{begin + 1}-----当前数量{length}')
                elif (begin + 1) == length and (begin + 1) % 50 != 0:
                    repetition = raw_length - length
                    print(f'当前基准{begin + 1}-----当前数量{length}\n重复数量{repetition}')
                proxy_compared = proxies_list[begin]

                begin_2 = begin + 1
                while begin_2 <= (length - 1):

                    if proxy_compared['server'] == proxies_list[begin_2]['server'] and proxy_compared['port'] == proxies_list[begin_2]['port']:
                        proxies_list.pop(begin_2)
                        length -= 1
                    begin_2 += 1
                begin += 1

        # 改名
        for proxy in proxies_list:

            if format_name_enabled == True:

                emoji = {
                    'US': '🇺🇸','HK': '🇭🇰', 'SG': '🇸🇬',
                    'JP': '🇯🇵', 'TW': '🇹🇼', 'CA': '🇨🇦',
                    'nowhere_land': '🇦🇶'
                }

                server = proxy['server']
                query_add = 'https://ip.taobao.com/outGetIpInfo?ip='+server+'&accessKey=alibaba-inc' # 请求地址 ip sever from http://ip-api.com/ https://www.shuzhiduo.com/A/MyJxgqwAzn/
                #try:
                    #发送get请求
                query_data = requests.get(query_add)
                query_json_raw = json.dumps(query_data.text) # https://blog.csdn.net/zengNLP/article/details/105446885
                query_json = json.loads(json.loads(query_json_raw)) # 解决 json.loads 返回 str https://blog.csdn.net/qq_38604355/article/details/97239369
                #except Exception as err:
                #    print(f'{err} when get from {query_add}')

                query_status = query_json['msg']
                if query_status == 'query success':
                    query_countryCode = query_json['data']['country_id']
                    query_city = query_json['data']['city']
                    if query_countryCode in emoji:
                        country_emoji = emoji[query_countryCode]
                    else:
                        country_emoji = emoji['nowhere_land']
                    
                    if query_city != 'XX':
                        proxy['name'] = f'{country_emoji}-{query_city}-{server}'
                    elif query_city == 'XX':
                        proxy['name'] = f'{country_emoji}-{server}'
                elif query_status != 'query success':
                    print('Ip Invalid')
            
            try:
                if proxy['name'] != None: # NoneType 判定方法 https://blog.csdn.net/fu6543210/article/details/89462036
                    if '|' in proxy['name'] or '[' in proxy['name'] or '[' in proxy['name']:
                        proxy['name'] = '"' + proxy['name'] + '"'
            except Exception as err:
                print(err)
                pass

            proxy_str = str(proxy)
            url_list.append(proxy_str)

        yaml_content_dic = {'proxies': url_list}
        yaml_content_raw = yaml.dump(yaml_content_dic, default_flow_style=False, sort_keys=False, allow_unicode=True, width=750, indent=2) # yaml.dump 显示中文方法 https://blog.csdn.net/weixin_41548578/article/details/90651464 yaml.dump 各种参数 https://blog.csdn.net/swinfans/article/details/88770119
        yaml_content = yaml_content_raw.replace('\'', '')
        yaml_content = yaml_content.replace('False', 'false')
        yaml_content = yaml_content.replace('\question', '?')
        return yaml_content

    def url_format(sub_content): # 对节点 Url 进行格式化处理

        ss_pattern = re.compile(r'(?<!vme)ss://.*?(?=ss://|ssr://|vmess://|trojan://)')
        ss_urls = re.findall(ss_pattern, sub_content)

        ssr_pattern = re.compile(r'ssr://.*?(?=ss://|ssr://|vmess://|trojan://)')
        ssr_urls = re.findall(ssr_pattern, sub_content)

        vmess_pattern = re.compile(r'vmess://.*?(?=ss://|ssr://|vmess://|trojan://)')
        vmess_urls = re.findall(vmess_pattern, sub_content)

        trojan_pattern = re.compile(r'trojan://.*?(?=ss://|ssr://|vmess://|trojan://)')
        trojan_urls = re.findall(trojan_pattern, sub_content)

        urls = ss_urls + ssr_urls + vmess_urls + trojan_urls
        url_content = '\r'.join(urls)
        return sub_content

#Debug

""" sub_list_json = './sub/sub_list.json'

def read_list():
    with open(sub_list_json, 'r', encoding='utf-8') as f: # 将 sub_list.json Url 内容读取为列表
        raw_list = json.load(f)
    input_list = []
    for index in range(len(raw_list)):
        if raw_list[index]['enabled']:
            urls = re.split('\|',raw_list[index]['url'])
            if len(urls) > 1:
                for url in urls:
                    single_raw_list = raw_list[index]
                    single_raw_list['url'] = url
                    input_list.append(single_raw_list)
            input_list.append(raw_list[index])
    return input_list

input_list = read_list()
for index in range(len(input_list)):
    a = sub_convert.convert(input_list[index]['url'], 'url', 'YAML')
    b = sub_convert.proxies_filter(a, False, False)
    file = open('out.yml', 'w', encoding = 'utf-8')
    file.write(b)
    file.close() """