#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Derek on 2021/10/26
"""
-------------------------------------------------
File Name :  main
Description : A file to review python3 basics according to my personal level: n+1
Author : derek
Email : derek_simon@outlook.com
-------------------------------------------------
Change Activity:
    2021/10/26: create
-------------------------------------------------
"""


__author__ = 'derek'


def print_hi(name):
    # first method
    print(f'Hi, {name}')


def exam_data_types():
    # string, integer, float, boolean, dictionary, tuple, list, set
    # common operations: index, slicing
    pass


def exam_range():
    # to check what is range do
    # [0, 1]
    # [0, 2, 4, 6, 8]
    print(list(range(2)))
    print(list(range(0, 10, 2)))


def exam_loop():
    pass


def exam_condition_statement():
    pass


def exam_try_except():
    pass


def exam_function():
    pass


def exam_file_operation():
    # open, write/append, read/readline, close
    pass


class Exam_Class:
    def __init__(self, param1, param2):
        self.attr1 = param1
        self.attr2 = param2

    def show_attr(self):
        print(self.attr1)
        print(self.attr2)


if __name__ == '__main__':
    # print_hi('Python3')
    # exam_range()

    obj = Exam_Class("Hello", "Python3")
    obj.show_attr()


