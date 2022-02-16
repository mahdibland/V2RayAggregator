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

def url_updated(url): # 判断远程远程链接是否已经更新
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=2))
    s.mount('https://', HTTPAdapter(max_retries=2))
    try:
        resp = s.get(url, timeout=2)
        status = resp.status_code
    except Exception:
        status = 404
    if status == 200:
        url_updated = True
    else:
        url_updated = False
    return url_updated

class update_url():

    def update_main(update_enable_list=[]):
        if len(update_enable_list) > 0:
            for id in update_enable_list:
                if id == 0:
                    status = update_url.update_id_0()
                    update_url.update_write(id, status[1], status[1])
                elif id == 21:
                    status = update_url.update_id_21()
                    update_url.update_write(id, status[1], status[1])
                elif id == 22:
                    status = update_url.update_id_22()
                    update_url.update_write(id, status[1], status[1])

            updated_list = json.dumps(raw_list, sort_keys=False, indent=2, ensure_ascii=False)
            file = open(sub_list_json, 'w', encoding='utf-8')
            file.write(updated_list)
            file.close()
        else:
            print('Don\'t need to be updated.')
                
    def update_write(id, status, updated_url):
        if status == 404:
            print(f'Id {id} URL 无可用更新\n')
        else:
            if updated_url != raw_list[id]['url']:
                raw_list[id]['url'] = updated_url
                print(f'Id {id} URL 更新至 : {updated_url}\n')
            else:
                print(f'Id {id} URL 无可用更新\n')

    def update_id_0(): # remarks: pojiezhiyuanjun/freev2, 将原链接更新至 https://raw.fastgit.org/pojiezhiyuanjun/freev2/master/%MM%(DD - 1).txt
        #yesterday = (datetime.today() + timedelta(-1)).strftime('%m%d')# 得到当前日期前一天 https://blog.csdn.net/wanghuafengc/article/details/42458721
        today = datetime.today().strftime('%m%d')
        front_url = 'https://raw.githubusercontent.com/pojiezhiyuanjun/freev2/master/'
        end_url = '.txt'
        url_update = front_url + today + end_url# 修改字符串中的某一位字符 https://www.zhihu.com/question/31800070/answer/53345749
        if url_updated(url_update):
            return [0, url_update]
        else:
            return [0, 404]
    
    def update_id_21():
        date_inurl = datetime.today().strftime('%Y/%m/%Y-%m-%d')
        #date_inurl = '2021/12/2021-12-08'
        url_update = f'https://www.mattkaydiary.com/{date_inurl}-free-v2ray-clash-nodes.html'

        if url_updated(url_update):
            resp = requests.get(url_update, timeout=5)
            raw_content = resp.text

            try:
                raw_content = raw_content.replace('amp;', '')
                #print(raw_content.find('v2ray(请开启代理后再拉取)&#65306;https://drive.google.com/uc'))
                #print(raw_content[raw_content.find('v2ray(请开启代理后再拉取)&#65306;https://drive.google.com/uc'):raw_content.find('v2ray(请开启代理后再拉取)&#65306;https://drive.google.com/uc')+100])
                pattern = re.compile(r'v2ray\(请开启代理后再拉取\)&#65306;https://drive\.google\.com/uc\?export=download&id=\w*-*\w*')
                
                url_update = re.findall(pattern, raw_content)[0][24:]
                return [21, url_update]
            except Exception as err:
                print(err)
                return [21, 404]
        else:
            return [21, 404]

    def update_id_22(): # remarks: v2raydy/v2ray, 将原链接更新至 https://https://raw.githubusercontent.com/v2raydy/v2ray/main/%MM-%(DD - 1)%str%1.txt
        yesterday = (datetime.today() + timedelta(-1)).strftime('%m-%d')# 得到当前日期前一天 https://blog.csdn.net/wanghuafengc/article/details/42458721
        
        front_url = 'https://raw.githubusercontent.com/v2raydy/v2ray/main/'
        end_url = '1.txt'
        for ch in 'abcdefghijklmnopqrstuvwxy':
            url_update = front_url + yesterday + ch + end_url# 修改字符串中的某一位字符 https://www.zhihu.com/question/31800070/answer/53345749
            if url_updated(url_update):
                return [22, url_update]
        else:
            return [22, 404]

if __name__ == '__main__':
    update_url.update_main([0,21,22])