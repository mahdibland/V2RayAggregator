import re
import yaml
import json
import re
import time
import os

from sub_convert import sub_convert
# below is replacement of above
from subs_function import subs_function

from list_merge import sub_merge

Eterniy_base_file = './EternityBase'
Eterniy_file = './Eternity'
Eternity_yml_file = './Eternity.yml'
readme = './README.md'
log_file = './LogInfo.txt'

provider_path = './update/provider/'
update_path = './update/'

sub_list_json = './sub/sub_list.json'

config_file = './update/provider/config.yml'
config_global_file = './update/provider/config-global.yml'


# https://ttl255.com/yaml-anchors-and-aliases-and-how-to-disable-them/
class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def substrings(string, left, right):
    value = string.replace('\n', '').replace(' ', '')
    start = value.index(left)
    end = value[start:].index(
        right) + (value.__len__() - value[start:].__len__())
    final_value = value[start:end].replace(left, '')
    return final_value


def eternity_convert(file, config, output, provider_file_enabled=True):
    # # no conversion from base64 so udp is not a problem
    # subconvertor not working with only proxy url
    all_provider = subs_function.convert_sub(
        "https://raw.githubusercontent.com/mahdibland/SSAggregator/master/sub/sub_merge_base64.txt", 'clash', "http://0.0.0.0:25500", False, extra_options="&udp=false")

    ##########   Add Name to Logs Before making chaages to Proxies  ############
    temp_providers = all_provider.split('\n')
    log_reader = open(log_file, 'r')
    log_lines = log_reader.readlines()
    log_reader.close()
    indexx = 0
    for line in temp_providers:
        if line != 'proxies:':
            try:
                #####
                server_name = substrings(line, "name:", ",")
                server_type = substrings(line, "type:", ",")
                log_lines[indexx] = "name: %s | type: %s | %s" % (
                    server_name, server_type, log_lines[indexx])
                #####
                indexx += 1
            except:
                print("log lines length != providers length")

    log_writer = open(log_file, 'w')
    log_writer.writelines(log_lines)
    log_writer.close()
    ############################################################################

    # remove lines with name issue
    removed_bad_char = list(filter(lambda x: str(x).__contains__(
        "�") == False, all_provider.split("\n")[1:]))
    log_lines_without_bad_char = list(filter(lambda x: str(x).__contains__(
        "�") == False, log_lines))

    # make sure the size of two list are equal
    print(
        f"removed_bad_char count => {removed_bad_char.__len__()} & log_lines_without_bad_char count => {log_lines_without_bad_char.__len__()}")

    # take a part from begining of all lines
    num = 200
    num = removed_bad_char.__len__() if removed_bad_char.__len__() <= num else num

    # convert the safe partition to yaml format
    all_provider = "proxies:\n" + "\n".join(removed_bad_char[0:num + 1])

    lines = re.split(r'\n+', all_provider)

    proxy_all = []
    #     us_proxy = []
    #     hk_proxy = []
    #     sg_proxy = []
    #     others_proxy = []
    indexx = 0
    for line in lines:
        if line != 'proxies:':
            try:
                name = substrings(line, "name:", ",")
                speed = substrings(
                    log_lines_without_bad_char[indexx], "avg_speed:", "|")
                line = re.sub("name:( |)(.*?),", "name: %s | %s," %
                              (name, speed), line)
            except:
                print(log_lines_without_bad_char[indexx])
                pass
            #           line = '  ' + line
            line = line.replace('- ', '')
            linee = yaml.safe_load(line)
            proxy_all.append(linee)

            indexx += 1

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
            provider_all = open(providers_files[key], 'w', encoding='utf-8')
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
    for key in eternity_providers.keys():  # 将节点转换为字典形式
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

    indexx = 0
    for key in provider_dic.keys():
        if not provider_dic[key]['proxies'] is None:
            for proxy in provider_dic[key]['proxies']:
                try:
                    speed = substrings(
                        log_lines_without_bad_char[indexx], "avg_speed:", "|")
                    name_dict[key].append(
                        str(proxy['name']).replace(" ", "") + " | " + speed)
                except:
                    name_dict[key].append(str(proxy['name']).replace(" ", ""))
                    print(log_lines_without_bad_char[indexx])

                indexx += 1

        if provider_dic[key]['proxies'] is None:
            name_dict[key].append('DIRECT')
    # 策略分组添加节点名
    proxy_groups = config['proxy-groups']
    proxy_group_fill = []
    for rule in proxy_groups:
        if rule['proxies'] is None:  # 不是空集加入待加入名称列表
            proxy_group_fill.append(rule['name'])

    full_size = all_name.__len__()
    part_size = int(full_size / 4)
    last_size = full_size - (part_size * 3)
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
                # todo it changes from Main group to tier names
                if "Tier 1" in rule_name:
                    rule.update({'proxies': all_name[0:part_size]})
                elif "Tier 2" in rule_name:
                    rule.update({'proxies': all_name[part_size:part_size*2]})
                elif "Tier 3" in rule_name:
                    rule.update({'proxies': all_name[part_size*2:part_size*3]})
                elif "Tier 4" in rule_name:
                    rule.update({'proxies': all_name[part_size*3:full_size]})

    config.update(all_provider_dic)
    config.update({'proxy-groups': proxy_groups})
    config.update({'proxies': proxy_all})

    """
    yaml_format = ruamel.yaml.YAML() # https://www.coder.work/article/4975478
    yaml_format.indent(mapping=2, sequence=4, offset=2)
    config_yaml = yaml_format.dump(config, sys.stdout)
    """
    config_yaml = yaml.dump(config, default_flow_style=False, sort_keys=False,
                            allow_unicode=True, width=750, indent=2, Dumper=NoAliasDumper)

    Eternity_yml = open(output, 'w+', encoding='utf-8')
    Eternity_yml.write(config_yaml)
    Eternity_yml.close()


def backup(file):
    try:
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
        txt_dir = update_path + date + '/' + date_day + '.txt'  # 生成$MM$DD.txt文件名
        file = open(txt_dir, 'w', encoding='utf-8')
        file.write(sub_convert.base64_decode(sub_content))
        file.close()
    except Exception as e:
        print("Error While backup EterniyBase_file => if you use method yaml ignore this")


if __name__ == '__main__':
    sub_merge.geoip_update(
        'https://raw.githubusercontent.com/Loyalsoldier/geoip/release/Country.mmdb')
    eternity_convert(Eterniy_file, config_file, output=Eternity_yml_file)
    backup(Eterniy_file)
    sub_merge.readme_update(readme, sub_merge.read_list(sub_list_json))
