#!/usr/bin/env python3

# Python 之间互相调用文件https://blog.csdn.net/winycg/article/details/78512300
from sub_convert import sub_convert
from list_update import update_url
from get_subs import subs

import json
import re
import os
import yaml
from urllib import request


# 分析当前项目依赖 https://blog.csdn.net/lovedingd/article/details/102522094


# 文件路径定义
Eterniy = './Eternity'
readme = './README.md'

sub_list_json = './sub/sub_list.json'
sub_merge_path = './sub/'
sub_list_path = './sub/list/'

ipv4 = r"([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})"
ipv6 = r'(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))'


def add_valid(line):
    if (line.__contains__("ssr://") or line.__contains__("ss://")
            or line.__contains__("trojan://") or line.__contains__("vmess://")):
        return line
    return ''


class sub_merge():
    def sub_merge(url_list):  # 将转换后的所有 Url 链接内容合并转换 YAML or Base64, ，并输出文件，输入订阅列表。

        content_list = []
        for t in os.walk(sub_list_path):
            for f in t[2]:
                f = t[0]+f
                os.remove(f)

        for (index, url_container) in enumerate(url_list):
            ids = url_list[index]['id']
            remarks = url_list[index]['remarks']
            if type(url_container['url']) == list:
                for each_url in url_container["url"]:
                    content = ''
                    print("gather server from " + each_url)
                    content += sub_convert.convert_remote(
                        each_url, 'url', 'http://127.0.0.1:25500')

                    if content == 'Url 解析错误':
                        content = sub_convert.main(each_url, 'url', 'url')
                        if content != 'Url 解析错误':
                            if add_valid(content) != '':
                                content_list.append(content)
                            else:
                                print(f'this url failed{each_url}')
                            print(
                                f'Writing content of {remarks} to {ids:0>2d}.txt\n')
                        else:
                            print(
                                f'Writing error of {remarks} to {ids:0>2d}.txt\n')
                        file = open(f'{sub_list_path}{ids:0>2d}.txt',
                                    'a+', encoding='utf-8')
                        file.write(content)
                        file.close()
                    elif content == 'Url 订阅内容无法解析':
                        file = open(f'{sub_list_path}{ids:0>2d}.txt',
                                    'a+', encoding='utf-8')
                        file.write('Url Subscription could not be parsed')
                        file.close()
                        print(
                            f'Writing error of {remarks} to {ids:0>2d}.txt\n')
                    elif content != None:
                        if add_valid(content) != '':
                            content_list.append(content)
                        else:
                            print(f'this url failed{each_url}')
                        file = open(f'{sub_list_path}{ids:0>2d}.txt',
                                    'a+', encoding='utf-8')
                        file.write(content)
                        file.close()
                        print(
                            f'Writing content of {remarks} to {ids:0>2d}.txt\n')
                    else:
                        file = open(f'{sub_list_path}{ids:0>2d}.txt',
                                    'a+', encoding='utf-8')
                        file.write('Url Subscription could not be parsed')
                        file.close()
                        print(
                            f'Writing error of {remarks} to {ids:0>2d}.txt\n')

            # it's not coming down here just adding it :)
            else:
                each_url = url_container["url"]
                content = ''
                print("gather server from " + each_url)
                content += sub_convert.convert_remote(
                    each_url, 'url', 'http://127.0.0.1:25500')

                if content == 'Url 解析错误':
                    content = sub_convert.main(each_url, 'url', 'url')
                    if content != 'Url 解析错误':
                        if add_valid(content) != '':
                            content_list.append(content)
                        else:
                            print(f'this url failed{each_url}')

                        print(
                            f'Writing content of {remarks} to {ids:0>2d}.txt\n')
                    else:
                        print(
                            f'Writing error of {remarks} to {ids:0>2d}.txt\n')
                    file = open(f'{sub_list_path}{ids:0>2d}.txt',
                                'a+', encoding='utf-8')
                    file.write(content)
                    file.close()
                elif content == 'Url 订阅内容无法解析':
                    file = open(f'{sub_list_path}{ids:0>2d}.txt',
                                'a+', encoding='utf-8')
                    file.write('Url Subscription could not be parsed')
                    file.close()
                    print(f'Writing error of {remarks} to {ids:0>2d}.txt\n')
                elif content != None:
                    content_list.append(content)
                    file = open(f'{sub_list_path}{ids:0>2d}.txt',
                                'a+', encoding='utf-8')
                    file.write(content)
                    file.close()
                    print(f'Writing content of {remarks} to {ids:0>2d}.txt\n')
                else:
                    file = open(f'{sub_list_path}{ids:0>2d}.txt',
                                'a+', encoding='utf-8')
                    file.write('Url Subscription could not be parsed')
                    file.close()
                    print(f'Writing error of {remarks} to {ids:0>2d}.txt\n')

            print('already gathered ' +
                  str(''.join(content_list).split('\n').__len__()))
            print('\n')

        print('Merging nodes...\n')
        # content_raw = '\n'.join(content_list)

        content_list = list(
            filter(lambda x: x != '', ''.join(content_list).split("\n")))
        # dup remove by string content
#         print("it was " + str(content_list.__len__()))
#         content_list = list(set(content_list))
#         print("now is " + str(content_list.__len__()))
        content_list = list(filter(lambda x: x.startswith("ssr://") or x.startswith("ss://")
                                   or x.startswith("trojan://") or x.startswith("vmess://"), content_list))

        content_list = list(
            filter(lambda x: x.__contains__("订阅内容解析错误") == False, content_list))
        content_raw = "\n".join(content_list)

        print(f"it's fine till here with {content_list.__len__()} lines")

        # content_yaml = sub_convert.main(content_raw, 'content', 'content', {
        #                                 'dup_rm_enabled': True, 'format_name_enabled': True})
        # final_content = sub_convert.makeup(
        #     content_raw, True, True)
        # content_raw = sub_convert.yaml_decode(final_content)

        content_yaml = sub_convert.main(content_raw, 'content', 'YAML', {
            'dup_rm_enabled': True, 'format_name_enabled': True})

        yaml_proxies = content_yaml.split('\n')[1:]
        temp = list(filter(lambda x: re.search(ipv6, x) ==
                    None or re.search(ipv4, x) != None, yaml_proxies))
        temp = list(filter(lambda x: re.search(
            "path: /(.*?)\?(.*?)=(.*?)}", x) == None, temp))

        temp2 = temp
        temp = []
        for pr in temp2:
            try:
                yaml.safe_load(pr)
                temp.append(pr)
            except Exception as e:
                print(e)

        print(f"found {yaml_proxies.__len__() - temp.__len__()} bad lines :)")
        ###temp###
#         print(temp)
        ##########
        content_yaml = "\n".join(temp)
        if content_yaml[-1:] == '\n':
            content_yaml[-1:] = ''
        content_yaml = 'proxies:\n' + content_yaml

        # todo removed dup
        content_raw = sub_convert.yaml_decode(content_yaml)

#         print('decoded content')
#         print(content_raw)

        # note removed here
        # content_raw = list(
        #     filter(lambda x: x != '', content_raw.split("\n")))
        # content_raw = "\n".join(content_raw)

        content_base64 = sub_convert.base64_encode(content_raw)

        content = content_raw

        ##############################

        def content_write(file, output_type):
            file = open(file, 'w+', encoding='utf-8')
            file.write(output_type)
            file.close

        write_list = [f'{sub_merge_path}/sub_merge.txt',
                      f'{sub_merge_path}/sub_merge_base64.txt', f'{sub_merge_path}/sub_merge_yaml.yml']
        content_type = (content, content_base64, content_yaml)
        for index in range(len(write_list)):
            content_write(write_list[index], content_type[index])
        print('Done!\n')

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
            f.close()
            for repo in sub_list:
                # not breaking the process only because of showcase :)
                try:
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
                    # if remarks != "mahdibland/SSAggregator":
                    #     thanks.append(line)
                except FileNotFoundError:
                    try:
                        with open(sub_file, 'r', encoding='utf-8') as f:
                            proxies = f.readlines()
                            if proxies == ['Url 解析错误'] or proxies == ['订阅内容解析错误']:
                                amount = 0
                            else:
                                amount = len(proxies)
                            f.close()
                        repo_amount_dic.setdefault(id, amount)
                        line = f'- [{remarks}]({repo_site}), number of nodes: `{amount}`\n'
                    except:
                        # ignore it
                        pass
                except:
                    # ignore it
                    pass

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
                """
                with open('./sub/sub_merge.txt', 'r', encoding='utf-8') as f:
                    proxies = f.read()
                    proxies = proxies.split('\n')
                    proxies = ['    '+proxy for proxy in proxies]
                    proxies = [proxy+'\n' for proxy in proxies]
                top_amount = len(proxies) - 1
                
                lines.insert(index+1, f'合并节点数量: `{top_amount}`\n')
                
                index += 5
                for i in proxies:
                    index += 1
                    lines.insert(index, i)
                """
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
    update_url.update_main(use_airport=False, airports_id=[
                           5], sub_list_json="./sub/sub_list.json")
    sub_merge.geoip_update(
        'https://raw.githubusercontent.com/Loyalsoldier/geoip/release/Country.mmdb')

    sub_list = sub_merge.read_list(sub_list_json)
    sub_list_remote = sub_merge.read_list(sub_list_json, True)

    # default method
    # sub_merge.sub_merge(sub_list)
    # sub_merge.readme_update(readme, sub_list)

    # fixed convertor in default method
    # subs.get_subs(sub_list)
    # sub_merge.readme_update(readme, sub_list)

    # using corresponding proxies method
    # subs.get_subs_v2(sub_list)
    # sub_merge.readme_update(readme, sub_list)

    # eject sub converting using local method and using sub convertor instead (only yaml available there is no
    # base64 or mixed type proxy in this method and other types will be handle using other workflows)
    subs.get_subs_v3(list(filter(lambda x: x['id'] != 5, sub_list)))
    sub_merge.readme_update(readme, sub_list)
