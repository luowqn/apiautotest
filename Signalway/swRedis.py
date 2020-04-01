#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : swRedis.py
# @Author: luowq
# @Date  : 2019/6/3 22:38
# @Desc  :
import redis

class SwRedis(object):
    '''
    Redis操作集合，没有包含官方所有操作，只包含了哈希操作！！！！

    用法：

    r = SwRedis('172.18.2.5',6379,'1234zxcv',db=8)

    (1)判断集合中的哈希key是否存在
    if r.hexists('books','python'):
       print('python 存在')

    (2)添加集合和哈希值，若集合不存在，则创建
    r.hset('book','test','v3.0.0')

    (3)集合中批量添加哈希值，若集合不存在，则创建
    r.hmset('books',{'Python':'3.6.4','Golange':'11.2.3'})

    (4)获取集合中哈希值
    r.hget('books','Python')
    >>'3.6.4'

    (5)批量获取集合中的哈希值
    r.hmget('books',['Python','Golange'])
    >>['3.6.4','11.2.3']

    (6)删除哈希值
    r.hdel('books', 'Python')

    (7)删除集合
    r.delete('books')

    '''

    def __init__(self,host,port=6379,pwd='1234zxcv',db=6):
        # decode_responses默认为False，结果输出为bytes
        self.__redis_conn = redis.ConnectionPool(host=host,port=port,db=db,password=pwd,decode_responses=True)
        self.__redis = redis.Redis(connection_pool=self.__redis_conn)

    def hexists(self,name,key):
        return self.__redis.hexists(name,key)

    def hset(self,name,key,value):
        return self.__redis.hset(name,key,value)

    def hmset(self,name,mapping):
        return self.__redis.hmset(name,mapping)

    def hget(self,name,key):
        return self.__redis.hget(name,key)

    def hmget(self,name, keys):
        return self.__redis.hmget(name, keys)

    def delete(self,name):
        return self.__redis.delete(name)

    def hdel(self,name,key):
        return self.__redis.hdel(name,key)


def testRedis():
    r = SwRedis('172.18.2.5', 6379, '1234zxcv', db=8)

    # (1)判断集合中的哈希key是否存在
    if r.hexists('books', 'python'):
        print('python 存在')

    # (2)添加集合和哈希值，若集合不存在，则创建
    r.hset('book', 'test', 'v3.0.0')

    # (3)集合中批量添加哈希值，若集合不存在，则创建
    r.hmset('books', {'Python': '3.6.4', 'Golange': '11.2.3'})

    # (4)获取集合中哈希值
    print('获取集合中哈希值:',r.hget('books', 'Python'))

    # (5)批量获取集合中的哈希值
    print('批量获取集合中的哈希值:',r.hmget('books', ['Python', 'Golange']))

    # (6)删除哈希值
    r.hdel('books', 'Python')

    # (7)删除集合
    r.delete('books')



if __name__ == '__main__':
    testRedis()