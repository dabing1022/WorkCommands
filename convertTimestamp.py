# coding:utf-8

'''
乐高上报文件增加可读性时间一列
'''

import re
import sys
from datetime import datetime
from code import InteractiveConsole
from os import path

source_file_path = "test.txt"

def convertProcess(file_path):
    with open(file_path) as f:
        line_no = 0
        file_content = ""
        for line in f:
            arr = re.split("\t", line)
            timestamp = arr[5]
            if line_no == 0:
                arr.insert(6, "t_zzlego_action.date")
            else:
                dateStr = datetime.fromtimestamp(int(timestamp) / 1000).strftime('%Y-%m-%d %H:%M:%S')
                arr.insert(6, dateStr)
            line_no += 1
            file_content += '\t'.join(arr)

        save(file_content, file_path)

def save(file_content, source_file_path):
    file_name_arr = source_file_path.split(".")
    new_file_name = source_file_path[0] + "_date" + "." + source_file_path[-1]
    dir_name = path.dirname(source_file_path)
    saving_path = path.join(dir_name, new_file_name)

    with open(saving_path, "w") as f:
        f.write(file_content)


if __name__ == "__main__":
    convertProcess(source_file_path)
