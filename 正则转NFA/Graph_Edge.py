# -*- coding: utf-8 -*- 
# @Time : 2021-09-14 22:21 
# @Author : SongJian
# @File : Graph_Edge.py

class Graph_Edge:

    def __init__(self, begin, end, label):
        self.begin = begin
        self.end = end
        self.label = label

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getBegin(self):
        return self.begin

    def setBegin(self, begin):
        self.begin = begin

    def getEnd(self):
        return self.end

    def setEnd(self, end):
        self.end = end

    def toString(self):
        return "Edge [begin=" + self.begin.toString() + ", end=" + self.end.toString() + ", label=" + self.label + "]"