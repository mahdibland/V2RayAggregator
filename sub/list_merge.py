#!/usr/bin/env python3

from requests.sessions import merge_cookies
from sub_convert import sub_convert # Python 之间互相调用文件https://blog.csdn.net/winycg/article/details/78512300
from list_update import update_url

import json
import os


# 分析当前项目依赖 https://blog.csdn.net/lovedingd/article/details/102522094


# 文件路径定义
sub_list_json = './sub/sub_list.json'
sub_merge_path = './sub/'
sub_list_path = './sub/list/'


class sub_merge(): # 将转换后的所有 Url 链接内容合并转换 YAML or Base64, ，并输出文件，输入订阅列表。

    def __init__(self,url_list):
        
        self.url_list = url_list

    def merge(self): # 将各自 Url 内容生成列表

        content_list = []
        for index in range(len(self.url_list)):
            content = sub_convert.url_decode(self.url_list[index])
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
        content_base64 = sub_convert.convert(content,'Base64')
        content_yaml = sub_convert.convert(content,'YAML')

        def content_write(file, output_type):
            file = open(file, 'w', encoding = 'utf-8')
            file.write(output_type)
            file.close
        write_list = [f'{sub_merge_path}/sub_merge.txt', f'{sub_merge_path}/sub_merge_base64.txt', f'{sub_merge_path}/sub_merge_yaml.yml']
        content_type = (content, content_base64, content_yaml)
        for index in range(len(write_list)):
            content_write(write_list[index], content_type[index])
        print('Done!')


with open(sub_list_json, 'r', encoding='utf-8') as f: # 将 sub_list.json Url 内容读取为列表
    raw_list = json.load(f)
sub_list = []
for index in range(len(raw_list)):
    if raw_list[index]['enabled']:
        sub_list.append(raw_list[index])
input_list = []
for index in range(len(sub_list)):
        input_list.append(sub_list[index]['url'])


update = update_url.update([0,])
merge = sub_merge(input_list).merge()
