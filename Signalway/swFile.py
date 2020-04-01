#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : swFile.py
# @Author: luowq
# @Date  : 2019/6/3 22:55
# @Desc  :
import base64
import json
from  xml.etree import ElementTree

class SwFile(object):
    '''
    文件操作集合

     (1)readFileJson：读取文件并转换为json
     (2)readFileString：读取文件转换为字符串
     (3)readFileBase64: 读取文件转换为base64
     (4)writeFileJson: 将json对象写入文件
     (5)writeFileString: 字符串写入文件
    '''

    @staticmethod
    def readFileJson(file,encoding=None):
        with open(file,encoding=encoding) as f:
            return json.loads(f.read())

    @staticmethod
    def readFileString(file,encoding=None):
        with open(file,encoding=encoding) as f:
            return f.read()

    @staticmethod
    def readFileBase64(file):
        with open(file,"rb") as f:
            return str(base64.b64encode(f.read()), encoding="utf-8")

    @staticmethod
    def writeFileJson(file,jsonObj,encoding=None):
        with open(file,'w',encoding=encoding) as f:
            f.write(json.dumps(jsonObj,indent=2))

    @staticmethod
    def writeFileString(file,string,encoding=None):
        with open(file,"w",encoding=encoding) as f:
            f.write(string)


def testFile():
    #print(SwFile.readFileBase64('testfile/testface.jpg'))
    print(SwFile.readFileJson('testfile/testJson.json'))
    print(SwFile.readFileString('testfile/testXml.xml'))
    #SwFile.writeFileJson('test.json',{'test':1,"yun":2,"parms":{"dataid":"heeell","yyy":88}})

if __name__ == '__main__':
    testFile()