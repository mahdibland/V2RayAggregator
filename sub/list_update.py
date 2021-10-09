#!/usr/bin/env python3

from datetime import timedelta, datetime
import json

# 文件路径定义
sub_list_json = './sub/sub_list.json'


with open(sub_list_json, 'r', encoding='utf-8') as f: # 载入订阅链接
    raw_list = json.load(f)
    f.close()

class url_update():

    def __init__(self,allow_id_list):
        self.allow_id_list = allow_id_list

    def update_id_0(): # remarks: pojiezhiyuanjun/freev2, 将原链接更新至 https://raw.fastgit.org/pojiezhiyuanjun/freev2/master/%MM%(DD - 1).txt
        raw_url = raw_list[0]['url']
        yesterday = (datetime.today() + timedelta(-1)).strftime('%m%d')# 得到当前日期前一天 https://blog.csdn.net/wanghuafengc/article/details/42458721
        url_update = raw_url[:-8] + yesterday + raw_url[-4:]# 修改字符串中的某一位字符 https://www.zhihu.com/question/31800070/answer/53345749
        print(f'Change id 0 url to : {url_update}\n')
        raw_list[0]['url'] = url_update

    def run_update(self,json_file=sub_list_json):
        for item in self.allow_id_list:
            if item == 0:
                url_update.update_id_0()

        updated_list = json.dumps(raw_list, sort_keys=False, indent=2, ensure_ascii=False)
        file = open(json_file, 'w', encoding='utf-8')
        file.write(updated_list)
        file.close()
