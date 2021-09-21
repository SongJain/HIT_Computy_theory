# -*- coding: utf-8 -*- 
# @Time : 2021-09-14 22:12 
# @Author : SongJian
# @File : Graph_Node.py
ID = -2
class Graph_Node:
    node_id = 0
    def __init__(self):
        global ID
        self.node_id = ID
        ID += 1

    def getID(self):
        return self.node_id

    def reset(self):
        global ID
        ID = 0

    def toString(self):
        return str(self.node_id) + ""

