# -*- coding: utf-8 -*- 
# @Time : 2021-09-15 7:42 
# @Author : SongJian
# @File : Stack.py
class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, data):
        """
        进栈函数
        """
        self.stack.append(data)

    def pop(self):
        """
        出栈函数，
        """
        return self.stack.pop()

    def peek(self):
        """
        取栈顶
        """
        return self.stack[-1]

    def clear(self):
        """
        清空栈
        """
        while len(self.stack) > 0:
            self.stack.pop()