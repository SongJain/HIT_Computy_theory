# -*- coding: utf-8 -*- 
# @Time : 2021-09-15 9:17 
# @Author : SongJian
# @File : Graph.py
from Graph_Node import Graph_Node
from Graph_Edge import Graph_Edge


class Graph:
    Edge_list = []

    start = Graph_Node()
    end = Graph_Node()

    def Graph(self):
        self.Edge_list = []

    def getEdges(self):
        return self.Edge_list

    def getStart(self):
        return self.start

    def setStart(self, start):
        self.start = start

    def getEnd(self):
        return self.end

    def setEnd(self, end):
        self.end = end

    def reset(self):
        Graph_Node.reset()

    """
    * 运算
    """

    def Star(self, obj):
        if isinstance(obj, Graph):
            self.addStar_grp(obj)
            return
        elif isinstance(obj, str):
            self.addStar_character(obj)
            return
        else:
            print(">>>正则表达式错误【Star】")
            return

    def addStar_grp(self, graph):
        beginNode = Graph_Node()
        endNode = Graph_Node()
        edge1 = Graph_Edge(beginNode, endNode, "epsilon")
        edge2 = Graph_Edge(beginNode, graph.getStart(), "epsilon")
        edge3 = Graph_Edge(graph.getEnd(), endNode, "epsilon")
        edge4 = Graph_Edge(graph.getEnd(), graph.getStart(), "epsilon")

        for i in range(len(graph.Edge_list)):
            self.Edge_list.append(graph.getEdges()[i])
        self.Edge_list.append(edge1)
        self.Edge_list.append(edge2)
        self.Edge_list.append(edge3)
        self.Edge_list.append(edge4)
        self.start = beginNode
        self.end = endNode

    def addStar_character(self, character):
        nodeCenter = Graph_Node()
        nodebegin = Graph_Node()
        nodeend = Graph_Node()
        edgelink = Graph_Edge(nodeCenter, nodeCenter, character)
        edgeEpsilonBegin = Graph_Edge(nodebegin, nodeCenter, "epsilon")
        edgeepsilonEnd = Graph_Edge(nodeCenter, nodeend, "epsilon")
        self.Edge_list.append(edgelink)
        self.Edge_list.append(edgeEpsilonBegin)
        self.Edge_list.append(edgeepsilonEnd)
        self.start = nodebegin
        self.end = nodeend

    """
    联合运算
    """

    def Union(self, obj1, obj2):
        if isinstance(obj1, str):
            if isinstance(obj2, Graph):
                self.addUnion_CandG(obj1, obj2)
                return
            elif isinstance(obj1, obj2):
                self.addUnion_CandC(obj1, obj2)
                return
        elif isinstance(obj1, Graph):
            if isinstance(obj2, Graph):
                self.addUnion_GandG(obj1, obj2)
                return
            elif isinstance(obj2, str):
                self.addUnion_GandC(obj1, obj2)
                return
        else:
            print(">>>正则表达式错误【Union】")
            return

    def addUnion_CandG(self, character, graph):
        beginNode = Graph_Node()
        endNode = Graph_Node()
        edge1 = Graph_Edge(beginNode, graph.getStart(), "epsilon")
        edge2 = Graph_Edge(graph.getEnd(), endNode, "epsilon")
        edge3 = Graph_Edge(beginNode, endNode, character)
        for index in range(graph.getEdges()):
            self.Edge_list.append(graph.getEdges()[index])
        self.Edge_list.append(edge1)
        self.Edge_list.append(edge2)
        self.Edge_list.append(edge3)
        self.start = beginNode
        self.end = endNode

    def addUnion_GandC(self, graph, character):
        beginNode = Graph_Node()
        endNode = Graph_Node()
        edge1 = Graph_Edge(beginNode, graph.getStart(), "epsilon")
        edge2 = Graph_Edge(graph.getEnd(), endNode, "epsilon")
        edge3 = Graph_Edge(beginNode, endNode, character)
        for index in range(len(graph.getEdges())):
            self.Edge_list.append(graph.getEdges()[index])
        self.Edge_list.append(edge1)
        self.Edge_list.append(edge2)
        self.Edge_list.append(edge3)
        self.start = beginNode
        self.end = endNode

    def addUnion_GandG(self, graph1, graph2):
        beginNode = Graph_Node()
        endNode = Graph_Node()
        edge1 = Graph_Edge(beginNode, graph1.getStart(), "epsilon")
        edge2 = Graph_Edge(beginNode, graph2.getStart(), "epsilon")
        edge3 = Graph_Edge(graph1.getEnd(), endNode, "epsilon")
        edge4 = Graph_Edge(graph2.getEnd(), endNode, "epsilon")
        self.start = beginNode
        for index in range(graph1.getEdges()):
            self.Edge_list.append(graph1.getEdges()[index])
        for index in range(graph2.getEdges()):
            self.Edge_list.append(graph2.getEdges()[index])

        self.Edge_list.append(edge1)
        self.Edge_list.append(edge2)
        self.Edge_list.append(edge3)
        self.Edge_list.append(edge4)

    def addUnion_CandC(self, cha1, cha2):
        biginNode = Graph_Node()
        endNode = Graph_Node()
        edge1 = Graph_Edge(biginNode, endNode, cha1)
        edge2 = Graph_Edge(biginNode, endNode, cha2)
        self.Edge_list.append(edge1)
        self.Edge_list.append(edge2)
        self.start = biginNode
        self.end = endNode

    """
    连接操作
    """
    def Concat(self, obj1, obj2):
        if isinstance(obj1, str):
            if isinstance(obj2, Graph):
                self.addConcat_CandG(obj1, obj2)
                return
            elif isinstance(obj2, str):
                self.addConcat_CandC(obj1, obj2)
        elif isinstance(obj1, Graph):
            if isinstance(obj2, Graph):
                self.addConcat_GandG(obj1, obj2)
                return
            elif isinstance(obj2, str):
                self.addConcat_GandC(obj1, obj2)
                return
        else:
            print(">>>正则表达式错误【Concat】")

    def addConcat_CandG(self, character, graph):
        beginNode = Graph_Node()
        edge = Graph_Edge(beginNode, graph.getStart(), character)
        for index in range(len(graph.getEdges())):
            self.Edge_list.append(graph.getEdges()[index])
        self.Edge_list.append(edge)
        self.start = beginNode
        self.end = graph.end

    def addConcat_GandC(self, graph, character):
        endNode = Graph_Node()
        edge = Graph_Edge(graph.getEnd(), endNode, character)
        for index in range(len(graph.getEdges())):
            self.Edge_list.append(graph.getEdges()[index])
        self.Edge_list.append(edge)
        self.start = graph.getStart()
        self.end = endNode

    def addConcat_GandG(self, graph1, graph2):
        edge = Graph_Edge(graph1.getEnd(), graph2.getStart(), "epsilon")
        for index in range(len(graph1.getEdges())):
            self.Edge_list.append(graph1.getEdges()[index])
        for index in range(len(graph2.getEdges())):
            self.Edge_list.append(graph2.getEdges()[index])
        self.Edge_list.append(edge)

    def addConcat_CandC(self, cha1, cha2):
        beginNode = Graph_Node()
        endNode = Graph_Node()
        midNode = Graph_Node()
        edge1 = Graph_Edge(beginNode, midNode, cha1)
        edge2 = Graph_Edge(midNode, endNode, cha2)
        self.start = beginNode
        self.end = endNode
        self.Edge_list.append(edge1)
        self.Edge_list.append(edge2)

    def toString(self):
        e_set = set(self.Edge_list)
        e_list = list(e_set)
        printString = "Start=" + self.start.toString() + "   End=" + self.end.toString() + "\n"
        for index in range(len(e_list)):
            printString += str(e_list[index].toString()) + "\n"
        return printString
