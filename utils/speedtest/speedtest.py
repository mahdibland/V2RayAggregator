import json, base64

out_json = './out.json'

def read_json(file): # 将 out.json 内容读取为列表
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

if __name__ == '__main__':
    output(read_json(out_json),99)