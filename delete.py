'''
Created on 2017年8月4日

@author: ning.lin
'''
from _datetime import date
from _md5 import md5
import datetime
import json
import os

from cffi.api import basestring

from My_devpos.My_devpos.settings import BASE_DIR
from My_devpos.devmanage.pymysql_conn import select_table


# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 
# path = os.path.join(BASE_DIR, 'My_devpos\\templates').replace('\\','/')
# str1=md5('123'.encode(encoding='utf_8', errors='strict'))
# print('md5',str1)

def md5(str1):
    import hashlib  
    if isinstance(str1,str):
        print("这是字符串")
        #encode(encoding='gb2312')
        m = hashlib.md5(str1.encode('UTF-8')) 
        md5value=m.hexdigest()
        return md5value


def select():  
      # if isinstance(obj, datetime.datetime):  
      #     return int(mktime(obj.timetuple()))  
    obj = select_table('host', '192.168.153.135')
    print("obj",obj)
    for i in obj:
        print("i",i)
        date_temp = i['Updatetime']
        print("date_temp",date_temp)
    print (obj)  

if __name__=='__main__':
    print("123")
    select()


#5a97440ea28e0e914a36566a8e3c8668
#     try:
#         req=requests.get(url,headers=header, timeout=10,proxies=proxy_ip,stream=True)
#         print("保存图片",url)
#         r=req.content
#         #print("req",req.text.encode(req.encoding).decode('utf-8'))
#         #print(soup)
#         with open(filename,'wb') as fd:
#             try:
#                 fd.write(r)
#                 print("保存成功")