'''
Created on 2017年8月4日

@author: admin
'''
# -*- coding:utf-8 -*-
import pymysql
def connect():
    config={'host':'127.0.0.1',
                'user':'root',
                'password':'root',
                'port':3306,
                'database':'my_devpos',
                'charset':'utf8'
            }
    try:
        conn=pymysql.connect(**config)
        print("conn is success!")
        return conn
    except Exception as e:
        print("conn is fails{}".format(e))
        
        
def select_table(table_name,ip):
    sql_select='select ip from ' +table_name+' where ip =%s'
    sql = 'select * from people_user'
    sql = 'select * from auth_user where username = %s'
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql_select,'ip')
        # 获取剩余结果的第一行数据
#         row_1 = cursor.fetchone()
#         
#         # 获取剩余结果前n行数据
#         row_2 = cursor.fetchmany(3)
         
        # 获取剩余结果所有数据
        row_3 = cursor.fetchall()
        print (row_3)
        
        conn.commit()
#         print ("row_1",row_1)
#         print ("row_2",row_2)
        print ("row_3",row_3)
        print ("row_3",len(row_3))
        return row_3 
    except Exception as e:
        print("select cursor is faild".format(e))


def select_all(table_name):
    sql_select='select * from ' +table_name + ' order by ip'
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql_select)
        # 获取剩余结果所有数据
        row_3 = cursor.fetchall()
        conn.commit()
        return row_3 
    except Exception as e:
        print("select cursor is faild".format(e))
        
#插入hostname表
def insert_table(table_name,data):
        try:
            conn=connect()
            cursor = conn.cursor()
            #元组连接插入方式
            sql_insert = "insert into python1(ip,hostname,ostype,application,pwd,username,port) \
            values(%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql_insert, data)
            conn.commit()
        except Exception as e:
            print("execute fails{}".format(e))
        finally:
            cursor.close()
            conn.close()
            print("conn has chosed")
            
def delete_table(table_name,ip):
        try:
            conn=connect()
            cursor = conn.cursor()
            #元组连接插入方式
            sql_delete = 'delete *from '+table_name+' where ip= %s'
            cursor.execute(sql_delete, ip)
            conn.commit()
        except Exception as e:
            print("execute fails{}".format(e))
        finally:
            cursor.close()
            conn.close()
            print("conn has chosed")
def update_table(table_name,ip):
        try:
            conn=connect()
            cursor = conn.cursor()
            #元组连接插入方式
            sql_delete = 'update  '+table_name+'set hostname=%s,ostype=%s,applicaion=%s,port=%s where ip=%s'
            +' where ip= %s'
            cursor.execute(sql_delete, ip)
            conn.commit()
        except Exception as e:
            print("execute fails{}".format(e))
        finally:
            cursor.close()
            conn.close()
            print("conn has chosed")

if __name__=='__main__':
    connect()
    select_table('host','root')


