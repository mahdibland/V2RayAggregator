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

                    if content == 'Err: No nodes found':
                        print("host convertor failed. trying manually...")
                        content = sub_convert.main(each_url, 'url', 'url')
                        if content != 'Url 解析错误':
                            if subs_function.is_line_valid(content) != '':
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

                    elif content == 'Err: failed to parse sub':
                        file = open(f'{sub_list_path}{ids:0>2d}.txt',
                                    'a+', encoding='utf-8')
                        file.write('Err: failed to parse sub')
                        file.close()
                        print(
                            f'Writing error of {remarks} to {ids:0>2d}.txt\n')

                    elif content != None and content != '':
                        print("host convertor failed. trying manually...")
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


if __name__ == "__main__":
    subs.get_subs([])
