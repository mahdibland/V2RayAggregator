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
    arred = lambda x,n : x*(10**n)//1/(10**n)
    print(str(list[0]))
    output_list = []
    for item in list:
        info = "id: %s | remarks: %s | protocol: %s | ping: %s | avg_speed: %s | max_speed: %s | Link: %s" % (str(item["id"]), item["remarks"], item["protocol"], str(item["ping"]), str(arred(item["avg_speed"] * 0.00000095367432, 3)), str(arred(item["max_speed"] * 0.00000095367432, 3)), item["Link"])
        output_list.append(info)
    with open('./LogInfo.txt', 'w') as f1:
        f1.writelines(output_list)
        f1.close()
        print('Write Log Success!')
        
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

if __name__ == '__main__':
    output(read_json(out_json),200)
