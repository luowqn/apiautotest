#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : swXml.py
# @Author: luowq
# @Date  : 2019/6/12 13:58
# @Desc  :
try:
  import xml.etree.cElementTree as ET
except ImportError:
  import xml.etree.ElementTree as ET


# #tree = ET.parse("E:/src/python/Signalway/testfile/testXml.xml")
# root = ET.fromstring(country_data_as_string)　　#导入字符串
# root = tree.getroot() #前三句导入数据并获取根元素
# print (root.tag)    #取标签名
# print (root.attrib)    #取属性（字典形式）
# for movie in root:
#     print ('*'*30)
#     print ("title:", movie.attrib['title'])    #取属性值
#     print ("type:", movie[0].text)    #取子节点的内容（元素值）