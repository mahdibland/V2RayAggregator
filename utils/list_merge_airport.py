#!/usr/bin/env python3
from urllib import request
import yaml
import os
import re
import json
from get_subs import subs
from list_update import update_url
from sub_convert import sub_convert


Eterniy = './Eternity'
readme = './README.md'

sub_list_airport_json = './sub/sub_list_airport.json'
sub_merge_path = './sub/'
sub_list_path = './sub/list/'


class sub_merge():
    def read_list(json_file, remote=False):  # 将 sub_list.json Url 内容读取为列表
        with open(json_file, 'r', encoding='utf-8') as f:
            raw_list = json.load(f)
        input_list = []
        for index in range(len(raw_list)):
            if raw_list[index]['enabled']:
                if remote == False:
                    urls = re.split('\|', raw_list[index]['url'])
                else:
                    urls = raw_list[index]['url']
                raw_list[index]['url'] = urls
                input_list.append(raw_list[index])
        return input_list

    def geoip_update(url):
        print('Downloading Country.mmdb...')
        try:
            request.urlretrieve(url, './utils/Country.mmdb')
            print('Success!\n')
        except Exception:
            print('Failed!\n')
            pass

    def readme_update(readme_file='./README.md', sub_list=[]):  # 更新 README 节点信息
        print('Update README.md file...')
        with open(readme_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            f.close()
        # 获得当前名单及各仓库节点数量
        with open('./sub/sub_merge.txt', 'r', encoding='utf-8') as f:
            total = len(f.readlines())
            total = f'Total number of merged nodes: `{total}`\n'
            thanks = []
            repo_amount_dic = {}
            for repo in sub_list:
                line = ''
                if repo['enabled'] == True:
                    id = repo['id']
                    remarks = repo['remarks']
                    repo_site = repo['site']

                    sub_file = f'./sub/list/{id:0>2d}.txt'
                    with open(sub_file, 'r', encoding='utf-8') as f:
                        proxies = f.readlines()
                        if proxies == ['Url 解析错误'] or proxies == ['订阅内容解析错误']:
                            amount = 0
                        else:
                            amount = len(proxies)
                        f.close()
                    repo_amount_dic.setdefault(id, amount)
                    line = f'- [{remarks}]({repo_site}), number of nodes: `{amount}`\n'
                if remarks != "alanbobs999/TopFreeProxies":
                    thanks.append(line)
            f.close()

        # 高速节点打印
        for index in range(len(lines)):
            if lines[index] == '### high-speed node\n':  # 目标行内容
                # 清除旧内容
                lines.pop(index+1)  # 删除节点数量
                while lines[index+4] != '\n':
                    lines.pop(index+4)

                with open('./Eternity', 'r', encoding='utf-8') as f:
                    proxies_base64 = f.read()
                    proxies = sub_convert.base64_decode(proxies_base64)
                    proxies = proxies.split('\n')
                    proxies = ['    '+proxy for proxy in proxies]
                    proxies = [proxy+'\n' for proxy in proxies]
                top_amount = len(proxies)

                lines.insert(
                    index+1, f'high-speed node quantity: `{top_amount}`\n')
                index += 4
                for i in proxies:
                    index += 1
                    lines.insert(index, i)
                break
        # 所有节点打印
        for index in range(len(lines)):
            if lines[index] == '### all nodes\n':  # 目标行内容
                # 清除旧内容
                lines.pop(index+1)  # 删除节点数量

                # with open('./sub/sub_merge.txt', 'r', encoding='utf-8') as f:
                with open('./sub/sub_merge_yaml.yml', 'r', encoding='utf-8') as f:
                    proxies = f.read()
                    proxies = proxies.split('\n')
                    top_amount = len(proxies) - 1
                    f.close()
                # if it's not yaml method we need to add 1 to the top amount
                lines.insert(
                    index+1, f'merge nodes w/o dup: `{top_amount}`\n')
                break
        # 节点来源打印
        for index in range(len(lines)):
            if lines[index] == '### node source\n':
                # 清除旧内容
                while lines[index+1] != '\n':
                    lines.pop(index+1)

                for i in thanks:
                    index += 1
                    lines.insert(index, i)
                break

        # 写入 README 内容
        with open(readme_file, 'w', encoding='utf-8') as f:
            data = ''.join(lines)
            print('Finish!\n')
            f.write(data)


if __name__ == '__main__':
    update_url.update_main(use_airport=True, airports_id=[
                           5], sub_list_json="./sub/sub_list_airport.json")
    # sub_merge.geoip_update(
    #     'https://raw.githubusercontent.com/Loyalsoldier/geoip/release/Country.mmdb')

    sub_list = sub_merge.read_list(sub_list_airport_json)
    sub_list_remote = sub_merge.read_list(sub_list_airport_json, True)

    subs.get_subs_v3(
        list(filter(lambda x: x['id'] == 5, sub_list)), output_path="airport_merge_yaml", should_cleanup=False, specific_files_cleanup=["05.txt"])
    # sub_merge.readme_update(readme, sub_list)
