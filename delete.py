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