from sub_convert import sub_convert
from subs_function import subs_function

import json
import re
import os
import yaml

sub_list_json = './sub/sub_list.json'
sub_merge_path = './sub/'
sub_list_path = './sub/list/'

ipv4 = r"([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})"
ipv6 = r'(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))'


class subs:

    def get_subs(content_urls: []):
        if content_urls == []:
            return

        for t in os.walk(sub_list_path):
            for f in t[2]:
                f = t[0]+f
                os.remove(f)

        content_list = []
        for (index, url_container) in enumerate(content_urls):
            ids = content_urls[index]['id']
            remarks = content_urls[index]['remarks']
            if type(url_container['url']) == list:
                for each_url in url_container["url"]:
                    print("gather server from " + each_url)
                    content = subs_function.convert_sub(
                        each_url, 'mixed', "http://0.0.0.0:25500")
                    print("added content: %s" %
                          str(content.split('\n').__len__()))
                    if content == 'Err: No nodes found' or content == 'Err: failed to parse sub':
                        print("host convertor failed. trying manually...")
                        content = sub_convert.main(each_url, 'url', 'url')
                        if content != 'Url 解析错误' and content != '订阅内容解析错误':
                            if subs_function.is_line_valid(content) != '':
                                content_list.append(content)
                            else:
                                print(f'this url failed{each_url}')
                            print(
                                f'Writing content of {remarks} to {ids:0>2d}.txt\n')
                        else:
                            print(
                                f'Writing error of {remarks} to {ids:0>2d}.txt\n')

                            if content == 'Err: No nodes found':
                                file = open(f'{sub_list_path}{ids:0>2d}.txt',
                                            'a+', encoding='utf-8')
                                file.write(content)
                                file.close()

                            if content == 'Err: failed to parse sub':
                                file = open(f'{sub_list_path}{ids:0>2d}.txt',
                                            'a+', encoding='utf-8')
                                file.write('Err: failed to parse sub')
                                file.close()

                    elif content != None and content != '':
                        if subs_function.is_line_valid(content) != '':
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

            print('already gathered ' +
                  str(''.join(content_list).split('\n').__len__()))
            print('\n')

        print('Merging nodes...\n')

        content_list = list(
            filter(lambda x: x != '', ''.join(content_list).split("\n")))
        content_raw = "\n".join(content_list)

        print(f"it's fine till here with {content_list.__len__()} lines")

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

    def get_subs_v2(content_urls: []):
        if content_urls == []:
            return

        for t in os.walk(sub_list_path):
            for f in t[2]:
                f = t[0]+f
                os.remove(f)

        content_list = []
        corresponding_list = []
        corresponding_id = 0
        for (index, url_container) in enumerate(content_urls):
            ids = content_urls[index]['id']
            remarks = content_urls[index]['remarks']
            if type(url_container['url']) == list:
                for each_url in url_container["url"]:
                    print("gather server from " + each_url)

                    content = subs_function.convert_sub(
                        each_url, 'mixed', "http://0.0.0.0:25500")
                    content_clash = subs_function.convert_sub(
                        each_url, 'clash', "http://0.0.0.0:25500")

                    print("added content: %s" %
                          str(content.split('\n').__len__()))

                    if content == 'Err: No nodes found' or content == 'Err: failed to parse sub':
                        print("host convertor failed. just continue & ignore...")
                        if content == 'Err: No nodes found':
                            file = open(f'{sub_list_path}{ids:0>2d}.txt',
                                        'a+', encoding='utf-8')
                            file.write(content)
                            file.close()

                        if content == 'Err: failed to parse sub':
                            file = open(f'{sub_list_path}{ids:0>2d}.txt',
                                        'a+', encoding='utf-8')
                            file.write('Err: failed to parse sub')
                            file.close()

                    elif content != None and content != '':
                        # creating corresponding list
                        if subs_function.is_line_valid(content) != '':
                            content_list.append(content)

                            mixed_content = "".join(content_list).split('\n')
                            clash_content = "".join(content_clash)

                            try:
                                clash_content = yaml.safe_load(
                                    clash_content)["proxies"]
                            except Exception as e:
                                print(e)

                            if clash_content.__len__() == mixed_content.__len__():
                                for (index, each_clash_proxy) in enumerate(clash_content):
                                    if re.search(ipv6, str(each_clash_proxy)) == None or re.search(ipv4, str(each_clash_proxy)) != None:
                                        if re.search("path: /(.*?)\?(.*?)=(.*?)}", str(each_clash_proxy)) == None:
                                            try:
                                                # make sure the c_clash_proxy is a valid yaml format
                                                # also it could be redundent code but it's for safety
                                                yaml.safe_load(
                                                    str(each_clash_proxy))
                                                corresponding_list.append(
                                                    {"id": corresponding_id, "c_clash": each_clash_proxy, "c_mixed": mixed_content[index]})
                                                corresponding_id += 1
                                            except Exception as e:
                                                print(e)

                            else:
                                print(f'this url failed {each_url}')
                                file = open(f'{sub_list_path}{ids:0>2d}.txt',
                                            'a+', encoding='utf-8')
                                file.write(content)
                                file.close()
                                print(
                                    f'Writing content of {remarks} to {ids:0>2d}.txt\n')
                        else:
                            print(f'this url failed {each_url}')
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

            print('already gathered ' +
                  str(''.join(content_list).split('\n').__len__()))
            print('\n')

        print('Merging nodes...\n')

        content_list = list(
            filter(lambda x: x != '', ''.join(content_list).split("\n")))
        content_raw = "\n".join(content_list)

        print(f"it's fine till here with {content_list.__len__()} lines")

        ################  okay everything is fine till here ################
        '''
        we should have a list of corresponding proxies and they are ready to be fixed in 2 ways:
        1- making their name better (using their server) => via thier clash corresponding
        2- remove duplicate proxies from the list => via thier clash corresponding
        after that we have clean list that contains both type that we need with modification and no conversion :)
        '''

        ################  Fix names  ################
        corresponding_list = subs_function.fix_proxies_name(
            corresponding_proxies=corresponding_list)

        ################  Fix Duplication  ################
        corresponding_list = subs_function.fix_proxies_duplication(
            corresponding_proxies=corresponding_list)

        # print(f"found {yaml_proxies.__len__() - temp.__len__()} bad lines :)")
        # content_yaml = "\n".join(temp)
        # if content_yaml[-1:] == '\n':
        #     content_yaml[-1:] = ''
        # content_yaml = 'proxies:\n' + content_yaml

        clash = list(map(lambda x: f"  - {x['c_clash']}", corresponding_list))
        mixed = list(map(lambda x: x["c_mixed"], corresponding_list))
        content_raw = "\n".join(mixed)

        content_yaml = 'proxies:\n' + "\n".join(clash)
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


if __name__ == "__main__":
    subs.get_subs([])
