import re, yaml, json
import time, os

from sub_convert import sub_convert
from list_merge import sub_merge

Eterniy_file = './Eternity'
Eternity_yml_file = './Eternity.yml'
readme = './README.md'
log_file = './LogInfo.txt'

provider_path = './update/provider/'
update_path = './update/'

sub_list_json = './sub/sub_list.json'

config_file = './update/provider/config.yml'
config_global_file = './update/provider/config-global.yml'

class NoAliasDumper(yaml.SafeDumper): # https://ttl255.com/yaml-anchors-and-aliases-and-how-to-disable-them/
    def ignore_aliases(self, data):
        return True

def eternity_convert(file, config, output, provider_file_enabled=True):
    
    file_eternity = open(file, 'r', encoding='utf-8')
    sub_content = file_eternity.read()
    file_eternity.close()
    all_provider = sub_convert.main(sub_content,'content','YAML',custom_set={'dup_rm_enabled': False,'format_name_enabled': True})

    # 创建并写入 provider 
    lines = re.split(r'\n+', all_provider)
    proxy_all = []
#     us_proxy = []
#     hk_proxy = []
#     sg_proxy = []
#     others_proxy = []
    
    log_reader = open(log_file, 'r')
    log_lines = log_reader.readlines()
    log_reader.close()
    indexx = 0
    for line in lines:
        if line != 'proxies:':
            #####
            print(line)
            line_json = json.loads(line.replace('\n', '').replace('- ', ''))
            server_name = line_json["name"]
            server_type = line_json["type"]
            log_lines[indexx] = "name: %s | type: %s | %s" % (server_name, server_type, line)
            indexx += 1
            #####
            line = '  ' + line
            proxy_all.append(line)

    #####
    log_writer = open(log_file, 'w')
    log_writer.writelines(log_lines)
    log_writer.close()
    #####
    
    if provider_file_enabled:
        providers_files = {
            'all': provider_path + 'provider-all.yml',
#             'others': provider_path + 'provider-others.yml',
#             'us': provider_path + 'provider-us.yml',
#             'hk': provider_path + 'provider-hk.yml',
#             'sg': provider_path + 'provider-sg.yml'
        }
        eternity_providers = {
            'all': all_provider,
#             'others': others_provider,
#             'us': us_provider,
#             'hk': hk_provider,
#             'sg': sg_provider
        }
        print('Writing content to provider')
        for key in providers_files.keys():
            provider_all = open(providers_files[key], 'w', encoding= 'utf-8')
            provider_all.write(eternity_providers[key])
            provider_all.close()
        print('Done!\n')

    # 创建完全配置的Eternity.yml
    config_f = open(config_file, 'r', encoding='utf-8')
    config_raw = config_f.read()
    config_f.close()
    
    config = yaml.safe_load(config_raw)

    all_provider_dic = {'proxies': []}
#     others_provider_dic = {'proxies': []}
#     us_provider_dic = {'proxies': []}
#     hk_provider_dic = {'proxies': []}
#     sg_provider_dic = {'proxies': []}
    provider_dic = {
        'all': all_provider_dic,
#         'others': others_provider_dic,
#         'us': us_provider_dic,
#         'hk': hk_provider_dic,
#         'sg': sg_provider_dic
    }
    for key in eternity_providers.keys(): # 将节点转换为字典形式
        provider_load = yaml.safe_load(eternity_providers[key])
        provider_dic[key].update(provider_load)

    # 创建节点名列表
    all_name = []
#     others_name = []
#     us_name = []
#     hk_name = []
#     sg_name = [] 
    name_dict = {
        'all': all_name,
#         'others': others_name,
#         'us': us_name,
#         'hk': hk_name,
#         'sg': sg_name
    }
    for key in provider_dic.keys():
        if not provider_dic[key]['proxies'] is None:
            for proxy in provider_dic[key]['proxies']:
                name_dict[key].append(proxy['name'])
        if provider_dic[key]['proxies'] is None:
            name_dict[key].append('DIRECT')
    # 策略分组添加节点名
    proxy_groups = config['proxy-groups']
    proxy_group_fill = []
    for rule in proxy_groups:
        if rule['proxies'] is None: # 不是空集加入待加入名称列表
            proxy_group_fill.append(rule['name'])
    for rule_name in proxy_group_fill:
        for rule in proxy_groups:
            if rule['name'] == rule_name:
#                 if '美国' in rule_name:
#                     rule.update({'proxies': us_name})
#                 elif '香港' in rule_name:
#                     rule.update({'proxies': hk_name})
#                 elif '狮城' in rule_name or '新加坡' in rule_name:
#                     rule.update({'proxies': sg_name})
#                 elif '其他' in rule_name:
#                     rule.update({'proxies': others_name})
#                 else:
                if "Main Group" in rule_name:
                    rule.update({'proxies': all_name})
    config.update(all_provider_dic)
    config.update({'proxy-groups': proxy_groups})

    """
    yaml_format = ruamel.yaml.YAML() # https://www.coder.work/article/4975478
    yaml_format.indent(mapping=2, sequence=4, offset=2)
    config_yaml = yaml_format.dump(config, sys.stdout)
    """
    config_yaml = yaml.dump(config, default_flow_style=False, sort_keys=False, allow_unicode=True, width=750, indent=2, Dumper=NoAliasDumper)
    
    Eternity_yml = open(output, 'w+', encoding='utf-8')
    Eternity_yml.write(config_yaml)
    Eternity_yml.close()

def backup(file):
    t = time.localtime()
    date = time.strftime('%y%m', t)
    date_day = time.strftime('%y%m%d', t)

    file_eternity = open(file, 'r', encoding='utf-8')
    sub_content = file_eternity.read()
    file_eternity.close()

    try:
        os.mkdir(f'{update_path}{date}')
    except FileExistsError:
        pass
    txt_dir = update_path + date + '/' + date_day + '.txt' # 生成$MM$DD.txt文件名
    file = open(txt_dir, 'w', encoding= 'utf-8')
    file.write(sub_convert.base64_decode(sub_content))
    file.close()

if __name__ == '__main__':
    sub_merge.geoip_update('https://raw.githubusercontent.com/Loyalsoldier/geoip/release/Country.mmdb')
    eternity_convert(Eterniy_file, config_file, output=Eternity_yml_file)
    backup(Eterniy_file)
    sub_merge.readme_update(readme,sub_merge.read_list(sub_list_json))
