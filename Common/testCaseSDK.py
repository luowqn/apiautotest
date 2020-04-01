#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:luowq
# Data: 2020/3/30 14:42
# File: testCaseSDK.py


class TestModule:

    def __init__(self, **kwargs):
        super(TestModule, self).__init__()
        self.__dict__.update(**kwargs)

class TestCase:

    def __init__(self,no,name):
        self.no = no
        self.name = name
        self.testModules = []