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
                'charset':'utf8',
                #要加上下面一行返回的是list，否则默认返回的是tuple
                'cursorclass':pymysql.cursors.DictCursor,
            }
    try:
        conn=pymysql.connect(**config)
        print("conn is success!")
        return conn
    except Exception as e:
        print("conn is fails{}".format(e))
        
        
def select_table(table_name,ip):

    #sql_select = "select ip from host where ip ='127.0.0.1'"
    #sql_select = 'select ip from ' + table_name
    try:
        conn=connect()
        cursor=conn.cursor()
        if table_name=='host':
            sql_select = "SELECT * FROM "+'`host`'+" WHERE `ip` = %s"
        elif table_name=='device_status':
            sql_select = "SELECT * FROM "+'`device_status`'+" WHERE `ip` = %s"
        cursor.execute(sql_select,(ip))
        # 获取剩余结果的第一行数据
#         row_1 = cursor.fetchone()
#         
#         # 获取剩余结果前n行数据
#         row_2 = cursor.fetchmany(3)
         
        # 获取剩余结果所有数据
        row_3 = cursor.fetchall()
        print ("row_3",row_3)
        
        conn.commit()
#         print ("row_1",row_1)
#         print ("row_2",row_2)
        return row_3 
    except Exception as e:
        print("select_table execute fails{}".format(e))


def select_all(table_name):
    sql_select='select * from ' +table_name + ' order by ip'
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql_select)
        # 获取剩余结果所有数据,结果类型为list
        row_3 = cursor.fetchall()
        conn.commit()
        return row_3 
    except Exception as e:
        print("select_all execute fails{}".format(e))
        
#插入hostname表
def insert_table(table_name,data):
        try:
            conn=connect()
            cursor = conn.cursor()
            #元组连接插入方式
            if table_name=='host':
                sql_insert = "insert into `host` (ip,hostname,ostype,application,pwd,username,port) \
                values(%s,%s,%s,%s,md5(%s),%s,%s)"
                cursor.execute(sql_insert, (data['ip'],data['hostname'],data['ostype'],data['application'],data['pwd'],data['username'],data['ports']))
                conn.commit()
            elif table_name=='device_status':
                sql_insert = "insert into python1(ip,hostname,ostype,application,pwd,username,port) \
                values(%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql_insert, data)
                conn.commit()               
        except Exception as e:
            print("insert_table execute fails{}".format(e))
        finally:
            cursor.close()
            conn.close()
            print("conn has chosed")
            
def delete_table(table_name,ip):
        try:
            conn=connect()
            cursor = conn.cursor()
            #元组连接插入方式
            sql_delete = 'delete  from '+table_name+' where ip= %s'
            cursor.execute(sql_delete,(ip,))
            conn.commit()
        except Exception as e:
            print("delete_table execute fails{}".format(e))
        finally:
            cursor.close()
            conn.close()
            print("conn has chosed")
def update_table(table_name,data):
        try:
            conn=connect()
            cursor = conn.cursor()
            #元组连接插入方式md5对密码进行加密
            if table_name=='host':
                sql_update = "update "+table_name+" set `hostname`=%s,`ostype`=%s,`application`=%s,`port`=%s,`username`=%s,`pwd`=md5(%s) where `ip`=%s"
                cursor.execute(sql_update, (data['hostname'],data['ostype'],data['application'],data['ports'],data['username'],data['pwd'],data['ip']))
                conn.commit()
            elif table_name=='device_status':
                sql_update = "update "+table_name+" set `cpu`=%s,`memory`=%s,`location`=%s,`product`=%s,`platform`=%s,`sn`=%s where `ip`=%s"
                cursor.execute(sql_update, (data['cpu'],data['memory'],data['location'],data['product'],data['platform'],data['sn'],data['ip']))
                conn.commit()
        except Exception as e:
            print("update_table execute fails{}".format(e))
        finally:
            cursor.close()
            conn.close()
            print("conn has chosed")

# if __name__=='__main__':
#     connect()
#     select_table('host','root')
#     dev_list=select_all('device_status')
#     print("dev_list",type(dev_list))


