'''
Created on 2017年8月4日

@author: ning.lin
'''
import os

from My_devpos.My_devpos.settings import BASE_DIR

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

path = os.path.join(BASE_DIR, 'My_devpos\\templates').replace('\\','/')

print("BASE_DIR",BASE_DIR)
print("path",path)


name = "xxx\xxx"
name = connection.escape(name)


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