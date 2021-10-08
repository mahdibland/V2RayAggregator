#!/usr/bin/env python3

from datetime import timedelta, datetime
import json


with open('./sub/sub_list.json', 'r', encoding='utf-8') as f: # 载入订阅链接
    raw_list = json.load(f)


def update_id_0(): # remarks: pojiezhiyuanjun/freev2, 将原链接更新至 https://raw.fastgit.org/pojiezhiyuanjun/freev2/master/%MM%(DD - 1).txt
    raw_url = raw_list[0]['url']

    yesterday = (datetime.today() + timedelta(-1)).strftime('%m%d')# 得到当前日期前一天 https://blog.csdn.net/wanghuafengc/article/details/42458721
    url_update = raw_url[:-8] + yesterday + raw_url[-4:]# 修改字符串中的某一位字符 https://www.zhihu.com/question/31800070/answer/53345749
    print(f'New url is : {url_update}')

update_id_0()