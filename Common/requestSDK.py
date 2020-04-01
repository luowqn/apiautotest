#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:luowq
# Data: 2020/3/29 21:58
from .enum import REQ_METHOD_TYPE_POST,REQ_METHOD_TYPE_GET
import json

class RequestSDK:

    @staticmethod
    def buidBody(bodyfile,bodyargs):
        try:
            with open(bodyfile,encoding="utf-8") as f:
                body = f.read()
                for key,value in bodyargs.item():
                    body.replace("${%s}"%key,value)
                body = json.dumps(body)
                return body
        except Exception as ex:
            raise ex

    @staticmethod
    def sendReq(sockfd,url,method,data=None,json=None):
        try:
            if method == REQ_METHOD_TYPE_POST:
                return sockfd.post(url,json=json,data=data)
            else:
                return sockfd.get(url, json=json, data=data)
        except Exception as ex:
            raise ex