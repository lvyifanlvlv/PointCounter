import time
class Data:
    # 定义私有变量
    ID,TIME,NAME,RGROUP,RNAME,PCOUNT,ISFINISHED,G_CNT,B_CNT = 0, 0, "", "", "", 0, 0, 0, 0

    # 定义get方法，返回私有变量的值
    def get_a(self,type):
        return Data.type

    def get_TIME(self):
        return Data.TIME
    # 定义set方法，设置私有变量的值
    def set_a(self,type, a):
        Data.type = a

    def set_time(self,a):
        Data.TIME = a

