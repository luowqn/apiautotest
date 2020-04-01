#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:luowq
# Data: 2020/3/30 14:50
# File: 1.py
import  re
body = '''
{
    "requestId":null,
    "code":"0",
    "message":"执行成功",
    "data":[
        {
            "organizationId":"0e7334c196e34395a2b93545addf1358",
            "organizationCode":"JT000104",
            "parentId":"2582cc8832194edea0699bc10fa50160",
            "organizationName":"南宁分公司334",
            "organizationType":"分公司",
            "imgIcon":"group1/M00/00/27/wKgDC15mMOqEeEm6AAAAAHi9vBU661.jpg",
            "organizationPicture":null,
            "organizationPhone":"07716722770113",
            "organizationPerson":"H总113",
            "organizationAddress":"南宁市中关村113",
            "organizationChildCount":null,
            "longitude":"12.0999999999999996",
            "latitude":"33.4399999999999977",
            "uiStyle":"###FFFF",
            "road":null
        },
        {
            "organizationId":"27ebc966013f493f958ec5d0611552bf",
            "organizationCode":"JT00010401",
            "parentId":"0e7334c196e34395a2b93545addf1358",
            "organizationName":"北京信路威南宁分公司平台中心",
            "organizationType":"路段公司",
            "imgIcon":null,
            "organizationPicture":null,
            "organizationPhone":"07716722770",
            "organizationPerson":"H总",
            "organizationAddress":"南宁市中关村",
            "organizationChildCount":null,
            "longitude":null,
            "latitude":null,
            "uiStyle":"###FFFF",
            "road":null
        },
        {
            "organizationId":"c1a52cf0022141ba946e54cf0a807443",
            "organizationCode":"JT0001040101",
            "parentId":"27ebc966013f493f958ec5d0611552bf",
            "organizationName":"南宁分公司平台中心高速平台组",
            "organizationType":"收费站",
            "imgIcon":null,
            "organizationPicture":null,
            "organizationPhone":"07716722770",
            "organizationPerson":"H总",
            "organizationAddress":"南宁市中关村3-19",
            "organizationChildCount":null,
            "longitude":null,
            "latitude":null,
            "uiStyle":"###FFFF",
            "road":null
        },
        {
            "organizationId":"2582cc8832194edea0699bc10fa50160",
            "organizationCode":"JT001",
            "parentId":null,
            "organizationName":"北京信路威科技股份有限公司2",
            "organizationType":"总公司",
            "imgIcon":null,
            "organizationPicture":null,
            "organizationPhone":"010621405082",
            "organizationPerson":"李总22",
            "organizationAddress":"北京市中关村2",
            "organizationChildCount":null,
            "longitude":null,
            "latitude":null,
            "uiStyle":"###FFFF",
            "road":null
        }
    ]
}
'''
print("\\{[^\\}]*\"organizationName\":"+"北京信路威科技股份有限公司2"+"[^\\}]*\\}")
s = re.findall("\\{[^\\}]*\"organizationName\":"+"北京信路威科技股份有限公司2"+"[^\\}]*\\}",body, re.M | re.I)
print(s)

import  random

print(len('006545001003920010'))
print('G00'+str(random.randint(8000000000000000,9000000000000000)))