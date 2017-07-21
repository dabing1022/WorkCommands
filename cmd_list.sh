#!/bin/bash
export LANG="zh_CN.UTF-8"

cmd_path='/Users/ChildhoddAndy/Documents/ChildhoodAndy/work_commands'

black=`tput setaf 0`
red=`tput setaf 1`
green=`tput setaf 2`
yellow=`tput setaf 3`
blue=`tput setaf 4`
magenta=`tput setaf 5`
cyan=`tput setaf 6`
white=`tput setaf 7`
reset=`tput sgr0`

timestamp=`date "+%Y.%m.%d  %H:%M:%S"`
echo "${green}${timestamp}${reset}"

echo "
1. [cmd_zz_proto.sh] protoc生成pb{h,m}文件更新到项目中
2. [urlencode.py] url encode编码
3. [urldecode.py] url decode解码
"


cmd_index=$1
echo "${blue}请输入执行脚本序号：${reset}"
read cmd_index
if [ $cmd_index -eq 1 ]; then
    bash $cmd_path/cmd_zz_proto.sh
elif [ $cmd_index -eq 2 ]; then
    echo "${blue}请输入要编码的字符串：${reset}"
    read url_data
    python $cmd_path/urlencode.py $url_data
elif [ $cmd_index -eq 3 ]; then
    echo "${blue}请输入要解码的字符串：${reset}"
    read url_data
    python $cmd_path/urldecode.py $url_data
else
    echo "请输入正确的序号"
fi
