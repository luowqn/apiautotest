#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:luowq
# Data: 2020/3/29 21:54
import yaml

class Configure:

    def __init__(self,conFile):
        with open(conFile,encoding='utf-8') as f:
            temp = yaml.safe_load(f)
            self.__dict__.update(**temp)
