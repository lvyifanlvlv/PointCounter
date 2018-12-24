import cv2 as cv
from zhuanhuan.data import Data
import json
class Chuancan:
    data = Data()
    def read():
        """
        读整个json，写到data里
        根据json中的图片id。读图，返回
        """
        f1=open("../myjson/package.json", 'r')
        load_dict = json.load(f1)
        Chuancan.data.set_a("ID",load_dict["ID"])
        # Chuancan.data.set_a("TIME", load_dict["TIME"])
        # Chuancan.data.set_a("NAME", load_dict["NAME"])
        # Chuancan.data.set_a("RGROUP", load_dict["RGROUP"])
        # Chuancan.data.set_a("PCOUNT", load_dict["PCOUNT"])
        # Chuancan.data.set_a("ISFINISHED", load_dict["ISFINISHED"])
        Chuancan.data.set_time(load_dict["TIME"])
        img = cv.imread("../images/%s"%Chuancan.data.get_a("ID"))



    def write(Blue, Green):
        Chuancan.data.B_CNT = Blue
        Chuancan.data.G_CNT = Green
Chuancan.read()

# print(Chuancan.data.get_a("ID"))