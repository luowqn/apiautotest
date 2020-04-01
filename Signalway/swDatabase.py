#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : swDatabase.py
# @Author: luowq
# @Date  : 2019/6/12 14:00
# @Desc  :
import pymysql
import psycopg2
import sqlite3
import traceback

class SwDatabase(object):

    def  __init__(self,dbtype,database,host='127.0.0.1',port=3306,user='signalway',password='1234zxcv'):
        if 0 == dbtype:
            self.db = pymysql.connect(host=host,user=user,password=password,database=database,port=port)
        elif 1 == dbtype:
            self.db = psycopg2.connect(host=host,port=port,user=user,password=password,database=database)
        elif 2 == dbtype:
            self.db = sqlite3.connect(database)
        self.cursor = self.db.cursor()


    def execute(self,sql):
        try :
            self.cursor.execute(sql)
            self.db.commit()
        except:
            print(traceback.print_exc())
            self.db.rollback()
            raise

    def fetchOne(self):
        return self.cursor.fetchone()

    def fetchAll(self):
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    try:
        datas1 = []
        datas2 = []
        question = 4
        DB = SwDatabase(1,'Result','172.18.2.9',5432,'postgres')
        #DB.execute('select imagename1 from st_data_carbody11_201907 where question1=%d'%question)
        #DB.execute('select imagename1 from st_data_carbody11_201907')
        #DB.execute('select imagename1 from st_data_carface11_201907 ')
        DB.execute("select imagename1 from st_data_carface11_201907 where question1=%d" % question)
        rows1 = DB.fetchAll()
        for row1 in rows1:
            datas1.append(row1[0])
        #DB.execute('select imagename2 from st_data_carface11_201907 where score1=-1')
        #DB.execute('select imagename2 from st_data_carface11_201907 ')
        DB.execute("select imagename2 from st_data_carface11_201907 where question2=%d" % question)
        #DB.execute('select imagename2 from st_data_carbody11_201907 where question2=%d'%question)
        #DB.execute('select * from st_data_carbody11_201907 where (question2 >= 1)')
        rows2 = DB.fetchAll()
        for row2 in rows2:
            datas2.append(row2[0])
        DB.close()
        datas1.extend(datas2)
        with open('test.csv','w',encoding='utf-8') as f:
            datas = set(datas1)
            print(len(datas))
            f.write('\n'.join(datas))
        # DB.execute("insert test2(`id`,`name`,`age`) values(4,'test4',4)")
        # DB.close()
        # DB = Database(1, 'temp', '172.18.2.9')
        # DB.execute("INSERT INTO test2(id,name,age) VALUES(1,'test1',1)")
        # DB.close()
       #  DB = Database(2, 'test.db')
       #  DB.execute('''CREATE TABLE COMPANY
       # (ID INT PRIMARY KEY     NOT NULL,
       # NAME           TEXT    NOT NULL,
       # AGE            INT     NOT NULL,
       # ADDRESS        CHAR(50),
       # SALARY         REAL);''')
      #   DB.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      # VALUES (1, 'Paul', 32, 'California', 20000.00 )")
      #   DB.close()
    except:
        print(traceback.print_exc())