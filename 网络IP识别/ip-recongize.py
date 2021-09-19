# -*- coding: utf-8 -*- 
# @Time : 2021-09-11 15:23 
# @Author : SongJian
# @File : ip-recongize.py

import re
"""
使用正则化库去识别IP地址的合法性
IP地址有两种，IPv4和IPv6
IPv4:(0-255).(0-255).(0-255).(0-255)
        ^:          不接受除方括号外的其他输入
        1-99:       [1-9]?\d
        100-199:    1\d{2}
        200-249:    2[0-4]\d
        250-255:    25[0-5]
IPv6:十六进制表示法：xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx
     每段中前面的0可以省略
     任何十六进制数：   0-9A-Fa-f
     
"""

## 判定函数
def Is_ipv4_address(input):
    ## IPv4 的正则表达式
    re_Ipv4 = "^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$"
    re_ip = re.compile(re_Ipv4)
    if re_ip.match(input):
        return True
    else:
        return False

def Is_ipv6_address(input):
    ## IPv6 的正则表达式
    re_Ipv6 = "^([\da-fA-F]{1,4}:){7}[\da-fA-F]{1,4}$"
    re_ip = re.compile(re_Ipv6, re.IGNORECASE)
    if re_ip.match(input):
        return True
    else:
        return False

if __name__ == '__main__':
    while 1:
        add = input(">>>请输入ip地址(按q退出)：")
        if add == 'q':
            break
        ans = Is_ipv4_address(add)
        ans1 = Is_ipv6_address(add)
        if ans:
            print(">>>合法IPv4！\n")
        else:
            if ans1:
                print(">>>合法IPv6！\n")
            else:
                print(">>>错误IP，请修改！\n")