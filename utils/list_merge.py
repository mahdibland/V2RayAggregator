#!/usr/bin/env python3

from sub_convert import sub_convert # Python 之间互相调用文件https://blog.csdn.net/winycg/article/details/78512300
from list_update import update_url

import json, re
from urllib import request


# 分析当前项目依赖 https://blog.csdn.net/lovedingd/article/details/102522094


# 文件路径定义
Eterniy = './Eternity'

sub_list_json = './sub/sub_list.json'
sub_merge_path = './sub/'
sub_list_path = './sub/list/'


def sub_merge(url_list): # # 将转换后的所有 Url 链接内容合并转换 YAML or Base64, ，并输出文件，输入订阅列表。

    content_list = []
    for index in range(len(url_list)):
        content = sub_convert.convert(url_list[index]['url'],'url','url')
        ids = url_list[index]['id']
        remarks = url_list[index]['remarks']
        #try:
        if content == 'Url 解析错误':
            file = open(f'{sub_list_path}{ids:0>2d}.txt', 'w', encoding= 'utf-8')
            file.write('Url 解析错误')
            file.close()
            print(f'Writing error of {remarks} to {ids:0>2d}.txt\n')
        elif content == 'Url 订阅内容无法解析':
            file = open(f'{sub_list_path}{ids:0>2d}.txt', 'w', encoding= 'utf-8')
            file.write('Url 订阅内容无法解析')
            file.close()
            print(f'Writing error of {remarks} to {ids:0>2d}.txt\n')
        elif content != None:
            content_list.append(content)
            file = open(f'{sub_list_path}{ids:0>2d}.txt', 'w', encoding= 'utf-8')
            file.write(content)
            file.close()
            print(f'Writing content of {remarks} to {ids:0>2d}.txt\n')
        else:
            file = open(f'{sub_list_path}{ids:0>2d}.txt', 'w', encoding= 'utf-8')
            file.write('Url 订阅内容无法解析')
            file.close()
            print(f'Writing error of {remarks} to {ids:0>2d}.txt\n')

    print('Merging nodes...\n')
    content_raw = ''.join(content_list) # https://python3-cookbook.readthedocs.io/zh_CN/latest/c02/p14_combine_and_concatenate_strings.html
    content_yaml = sub_convert.convert(content_raw,'content','YAML', True)
    content_base64 = sub_convert.convert(content_yaml,'content','Base64')
    content = sub_convert.convert(content_yaml,'content','url')

    def content_write(file, output_type):
        file = open(file, 'w', encoding = 'utf-8')
        file.write(output_type)
        file.close
    write_list = [f'{sub_merge_path}/sub_merge.txt', f'{sub_merge_path}/sub_merge_base64.txt', f'{sub_merge_path}/sub_merge_yaml.yml']
    content_type = (content, content_base64, content_yaml)
    for index in range(len(write_list)):
        content_write(write_list[index], content_type[index])
    print('Done!')

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

def geoip_update(url):
    print('Downloading Country.mmdb...')
    try:
        request.urlretrieve(url, './utils/Country.mmdb')
        print('Success!')
    except Exception:
        print('Failed!')
        pass

sub_list = read_list()

update_url.update([0,])
geoip_update('https://cdn.jsdelivr.net/gh/Loyalsoldier/geoip@release/Country.mmdb')

merge = sub_merge(sub_list)
