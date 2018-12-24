#using for database reading
import sqlite3
import os
import time

def get_conn(path):
    conn = sqlite3.connect(path)
    if os.path.exists(path) and os.path.isfile(path):
        #print('硬盘上面:[{}]'.format(path))
        return conn
    else:
        conn = None
        #print('内存上面:[:memory:]')
        return sqlite3.connect(':memory:')

def get_cursor(conn):
    if conn is not None:
        return conn.cursor()
    else:
        return get_conn('').cursor()

def create_table(conn, sql):
    '''创建数据库表：student'''
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        cu.execute(sql)
        conn.commit()
        print('创建数据库表[student]成功!')
        close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

def close_all(conn, cu):
    '''关闭数据库游标对象和数据库连接对象'''
    try:
        if cu is not None:
            cu.close()
    finally:
        if cu is not None:
            cu.close()

def save(conn, sql, data):
    '''插入数据'''
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            for d in data:
                cu.execute(sql, d)
                conn.commit()
            close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

def fetchall(conn, sql):
    '''查询所有数据'''
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        cu.execute(sql)
        r = cu.fetchall()
        if len(r) > 0:
            for e in range(len(r)):
                print(r[e])
    else:
        print('the [{}] is empty or equal None!'.format(sql))

# def fetchone(conn, sql, data):
#     '''查询一条数据'''
#     if sql is not None and sql != '':
#         if data is not None:
#             # Do this instead
#             d = (data,)
#             cu = get_cursor(conn)
#             cu.execute(sql, d)
#             r = cu.fetchall()
#             if len(r) > 0:
#                 for e in range(len(r)):
#                     print(r[e])
#         else:
#             print('the [{}] equal None!'.format(data))
#     else:
#         print('the [{}] is empty or equal None!'.format(sql))

# def update(conn, sql, data):
#     '''更新数据'''
#     if sql is not None and sql != '':
#         if data is not None:
#             cu = get_cursor(conn)
#             for d in data:
#                 cu.execute(sql, d)
#                 conn.commit()
#             close_all(conn, cu)
#     else:
#         print('the [{}] is empty or equal None!'.format(sql))

# def delete(conn, sql, data):
#     '''删除数据'''
#     if sql is not None and sql != '':
#         if data is not None:
#             cu = get_cursor(conn)
#             for d in data:
#                 cu.execute(sql, d)
#                 conn.commit()
#             close_all(conn, cu)
#     else:
#         print('the [{}] is empty or equal None!'.format(sql))

# def drop_table_test():
#     '''删除数据库表测试'''
#     conn = get_conn(DB_FILE_PATH)
#     drop_table(conn, TABLE_NAME)

def create_table_test(path):
    '''创建数据库表测试'''
    create_table_sql = '''CREATE TABLE `student`(
                              `ID` char(20) PRIMARY KEY  NOT NULL,
                              `TIME` char(20) DEFAULT NULL, 
                              `NAME` char(20) DEFAULT NULL,
                              `RGROUP` char(20) DEFAULT NULL,
                              `RNAME` char(20) DEFAULT NULL,
                              `PCOUNT` int(11) DEFAULT NULL,
                              `ISFINISHED` int(11) DEFAULT NULL,
                              `G_CNT` int(11) DEFAULT NULL,
                              `B_CNT` int(11) DEFAULT NULL
                          )'''
    conn = get_conn(path)
    create_table(conn, create_table_sql)

def save_test(data):
    '''保存数据测试...'''
    save_sql = '''INSERT INTO student values (?, ?, ?, ?, ?, ?, ?, ?, ?)'''

    conn = get_conn('E:\\PointCounter\\hongten.db')
    save(conn, save_sql, data)
    print('写入数据库表[student]成功!')

def fetchall_test():
    '''查询所有数据...'''
    fetchall_sql = '''SELECT * FROM student'''
    conn = get_conn('E:\\PointCounter\\hongten.db')
    fetchall(conn, fetchall_sql)

# def fetchone_test():
#     '''查询一条数据...'''
#     fetchone_sql = 'SELECT * FROM student WHERE ID = ? '
#     data = 1
#     conn = get_conn(DB_FILE_PATH)
#     fetchone(conn, fetchone_sql, data)

# def update_test():
#     '''更新数据...'''
#     update_sql = 'UPDATE student SET G_CNT = ? WHERE ID = ? '
#     data = [(3, 1)]
#     conn = get_conn(DB_FILE_PATH)
#     update(conn, update_sql, data)

def writeDB(a,b,c,d,e,f,g,h,i):
    data = [(a,b,c,d,e,f,g,h,i)]
    save_test(data)
    fetchall_test()
    # fetchone_test()
    # update_test()
    # fetchall_test()
    # fetchall_test()



