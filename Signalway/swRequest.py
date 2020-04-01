#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : swRequest.py
# @Author: luowq
# @Date  : 2019/7/17 15:36
# @Desc  :
import requests

class SwRequests(object):
    '''
    0：长连接
    1: 短连接
    '''
    def __init__(self,connType=1):
        if 0 == connType:
            self.socket = requests.session()
        else:
            self.socket = None

    def post(self,url, data=None, json=None, **kwargs):
        return self.__func('post', url, data=data, json=json, **kwargs)

    def get(self, url, data=None, json=None, **kwargs):
        return self.__func('get', url, data=data, json=json, **kwargs)

    def __func(self,reqType, url, data=None, json=None, **kwargs):
        if self.socket:
            longConn = self.socket.post
            if 'get' == reqType:
                longConn = self.socket.get
            resp = longConn(url, data=data, json=json, **kwargs)
        else:
            shortConn = requests.post
            if 'get' == reqType:
                shortConn = requests.get
            resp =shortConn(url, data=data, json=json, **kwargs)
        return resp
    def close(self):
        self.socket.close()