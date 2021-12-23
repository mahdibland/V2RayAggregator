#!/usr/bin/env python3

from datetime import timedelta, datetime
import json, re
import requests
from requests.adapters import HTTPAdapter

# 文件路径定义
sub_list_json = './sub/sub_list.json'


with open(sub_list_json, 'r', encoding='utf-8') as f: # 载入订阅链接
    raw_list = json.load(f)
    f.close()

def url_test(url):
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=5))
    s.mount('https://', HTTPAdapter(max_retries=5))
    try:
        resp = s.get(url, timeout=3)
        url_updated = True
    except Exception:
        url_updated = False
    return url_updated

class update_url():

    def update(id_allow_list=[]):
        if len(id_allow_list) > 0:
            for id in id_allow_list:
                if id == 0:
                    update_url.update_id_0()
                if id == 22:
                    update_url.update_id_22()

            updated_list = json.dumps(raw_list, sort_keys=False, indent=2, ensure_ascii=False)
            file = open(sub_list_json, 'w', encoding='utf-8')
            file.write(updated_list)
            file.close()
        else:
            print('Don\'t need to update.')
                
    def update_id_0(): # remarks: pojiezhiyuanjun/freev2, 将原链接更新至 https://raw.fastgit.org/pojiezhiyuanjun/freev2/master/%MM%(DD - 1).txt
        raw_url = raw_list[0]['url']
        yesterday = (datetime.today() + timedelta(-1)).strftime('%m%d')# 得到当前日期前一天 https://blog.csdn.net/wanghuafengc/article/details/42458721
        url_update = raw_url[:-8] + yesterday + raw_url[-4:]# 修改字符串中的某一位字符 https://www.zhihu.com/question/31800070/answer/53345749
        print(f'Change id 0 url to : {url_update}\n')
        raw_list[0]['url'] = url_update
    
    def update_id_22():
        date_inurl = datetime.today().strftime('%Y/%m/%Y-%m-%d')
        #date_inurl = '2021/12/2021-12-08'
        url_update = f'https://www.mattkaydiary.com/{date_inurl}-free-v2ray-clash-nodes.html'
        try:
            resp = requests.get(url_update, timeout=5)
            raw_content = resp.text
            raw_content = raw_content.replace('amp;', '')

            #print(raw_content.find('v2ray(请开启代理后再拉取)&#65306;https://drive.google.com/uc'))
            #print(raw_content[raw_content.find('v2ray(请开启代理后再拉取)&#65306;https://drive.google.com/uc'):raw_content.find('v2ray(请开启代理后再拉取)&#65306;https://drive.google.com/uc')+100])
            pattern = re.compile(r'v2ray\(请开启代理后再拉取\)&#65306;https://drive\.google\.com/uc\?export=download&id=\w*-*\w*')
            
            url_update = re.findall(pattern, raw_content)[0][24:]
            print(f'Change id 22 url to : {url_update}\n')
            raw_list[22]['url'] = url_update
        except Exception:
            print('Id 22 url 无需更新')
            pass
