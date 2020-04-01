#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : swRandom.py
# @Author: luowq
# @Date  : 2019/10/15 14:19
# @Desc  :
import random

class SwRandom(object):

    '''
    preStr:车牌号前缀 例如：桂/粤
    '''
    @staticmethod
    def CarNo(preStr):
        baseStr = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
        length = len(baseStr) - 1
        randomStr1 = baseStr[random.randint(0, length)]
        randomStr2 = baseStr[random.randint(0, length)]
        plateNumber = preStr + randomStr1 + str(random.randint(1000, 9999)) + randomStr2
        return plateNumber

    @staticmethod
    def randInt(start,end):
        return random.randint(start,end)

    @staticmethod
    def Phone():
        # 第二位数字
        second = [3, 4, 5, 7, 8][random.randint(0, 4)]
        # 第三位数字
        third = {
            3: random.randint(0, 9),
            4: [5, 7, 9][random.randint(0, 2)],
            5: [i for i in range(10) if i != 4][random.randint(0, 8)],
            7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
            8: random.randint(0, 9),
        }[second]
        # 最后八位数字
        suffix = random.randint(9999999, 100000000)
        # 拼接手机号
        return "1{}{}{}".format(second, third, suffix)

# print(SwRandom.CarNo('津'))