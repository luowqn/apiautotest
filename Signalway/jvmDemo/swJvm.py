#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : jvm.py
# @Author: luowq
# @Date  : 2019/9/27 14:17
# @Desc  :
from jpype import *
import os

class SwJvm(object):

    def __init__(self,className,jarName):
        jarPath = os.path.abspath(os.path.dirname(__file__))
        startJVM(getDefaultJVMPath(),"-ea",r"-Djava.class.path=%s\%s"%(jarPath,jarName))
        self.JClass = JClass(className)()

    def encryptAES7(self,str, key, iv):
        return self.JClass.encryptAES7(str,key,iv)

    def decryptAES7(self,str,key,iv):
        return self.JClass.decryptAES7(str,key,iv)

    def shutDown(self):
        shutdownJVM()
