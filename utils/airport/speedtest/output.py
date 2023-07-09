import json
import base64
import os
import time

out_json = './output.json'

Eternity_Air = "./EternityAir"
airport_all_base64 = "./sub/airport_merge_base64.txt"
sub_all = "./sub/airport_sub_merge.txt"
Eternity_Air_file = "./EternityAir.txt"


def read_json(file):  # 将 output.json 内容读取为列表
    while os.path.isfile(file) == False:
        print('Awaiting speedtest complete')
        time.sleep(30)
    with open(file, 'r', encoding='utf-8') as f:
        print('Reading output.json')
        proxies_all = json.load(f)["nodes"]
        f.close()
    return proxies_all


def output(list, num):
    # sort base their avg speed rather than max speed which is default option
    list = sorted(list, key=lambda x: x['avg_speed'], reverse=True)

    def arred(x, n): return x*(10**n)//1/(10**n)
    print(str(list[0]))
    output_list = []
    for item in list:
        info = "id: %s | remarks: %s | protocol: %s | ping: %s MS | avg_speed: %s MB | max_speed: %s MB | Link: %s\n" % (str(item["id"]), item["remarks"], item["protocol"], str(
            item["ping"]), str(arred(item["avg_speed"] * 0.00000095367432, 3)), str(arred(item["max_speed"] * 0.00000095367432, 3)), item["link"])

        # if str(arred(item["avg_speed"] * 0.00000095367432, 3)) != "0.0" and str(arred(item["avg_speed"] * 0.00000095367432, 3)) != "0.00":
        output_list.append(info)
    with open('./LogInfoAir.txt', 'w') as f1:
        f1.writelines(output_list)
        f1.close()
        print('Write Log Success!')

    output_list = []
    for index in range(list.__len__()):
        proxy = list[index]['link']
        output_list.append(proxy)

    content = '\n'.join(output_list)
    content_base64 = base64.b64encode(
        '\n'.join(output_list).encode('utf-8')).decode('ascii')
    content_base64_part = base64.b64encode(
        '\n'.join(output_list[0:num]).encode('utf-8')).decode('ascii')

    with open(sub_all, 'w') as f:
        f.write(content)
        print('Write All Urls Success!')
        f.close()
    with open(airport_all_base64, 'w+', encoding='utf-8') as f:
        f.write(content_base64)
        print('Write All Base64 Success!')
        f.close()
    with open(Eternity_Air, 'w+', encoding='utf-8') as f:
        f.write(content_base64_part)
        print('Write Part Base64 Success!')
        f.close()

    with open(Eternity_Air_file, 'w') as f:
        f.write('\n'.join(output_list[0:num]))
        print('Write Part Base Success!')
        f.close()

    return content


if __name__ == '__main__':
    num = 200
    if os.path.isfile(out_json):
        os.unlink(out_json)
    value = read_json(out_json)
    output(value, value.__len__() if value.__len__() <= num else num)
