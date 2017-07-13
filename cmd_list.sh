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
2. [cmd_zz_proto.sh] protoc生成pb{h,m}文件更新到项目中
"


cmd_index=$1
echo "${blue}请输入执行脚本序号：${reset}"
read cmd_index
if [ $cmd_index -eq 1 ]; then
    bash $cmd_path/cmd_zz_proto.sh
elif [ $cmd_index -eq 2 ]; then
    bash $cmd_path/cmd_zz_proto.sh
else
    echo "请输入正确的序号"
fi
