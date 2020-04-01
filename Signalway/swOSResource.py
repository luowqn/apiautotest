#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : swOsResource.py
# @Author: luowq
# @Date  : 2019/6/12 14:02
# @Desc  :
import psutil

class Cpu(object):

    def __init__(self,interval):
        #逻辑核心数
        self.mLogicalCount = psutil.cpu_count()
        #物理核心数
        self.mCount = psutil.cpu_count(logical=False)
        #使用率
        self.mUsage= psutil.cpu_percent(interval=interval,percpu=True)

class Memory(object):

    def __init__(self):
        memoryInfo = psutil.virtual_memory()
        #内存总大小
        self.mTotal = memoryInfo.total
        #使用率
        self.mUsage = memoryInfo.percent
        #可使用大小
        self.mAvailable = memoryInfo.available
        #已使用大小
        self.mUsed = memoryInfo.used
        #空闲大小
        self.mFree = memoryInfo.free

class Disk(object):

    def __init__(self,dir):
        #磁盘使用率
        self.mDiskUsage = psutil.disk_usage(dir)

class SwOSResource(object):
    '''
    获取系统资源
    Cpu：默认按1秒去计算Cpu使用率，返回CPU信息对象
    Memory：返回内存信息对象
    Process：根据pid，返回进程信息
    '''
    @staticmethod
    def Cpu(interval=1):
        return Cpu(interval)

    @staticmethod
    def Memory():
        return Memory()

    @staticmethod
    def Disk(dir):
        return Disk(dir)

    @staticmethod
    def Process(pid):
        return psutil.Process(pid)


if __name__ == '__main__':
    Cpu = SwOSResource.Cpu(1)
    print(Cpu.mCount)