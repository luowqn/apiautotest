#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : swString.py
# @Author: luowq
# @Date  : 2019/6/12 14:01
# @Desc  :
import json
import hmac
import base64
import hashlib

class SwString(object):
    '''
    toJson：字符串转json
    jsonTo：json转字符串
    toHmacMd5：字符串编码为哈希MD5
    toBase64：字符串转baase64
    '''

    @staticmethod
    def toJson(string,encoding='utf-8'):
        try:
            return json.loads(string,encoding=encoding)
        except Exception as ex:
            raise ex

    @staticmethod
    def jsonTo(obj,ensure_ascii=True):
        return json.dumps(obj,indent=4,ensure_ascii=ensure_ascii)

    @staticmethod
    def toHmacMd5(key,msg=None,encoding='utf-8'):
        if msg:
            msg = bytes(msg,encoding=encoding)
        return hmac.new(bytes(key, encoding=encoding), msg).hexdigest()

    @staticmethod
    def toBase64(string,encoding='utf-8'):
        return str(base64.b64encode(string), encoding=encoding)

    @staticmethod
    def toMd5(string):
        return hashlib.md5(string).hexdigest()


def testString():
    print(SwString.toJson('{"a":1}'))
    test={}
    test['aa'] = 'test'
    test['bb'] = 'kk'
    print(SwString.jsonTo(test))
    print(SwString.toHmacMd5('aaaaa','bbbb'))
    print(SwString.toJson('{"code":200,"command":"HB.R","data":"{\"serverTime\":1570613038406}","msg":"OK","requestId":"1570613035009","time":"2019-10-09 17:23:58"}'))

if __name__ == '__main__':
    testString()