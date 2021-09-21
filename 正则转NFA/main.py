# -*- coding: utf-8 -*- 
# @Time : 2021-09-15 8:10 
# @Author : SongJian
# @File : main.py
from Stack import Stack
from RL_to_NFA import Regex
from Graph import Graph

if __name__ == "__main__":
    # 打开文件对象
    file = open('re_express.txt', 'r')
    regexString = file.read()
    strr = Regex(regexString)
    print("文件读取的正则表达式：" + regexString)
    print("正则表达式转换后：" + strr.regex)
    g = strr.transforNFA()
    print(g.toString())
    strr.reset()



