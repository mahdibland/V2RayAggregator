#!/usr/bin/env python3

from sub_convert import sub_convert # Python 之间互相调用文件https://blog.csdn.net/winycg/article/details/78512300
from list_update import update_url

import json, re
from urllib import request


# 分析当前项目依赖 https://blog.csdn.net/lovedingd/article/details/102522094


# 文件路径定义
Eterniy = './Eternity'
readme = './README.md'

sub_list_json = './sub/sub_list.json'
sub_merge_path = './sub/'
sub_list_path = './sub/list/'

class sub_merge():
    def sub_merge(url_list): # 将转换后的所有 Url 链接内容合并转换 YAML or Base64, ，并输出文件，输入订阅列表。

        content_list = []
        for index in range(len(url_list)):
            content = sub_convert.convert_remote(url_list[index]['url'],'url')
            ids = url_list[index]['id']
            remarks = url_list[index]['remarks']
            #try:
            if content == 'Url 解析错误':
                content = sub_convert.convert(sub_merge.read_list(sub_list_json)[index]['url'],'url','url')
                if content != 'Url 解析错误':
                    content_list.append(content)
                    print(f'Writing content of {remarks} to {ids:0>2d}.txt\n')
                else:
                    print(f'Writing error of {remarks} to {ids:0>2d}.txt\n')
                file = open(f'{sub_list_path}{ids:0>2d}.txt', 'w', encoding= 'utf-8')
                file.write('Url 解析错误')
                file.close()
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
        content_yaml = sub_convert.convert(content_raw,'content','YAML',{'dup_rm_enabled': False, 'format_name_enabled': True})
        content_base64 = sub_convert.base64_encode(content_yaml)
        content = content_raw

        def content_write(file, output_type):
            file = open(file, 'w', encoding = 'utf-8')
            file.write(output_type)
            file.close
        
        write_list = [f'{sub_merge_path}/sub_merge.txt', f'{sub_merge_path}/sub_merge_base64.txt', f'{sub_merge_path}/sub_merge_yaml.yml']
        content_type = (content, content_base64, content_yaml)
        for index in range(len(write_list)):
            content_write(write_list[index], content_type[index])
        print('Done!\n')

    def read_list(json_file,remote=False): # 将 sub_list.json Url 内容读取为列表
        with open(json_file, 'r', encoding='utf-8') as f:
            raw_list = json.load(f)
        input_list = []
        for index in range(len(raw_list)):
            if raw_list[index]['enabled']:
                if remote == False:
                    urls = re.split('\|',raw_list[index]['url'])
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

    def readme_update(readme_file='./README.md', sub_list=[]): # 更新 README 节点信息
        print('更新 README.md 中')
        with open(readme_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # 获得当前名单及各仓库节点数量
        with open('./sub/sub_merge.txt', 'r', encoding='utf-8') as f:
            total = len(f.readlines())
            total = f'当前合并节点总数: `{total}`\n'
        thanks = [total]
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
                
                repo_amount_dic.setdefault(id, amount)
                line = f'- [{remarks}]({repo_site}), 节点数量: `{amount}`\n'
            if id != 12:
                thanks.append(line)

        # 鸣谢名单打印
        for index in range(len(lines)):
            if lines[index] == '### 鸣谢名单\n':
                # 清除旧内容
                while lines[index+1] != '\n':
                    lines.pop(index+1)

                for i in thanks:
                    index +=1
                    lines.insert(index, i)
                break

        # 当前节点打印
        for index in range(len(lines)):
            if lines[index] == '  <summary>展开复制节点</summary>\n': # 目标行内容
                # 清除旧内容
                lines.pop(index-3) # 删除节点数量
                index -= 1 # 使 index 所指内容不变
                while lines[index+2] != '\n':
                    lines.pop(index+2)

                with open('./Eternity', 'r', encoding='utf-8') as f:
                    proxies_base64 = f.read()
                    proxies = sub_convert.convert(proxies_base64,'content','url')
                    proxies = proxies.split('\n')
                    proxies = ['    '+proxy for proxy in proxies]
                    proxies = [proxy+'\n' for proxy in proxies]
                top_amount = len(proxies) - 1
                
                lines.insert(index-2, f'当前节点数量: `{top_amount}`\n')
                index += 2
                for i in proxies:
                    index += 1
                    lines.insert(index, i)
                break

        # 写入 README 内容
        with open(readme_file, 'w', encoding='utf-8') as f:
            data = ''.join(lines)
            print('完成!\n')
            f.write(data)

if __name__ == '__main__':
    #update_url.update_main([0,21,22])
    #sub_merge.geoip_update('https://raw.githubusercontent.com/Loyalsoldier/geoip/release/Country.mmdb')

    sub_list = sub_merge.read_list(sub_list_json)
    sub_list_remote = sub_merge.read_list(sub_list_json,True)
    sub_merge.sub_merge(sub_list_remote)
    sub_merge.readme_update(readme,sub_list)
