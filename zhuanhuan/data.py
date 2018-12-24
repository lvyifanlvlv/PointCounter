import time
class Data:
    # 定义私有变量
    ID,TIME,NAME,RGROUP,RNAME,PCOUNT,ISFINISHED,G_CNT,B_CNT = 0, 0, "", "", "", 0, 0, 0, 0

    # 定义get方法，返回私有变量的值
    def get_ID(self):
        return Data.ID

    def get_TIME(self):
        return Data.TIME

    def get_NAME(self):
        return Data.NAME

    def get_RGROUP(self):
        return Data.RGROUP

    def get_RNAME(self):
        return Data.RNAME

    def get_PCOUNT(self):
        return Data.PCOUNT

    def get_ISFINISHED(self):
        return Data.ISFINISHED

    def get_G_CNT(self):
        return Data.G_CNT

    def get_B_CNT(self):
        return Data.B_CNT

    # 定义set方法，设置私有变量的值
    def set_ID(self,a):
        Data.ID = a

    def set_TIME(self,a):
        Data.TIME = a

    def set_NAME(self,a):
        Data.NAME = a

    def set_RGROUP(self,a):
        Data.RGROUP = a

    def set_RNAME(self,a):
        Data.RNAME = a

    def set_PCOUNT(self,a):
        Data.PCOUNT = a

    def set_ISFINISHED(self,a):
        Data.ISFINISHED = a

    def set_G_CNT(self,a):
        Data.G_CNT = a

    def set_B_CNT(self,a):
        Data.B_CNT = a


