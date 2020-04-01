#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : swLog.py
# @Author: luowq
# @Date  : 2019/6/12 13:59
# @Desc  :
import logging.handlers

LOG_TYPE={
    "warn":logging.WARNING,
    "error":logging.ERROR,
    "info":logging.INFO,
    "debug":logging.DEBUG
}


class SwLog(object):
    '''
    默认按天生成日志，保留3天的日志
    初始化入参：
    （1）when：S：秒  M：分 H：小时 D：天 W：星期
    （2）backCount：保留日志个数
    '''
    def __init__(self, filename, level, when='D', backCount=3):
        self.logger = logging.getLogger(filename)
        format = logging.Formatter('%(asctime)s [%(filename)s:%(lineno)d] %(levelname)s %(message)s')
        self.logger.setLevel(LOG_TYPE.get(level.lower()))

        stream = logging.StreamHandler()
        stream.setFormatter(format)

        handler = logging.handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount,
                                                            encoding='utf-8')
        handler.setFormatter(format)

        self.logger.addHandler(stream)
        self.logger.addHandler(handler)

    def warn(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)