# coding:utf-8

import re
import json
import csv

source_file = "sendPackageFail.txt"
pv_key = "PV"
uv_key = "UV"
pv_rate_key = "PV PERCENT"
uv_rate_key = "UV PERCENT"
line_no = 0

total_pv = 0
total_uv_map = {}
subcmd_list_count = {}
subcmd_uv_list = {}

def get_pretty_print(dictionary):
    dumps = json.dumps(dictionary)
    json_obj = json.loads(dumps)
    return json.dumps(json_obj, sort_keys=True, indent=4, separators=(',', ': '))

def increase_pv_count(dictionary, key):
    if key not in dictionary:
        dictionary[key] = 0
    dictionary[key] = dictionary[key] + 1

def increase_uv_count(dictionary, unique_key, key, judgeKey):
    if key not in dictionary:
        dictionary[key] = 0

    if unique_key not in subcmd_uv_list:
        subcmd_uv_list[unique_key] = []
    if judgeKey not in subcmd_uv_list[unique_key]:
        dictionary[key] = dictionary[key] + 1
        subcmd_uv_list[unique_key].append(judgeKey)

def parseline(line_content):
    global total_pv
    subcmd_match = re.search(r'(\d*).*"subcmd":"(\w*)".*"code":"(-?\d*)"', line_content)
    if subcmd_match:
        uid = subcmd_match.group(1)
        subcmd_name = subcmd_match.group(2)
        code = subcmd_match.group(3)
        code_key = "code_" + str(code)
        if len(subcmd_name) == 0:
            subcmd_name = "UnKnown"

        total_pv = total_pv + 1
        if str(uid) not in total_uv_map:
            if uv_key not in total_uv_map:
                total_uv_map[uv_key] = 0
            total_uv_map[uv_key] = total_uv_map[uv_key] + 1
            total_uv_map[str(uid)] = True

        if subcmd_name not in subcmd_list_count:
            subcmd_list_count[subcmd_name] = {}
        if code_key not in subcmd_list_count[subcmd_name]:
            subcmd_list_count[subcmd_name][code_key] = {}

        increase_pv_count(subcmd_list_count[subcmd_name], pv_key)
        increase_uv_count(subcmd_list_count[subcmd_name], subcmd_name + uv_key + str(uid), uv_key, uv_key + str(uid))

        increase_pv_count(subcmd_list_count[subcmd_name][code_key], pv_key)
        increase_uv_count(subcmd_list_count[subcmd_name][code_key], subcmd_name + code_key + uv_key + str(uid), uv_key, uv_key + str(uid))

def exportToExcel():
    with open('sendPackageFail.csv', 'w') as csvfile:
        fieldnames = ['api', 'code', 'pv', 'percent', 'uv', 'percent']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for (key1, value1) in subcmd_list_count.items():
            if isinstance(value1, dict):
                for (key2, value2) in value1.items():
                    if isinstance(value2, dict):
                        writer.writerow({'api': key1, 'code': re.split("_", key2)[-1], 'pv': str(value2[pv_key]), 'percent': str(value2[pv_rate_key]), 'uv': str(value2[uv_key]), 'percent': str(value2[uv_rate_key])})

with open(source_file) as f:
    for line in f:
        line_no = line_no + 1
        parseline(line)

for (key1, value1) in subcmd_list_count.items():
    if isinstance(value1, dict):
        value1[pv_rate_key] = '%.2f%%'% (value1[pv_key] / total_pv * 100)
        value1[uv_rate_key] = '%.2f%%'% (value1[uv_key] / total_uv_map[uv_key] * 100)
        for (key2, value2) in value1.items():
            if isinstance(value2, dict):
                value2[pv_rate_key] = '%.2f%%'% (value2[pv_key] / total_pv * 100)
                value2[uv_rate_key] = '%.2f%%'% (value2[uv_key] / total_uv_map[uv_key] * 100)



print(u"Failed pv: %d, uv: %d" % (total_pv, total_uv_map[uv_key]))
print(get_pretty_print(subcmd_list_count))
exportToExcel()
