# -*- coding: utf-8 -*- 
# @Time : 2021-09-14 22:00 
# @Author : SongJian
# @File : RL_to_NFA.py
from Stack import Stack
from Graph_Node import Graph_Node
from Graph import Graph


class Regex:

    regex = ""
    operatorStack = Stack()
    operandStack = Stack()
    """ 分别是 * & | ()  # 的优先级 """
    priority = [[1, 1, 1, -1, 1, 1], [-1, 1, 1, -1, 1, 1],
                [-1, -1, 1, -1, 1, 1], [-1, -1, -1, -1, 0, 2],
                [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]]

    def __init__(self, pre_regex):
        self.regex = self.prepare_RL(pre_regex)
        self.operandStack = Stack()
        self.operatorStack = Stack()

    def Regex(self, pre_regex):
        self.regex = self.prepare_RL(pre_regex)
        self.operandStack = Stack()
        self.operatorStack = Stack()

    """
    先对正则表达式进行预处理
    """
    def prepare_RL(self, regular_Language):
        prepared_rl = ""
        regular_Language.replace(" ", "")
        for index in range(len(regular_Language)):
            if index == 0:
                prepared_rl += regular_Language[index]
            else:
                if (regular_Language[index] == '|') or (regular_Language[index] == '*') or (
                        regular_Language[index] == ')'):
                    prepared_rl += regular_Language[index]
                else:
                    if (regular_Language[index - 1] == '(') or (regular_Language[index - 1] == '|'):
                        prepared_rl += regular_Language[index]
                    else:
                        prepared_rl += ("&" + regular_Language[index])
        return prepared_rl

    """
    判断是否是符号
    """
    def isOperator(self, op):
        ops = "*&|()#"
        return op in ops

    """
    判断操作符的优先级，根据行列，从priority二维数组中取值
    """
    def priorityOperator(self, character1, character2):
        priorityString = "*&|()#"
        return self.priority[priorityString.index(character1)][priorityString.index(character2)]

    """
    转换代码，将Regex转化为NFA
    """
    def transforNFA(self):
        if len(self.regex) == 0:
            return None
        else:
            index = 0
            self.operatorStack.push('#')
            self.regex += "#"
            while self.regex[index] != '#' or self.operatorStack.peek() != '#':
                if self.isOperator(self.regex[index]) == False:
                    # 如果当前index下的字符是一个数，则压入operandStack
                    self.operandStack.push(self.regex[index])
                    index += 1
                else:
                    # 如果当前index下的字符是一个符号
                    # 先比较当前操作符与操作符栈顶的操作符的优先级
                    value = self.priorityOperator(self.operatorStack.peek(), self.regex[index])
                    if value == 1:
                        character = self.operatorStack.pop()
                        if character == '*':
                            obj = self.operandStack.pop()
                            graph1 = Graph()
                            graph1.Star(obj)
                            self.operandStack.push(graph1)
                        elif character == '&':
                            obj2 = self.operandStack.pop()
                            obj1 = self.operandStack.pop()
                            graph2 = Graph()
                            graph2.Concat(obj1, obj2)
                            self.operandStack.push(graph2)
                        elif character == '|':
                            obj4 = self.operandStack.pop()
                            obj3 = self.operandStack.pop()
                            graph3 = Graph()
                            graph3.Union(obj3, obj4)
                            self.operandStack.push(graph3)
                    elif value == 0:
                        self.operatorStack.pop()
                        index += 1
                    elif value == -1:
                        self.operatorStack.push(self.regex[index])
                        index += 1
        return self.operandStack.pop()

    def reset(self):
        Graph_Node().reset()
        self.operatorStack.clear()
        self.operandStack.clear()

    def getregex(self):
        return self.regex

    def setregex(self, re):
        self.prepare_RL(re)