import json, base64, os, time

out_json = './out.json'

def read_json(file): # 将 out.json 内容读取为列表
    while os.path.isfile(file)==False:
        print('Awaiting speedtest complete')
        time.sleep(30)
    with open(file, 'r', encoding='utf-8') as f:
        print('Reading out.json')
        proxies_all = json.load(f)
        f.close()
    return proxies_all

def output(list,num):
    output_list = []
    for index in range(num):
        proxy = list[index]['Link']
        output_list.append(proxy)
    content = base64.b64encode('\n'.join(output_list).encode('utf-8')).decode('ascii')
    with open('./Eternity', 'w+', encoding='utf-8') as f:
        f.write(content)
        print('Write Success!')
        f.close()
    return content

def info(list):
    output_list = []
    for item in list:
#         info = "ping: " + str(item["ping"]) + " | speed: " + str(item["speed"]) + " | maxspeed: " + str(item["maxspeed"]) + "proxy: " + item['Link']
#         output_list.append(info)
        output_list.append(str(item) + "\n")
    with open('./LogInfo.txt', 'w') as f:
        f.writelines(output_list)
        print('Write Log Success!')
        f.close()
    return true

if __name__ == '__main__':
    output(read_json(out_json),200)
    info(read_json(out_json))
