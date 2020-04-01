#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:luowq
# Data: 2020/3/30 15:39
# File: testCase.py

from Signalway import SwRequests
from Common import RequestSDK
from .globalVars import gVars
import  unittest
import json
import re

class TestCase_%(seq1)d(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.__doc__ = '基础数据准备'
        cls.socketfd = SwRequests(0)

    % (testModule)s

    @classmethod
    def tearDown(cls) -> None:
        cls().socketfd.close()