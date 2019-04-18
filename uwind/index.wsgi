#!/usr/bin/python2
# -*- coding: UTF-8 -*-
#encoding=utf-8

import os

import pymysql.cursors
import pymysql


def test():
    # 连接数据库
    connect = pymysql.Connect(
        host='my9517919.xincache1.cn',
        port=3306,
        user='my9517919',
        passwd='a4P5p5S4',
        db='my9517919',
        charset='utf8'
    )

    # 获取游标
    cursor = connect.cursor()

    try:
        cursor.execute("set names 'utf8'")
        cursor.execute("select * from my_users")  # 添加数据
    except Exception as e:
        connect.rollback()  # 事务回滚
        a = '事务处理失败'
        print('事务处理失败', e)
    else:
        s = ''
        result = cursor.fetchall()
        for row in result:
            idd = row[0]
            name = row[1]
            s = s + str(idd) + "<br>"+row[1].encode('utf8')+ "<br>"
        connect.commit()  # 事务提交
        a = '事务处理成功'+ s
        print('事务处理成功', cursor.rowcount)


    # 关闭连接
    cursor.close()
    connect.close()
    return a



def application(environ, start_response):
    start_response('200 ok', [('content-type', 'text/html; charset=UTF-8')])
    c = os.getcwd()
    d = str(pymysql.MySQLError)
    e = str(pymysql.VERSION)
    return ['<body><br>'+test()+'<br>Hello, SAE <br> 这是第一个测试的代码!测试一下就可以了'+e+c+d+'</body>']


if __name__ == "__main__":

    print(test())
