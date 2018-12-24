from shujuku import dboperation
def init():
    '''初始化方法'''
    # 数据库文件绝句路径
    global DB_FILE_PATH
    DB_FILE_PATH = 'E:\\PointCounter\\hongten.db'
    # 数据库表名称
    global TABLE_NAME
    TABLE_NAME = 'student'
    # 创建数据库表student
    dboperation.create_table_test(DB_FILE_PATH)
init()