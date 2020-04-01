#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : swtime.py
# @Author: luowq
# @Date  : 2019/6/3 23:35
# @Desc  :
import datetime
import time

class SwTime(object):
    '''
    时间操作集合

     (1)getNow：获取当前时间，返回字符串
     (2)strToTime：字符串转时间对象
     (3)timeToStr: 时间对象转字符串
     (4)operationTime: 必须时间对象入参，年/月/日/时/分/秒/毫秒/月/周/加减操作，返回字符串
    '''

    @staticmethod
    def getNow(format="%Y-%m-%d %H:%M:%S"):
        return datetime.datetime.now().strftime(format)

    @staticmethod
    def getNowTimeStamp():
        return (lambda: int(round(time.time() * 1000)))()

    @staticmethod
    def strToTime(string,format='%Y-%m-%d %H:%M:%S'):
        return datetime.datetime.strptime(string, format)

    @staticmethod
    def timeToStr(time,format="%Y-%m-%d %H:%M:%S"):
        return time.strftime(format)

    @classmethod
    def timeOffset(cls,year=0,month=0,date=0,hour=0,minutes=0,seconds=0,format="%Y-%m-%d %H:%M:%S"):
        try:
            now = datetime.datetime.now()
            y = now.year+year
            m = now.month+month
            d = now.day+date
            h = now.hour+hour
            min = now.minute+minutes
            sec = now.second+seconds
            print(min)
            result =now.replace(year=y, month=m, day=d, hour=h,minute=min,second=sec).strftime(format)
            return result
        except Exception as ex:
            raise ex

    @classmethod
    def operationTime(cls,string,format="%Y-%m-%d %H:%M:%S",days=0,seconds=0,microseconds=0,milliseconds=0,minutes=0,hours=0,weeks=0):
        return cls.timeToStr(cls.strToTime(string) + datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds, milliseconds=milliseconds,
                                  minutes=minutes, hours=hours, weeks=weeks),format)


def testTime():
    print(SwTime.getNow())
    print(SwTime.strToTime("2019-11-28 00:00:00"))
    print(SwTime.operationTime(SwTime.strToTime("2019-11-28 00:00:00"),days=-3))
    print(SwTime.timeOffset(year=-1))
    print(time.time())


if __name__ == '__main__':
    testTime()