import re, yaml

from sub_convert import sub_convert

Eterniy_file = './Eternity'
Eternity_yml_file = './Eternity.yml'

provider_path = './update/provider/'

config_file = './update/provider/config.yml'
config_global_file = './update/provider/config-global.yml'

class NoAliasDumper(yaml.SafeDumper): # https://ttl255.com/yaml-anchors-and-aliases-and-how-to-disable-them/
    def ignore_aliases(self, data):
        return True

def eternity_convert(content, config, output, provider_file_enabled=True):
    try:
        file_eternity = open(content, 'r', encoding='utf-8')
        sub_content = file_eternity.read()
        file_eternity.close()
    except Exception as err:
        print(err)
        sub_content = content
    all_provider = sub_convert.convert(sub_content,'content','YAML')

    # 创建并写入 provider 
    lines = re.split(r'\n+', all_provider)
    proxy_all = []
    us_proxy = []
    hk_proxy = []
    sg_proxy = []
    others_proxy = []
    for line in lines:
        if line != 'proxies:':
            line = '  ' + line
            proxy_all.append(line)

            if 'US' in line or '美国' in line:
                us_proxy.append(line)
            elif 'HK' in line or '香港' in line:
                hk_proxy.append(line)
            elif 'SG' in line or '新加坡' in line:
                 sg_proxy.append(line)
            else:
                others_proxy.append(line)
    us_provider = 'proxies:\n' + '\n'.join(us_proxy)
    hk_provider = 'proxies:\n' + '\n'.join(hk_proxy)
    sg_provider = 'proxies:\n' + '\n'.join(sg_proxy)
    others_provider = 'proxies:\n' + '\n'.join(others_proxy)
    
    if provider_file_enabled:
        providers_files = {
            'all': provider_path + 'provider-all.yml',
            'others': provider_path + 'provider-others.yml',
            'us': provider_path + 'provider-us.yml',
            'hk': provider_path + 'provider-hk.yml',
            'sg': provider_path + 'provider-sg.yml'
        }
        eternity_providers = {
            'all': all_provider,
            'others': others_provider,
            'us': us_provider,
            'hk': hk_provider,
            'sg': sg_provider
        }
        print('Writing content to provider')
        for key in providers_files.keys():
            provider_all = open(providers_files[key], 'w', encoding= 'utf-8')
            provider_all.write(eternity_providers[key])
            provider_all.close()
        print('Done!')

    # 创建完全配置的Eternity.yml
    config_f = open(config_file, 'r', encoding='utf-8')
    config_raw = config_f.read()
    config_f.close()
    
    config = yaml.safe_load(config_raw)

    all_provider_dic = {'proxies': []}
    others_provider_dic = {'proxies': []}
    us_provider_dic = {'proxies': []}
    hk_provider_dic = {'proxies': []}
    sg_provider_dic = {'proxies': []}
    provider_dic = {
        'all': all_provider_dic,
        'others': others_provider_dic,
        'us': us_provider_dic,
        'hk': hk_provider_dic,
        'sg': sg_provider_dic
    }
    for key in eternity_providers.keys(): # 将节点转换为字典形式
        provider_load = yaml.safe_load(eternity_providers[key])
        provider_dic[key].update(provider_load)

    # 创建节点名列表
    all_name = []
    others_name = []
    us_name = []
    hk_name = []
    sg_name = [] 
    name_dict = {
        'all': all_name,
        'others': others_name,
        'us': us_name,
        'hk': hk_name,
        'sg': sg_name
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
                if '美国' in rule_name:
                    rule.update({'proxies': us_name})
                elif '香港' in rule_name:
                    rule.update({'proxies': hk_name})
                elif '狮城' in rule_name or '新加坡' in rule_name:
                    rule.update({'proxies': sg_name})
                elif '其他' in rule_name:
                    rule.update({'proxies': others_name})
                else:
                    rule.update({'proxies': all_name})
    config.update(all_provider_dic)
    config.update({'proxy-groups': proxy_groups})

    """
    yaml_format = ruamel.yaml.YAML() # https://www.coder.work/article/4975478
    yaml_format.indent(mapping=2, sequence=4, offset=2)
    config_yaml = yaml_format.dump(config, sys.stdout)
    """
    config_yaml = yaml.dump(config, default_flow_style=False, sort_keys=False, allow_unicode=True, width=750, indent=2, Dumper=NoAliasDumper)
    
    Eternity_yml = open(output, 'w', encoding='utf-8')
    Eternity_yml.write(config_yaml)
    Eternity_yml.close()

convert = eternity_convert(Eterniy_file, config_file, output=Eternity_yml_file)
convert = eternity_convert(Eterniy_file, config_global_file, output='./update/provider/eternity-global.yml')