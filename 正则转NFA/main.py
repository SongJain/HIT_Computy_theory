# -*- coding: utf-8 -*- 
# @Time : 2021-09-15 8:10 
# @Author : SongJian
# @File : main.py
from Stack import Stack
from RL_to_NFA import Regex
from Graph import Graph

if __name__ == "__main__":
    regexString1 = "(ab|c)*abb"
    strr = Regex(regexString1)
    g = strr.transforNFA()
    print("正则表达式转换后："+strr.regex)
    print(g.toString())
    strr.reset()



