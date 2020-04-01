#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : swTimer.py
# @Author: luowq
# @Date  : 2019/9/27 17:05
# @Desc  :
from apscheduler.schedulers.background import BackgroundScheduler

'''
定时器

getJob：获取定时器信息
add_interval：添加定时器任务，时间间隔为秒 
              jobId：为定时器id
              jobFunc：定时器触发后调用的函数
stop_job：停止定时器仍无
'''
class SwTimer(object):

    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def getJob(self,jobId):
        return self.scheduler.get_job(jobId)

    def stop_job(self,jobId):
        self.scheduler.remove_job(jobId)

    def add_interval(self,jobId,jobFunc,sec=0,*args):
        #self.scheduler.add_job(jobFunc, 'interval',seconds=sec,id=jobId,args=args)
        self.scheduler.add_job(jobFunc, 'cron', second='*/%d'%sec,id=jobId,args=args)

    def run(self):
        self.scheduler.start()

class test(object):

    def __init__(self):
        self.count =6

def jobFunc(msg):
    print(msg[0],msg[1])
    print("HelloWorld"+str(msg.count)+msg)
    msg.count = msg.count -1


if __name__ == '__main__':
    import traceback
    try:
        tst = test()
        t = SwTimer()
        t.add_interval('1',jobFunc,3,[tst,'#####'])
        t.run()
        while True:
            pass
    except Exception:
        print(traceback.format_exc())
