#!/usr/bin/env python3

from pathlib import Path
import json
import yaml
import base64
from urllib.parse import quote
import requests
from requests.adapters import HTTPAdapter

# 分析当前项目依赖 https://blog.csdn.net/lovedingd/article/details/102522094


sub_list_json = './sub/sub_list.json'
sub_metge_path = './sub'
sub_list_path = './sub/list/'


class sub_convert():# 将订阅链接中YAML，Base64等内容转换为 Url 链接内容
    
    def __init__(self,sub_url,output_type):
        self.sub_url = sub_url
        self.output_type = output_type
        self.url_content = ''
    
    def yaml_decode(content): # YAML 转换为 Url 链接内容
        yaml_content = yaml.dump(content)
        return yaml_content
    def base64_decode(content): # Base64 转换为 Url 链接内容
        base64_content = base64.b64decode(content.encode('utf-8')).decode('ascii')
        return base64_content

    def url_encode(self):# 读取订阅内容，并转化为 Url 链接内容

        s = requests.Session()
        s.mount('http://', HTTPAdapter(max_retries=3))
        s.mount('https://', HTTPAdapter(max_retries=3))
        try:
            print('Downloading from:' + self.sub_url)
            resp = s.get(self.sub_url, timeout=5)
            sub_content = resp.content.decode('utf-8') 

            if 'proxies:' in sub_content: # 判断字符串是否在文本中，是，判断为YAML。https://cloud.tencent.com/developer/article/1699719
                self.url_content = sub_convert.yaml_decode(sub_content)
                return self.url_content.replace('\r','')
                #return self.url_content.replace('\r','') # 去除‘回车\r符’ https://blog.csdn.net/jerrygaoling/article/details/81051447
            elif '://'  in sub_content: # 同上，是，判断为 Url 链接内容。
                self.url_content = sub_content
                return self.url_content.replace('\r','')
            else: # 判断 Base64.
                try:
                    self.url_content = sub_convert.base64_decode(sub_content)
                    self.url_content = base64.b64decode(sub_content.encode('utf-8')).decode('ascii')
                    return self.url_content.replace('\r','')
                except Exception: # 万能异常 https://blog.csdn.net/Candance_star/article/details/94135515
                    print('Url 订阅内容无法解析')
                    return 'Url 订阅内容无法解析'

        except Exception as err:
            print(err)
            return 'Url 解析错误'

        
    def yaml_encode(url_content): # 将 Url 内容转换为 YAML 
        yaml_content = url_content
        return yaml_content
    def base64_encode(url_content): # 将 Url 内容转换为 Base64
        base64_content = base64.b64encode(url_content.encode('utf-8')).decode('ascii')
        return base64_content

    def convert(self): # convert Url to YAML or Base64

        if self.output_type == 'YAML':
            return sub_convert.yaml_encode(self.url_content)
        elif self.output_type == 'Base64':
            return sub_convert.base64_encode(self.url_content)


class sub_merge(): # 将转换后的所有 Url 链接内容合并转换 YAML or Base64, ，并输出文件，输入订阅列表。

    def __init__(self,url_list):
        
        self.url_list = url_list

    def merge(self): # 将各自 Url 内容生成列表

        content_list = []
        for index in range(len(self.url_list)):
            content = sub_convert(self.url_list[index],'').url_encode()
            ids = sub_list[index]['id']
            remarks = sub_list[index]['remarks']
            #try:
            if content == 'Url 解析错误':
                file = open(f'{sub_list_path}{ids:0>2d}.txt', 'w', encoding = 'utf-8')
                file.write('Url 解析错误')
                file.close()
                print(f'Writing error of {remarks} to {ids:0>2d}.txt\n')
            elif content == 'Url 订阅内容无法解析':
                file = open(f'{sub_list_path}{ids:0>2d}.txt', 'w', encoding = 'utf-8')
                file.write('Url 订阅内容无法解析')
                file.close()
                print(f'Writing error of {remarks} to {ids:0>2d}.txt\n')
            else:
                content_list.append(content)
                file = open(f'{sub_list_path}{ids:0>2d}.txt', 'w', encoding = 'utf-8')
                file.write(content)
                file.close()
                print(f'Writing content of {remarks} to {ids:0>2d}.txt\n')
        
        print('Merging nodes...\n')
        content = '\n'.join(content_list) # https://python3-cookbook.readthedocs.io/zh_CN/latest/c02/p14_combine_and_concatenate_strings.html
        content_base64 = sub_convert.base64_encode(content)
        content_yaml = sub_convert.yaml_encode(content)

        def content_write(file, output_type):
            file = open(file, 'w', encoding = 'utf-8')
            file.write(output_type)
            file.close
        write_list = [f'{sub_metge_path}/sub_merge.txt', f'{sub_metge_path}/sub_merge_base64.txt', f'{sub_metge_path}/sub_merge_yaml.txt']
        content_type = (content, content_base64, content_yaml)
        for index in range(len(write_list)):
            content_write(write_list[index], content_type[index])
        print('Done!')


with open(sub_list_json, 'r', encoding='utf-8') as f:
    raw_list = json.load(f)
sub_list = []
for index in range(len(raw_list)): # 将 sub_list.json Url 内容读取为列表
    if raw_list[index]['enabled']:
        sub_list.append(raw_list[index])

input_list = []
for index in range(len(sub_list)): # 将 sub_list.json Url 内容读取为列表
        input_list.append(sub_list[index]['url'])
run = sub_merge(input_list).merge()
