import re

from sub_convert import sub_convert

Eterniy = './Eternity'

def eternity_convert():
    file_eternity = open(Eterniy, 'r', encoding='utf-8')
    sub_content = file_eternity.read()
    eternity_convert = sub_convert.convert(sub_content,'content','YAML', False)
    file_eternity.close()

    eternity_yml = open('Eternity.yml', 'w', encoding= 'utf-8')
    eternity_yml.write(eternity_convert)
    eternity_yml.close()
    
    providers_files = {
        'all': './update/provider/eternity-all.yml',
        'others': './update/provider/eternity-others.yml',
        'us': './update/provider/eternity-us.yml',
        'hk': './update/provider/eternity-hk.yml',
        'sg': './update/provider/eternity-sg.yml'
    }

    lines = re.split(r'\n+', eternity_convert)
    us_proxy = []
    hk_proxy = []
    sg_proxy = []
    others_proxy = []
    for line in lines:
        if 'US' in line or '美国' in line:
            us_proxy.append(line)
        elif 'HK' in line or '香港' in line:
            hk_proxy.append(line)
        elif 'SG' in line or '新加坡' in line:
            sg_proxy.append(line)
        else:
            others_proxy.append(line)
    us_proxy = 'proxies:\n' + '\n'.join(us_proxy)
    hk_proxy = 'proxies:\n' + '\n'.join(hk_proxy)
    sg_proxy = 'proxies:\n' + '\n'.join(sg_proxy)
    others_proxy = 'proxies:\n' + '\n'.join(others_proxy)

    eternity_providers = {
        'all': eternity_convert,
        'others': others_proxy,
        'us': us_proxy,
        'hk': hk_proxy,
        'sg': sg_proxy
    }
    for key in providers_files.keys():
        provider_all = open(providers_files[key], 'w', encoding= 'utf-8')
        provider_all.write(eternity_providers[key])
        provider_all.close()

convert = eternity_convert()