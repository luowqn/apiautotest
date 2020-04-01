#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: luowq
# @Date  : 2019/6/3 22:41
# @Desc  :
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : swDatabase.py
# @Author: luowq
# @Date  : 2019/6/12 14:00
# @Desc  :
from swDatabase import SwDatabase
from swString import SwString
from swTime import SwTime
import requests
import uuid
import traceback

if __name__ == '__main__':
    try:
        url = 'http://172.18.10.137:9900/signalway/image/structurization.htm'
        socket = requests.session()
        with open('plateNumber.json') as f:
            msg = f.read()
            DB = SwDatabase(1,'Result','172.18.2.9',5432,'postgres')
            #DB.execute('select imagename1 from st_data_carbody11_201907 where question1=%d'%question)
            #DB.execute('select imagename1 from st_data_carbody11_201907')
            #DB.execute('select imagename1 from st_data_carface11_201907 ')
            DB.execute("select imagename1,imageurl1 from st_data_carface11_201907")
            rows1 = DB.fetchAll()
            for row1 in rows1:
                imageurl = 'http://172.18.2.9/sucai/%s'%row1[1]
                newKey =  SwString.toHmacMd5('EEB82110676E4A268DB5DFF08DDB1C87', imageurl)
                body = msg%{"id":str(uuid.uuid4()),"newkey":newKey,"imagename":row1[0]+".jpg","time":SwTime.getNow(),
                            "imageUrl":imageurl}
                print(body)
                resp = socket.post(url,body)
                print(resp)
        #DB.execute('select imagename2 from st_data_carface11_201907 where score1=-1')
        #DB.execute('select imagename2 from st_data_carface11_201907 ')
        #DB.execute("select imagename2 from st_data_carface11_201907 where question2=%d" % question)
        #DB.execute('select imagename2 from st_data_carbody11_201907 where question2=%d'%question)
        #DB.execute('select * from st_data_carbody11_201907 where (question2 >= 1)')
        DB.close()
    except:
        print(traceback.print_exc())