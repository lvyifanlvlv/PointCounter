import cv2 as cv
from zhuanhuan.data import Data
import json
import sqlite3
import os
import time
from shujuku import dboperation

class Chuancan:
    data = Data()
    def read():
        """
        读整个json，写到data里
        根据json中的图片id。读图，返回
        """
        f1=open("myjson/receive.json", 'r')
        load_dict = json.load(f1)
        Chuancan.data.set_ID(load_dict["ID"])
        Chuancan.data.set_TIME(load_dict["TIME"])
        Chuancan.data.set_NAME(load_dict["NAME"])
        Chuancan.data.set_RGROUP(load_dict["RGROUP"])
        Chuancan.data.set_RNAME(load_dict["RNAME"])
        Chuancan.data.set_PCOUNT(load_dict["PCOUNT"])
        Chuancan.data.set_ISFINISHED(load_dict["ISFINISHED"])
        f1.close()
        img = cv.imread("%s"%Chuancan.data.get_ID())
        print('###############################image reading success!!###############')
        return img


    def write(Blue, Green):
        new_dict = {}
        new_dict['ID'] = Chuancan.data.get_ID()
        new_dict['TIME'] = Chuancan.data.get_TIME()
        new_dict['NAME'] = Chuancan.data.get_NAME()
        new_dict['RGROUP'] = Chuancan.data.get_RGROUP()
        new_dict['RNAME'] = Chuancan.data.get_RNAME()
        new_dict['PCOUNT'] = Chuancan.data.get_PCOUNT()
        new_dict['ISFINISHED'] = Chuancan.data.get_ISFINISHED()
        new_dict['B_CNT'] = Blue
        new_dict['G_CNT'] = Green
        print(new_dict)
        with open("myjson/return.json", "w") as f:
            json.dump(new_dict, f)
        f.close()
        #dboperation.writeDB(new_dict['ID'],new_dict['TIME'],new_dict['NAME'],new_dict['RGROUP'],
        #                   new_dict['RNAME'],new_dict['PCOUNT'],new_dict['ISFINISHED'],
        #                    new_dict['B_CNT'],new_dict['G_CNT'])






