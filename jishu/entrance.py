#the entrance of data processing
from jishu.mainprocess import process
from zhuanhuan.entrance import Chuancan
def ent(self):
    #img = Chuancan.read()
    print(Chuancan.read())
    B_num,G_num = process(img)
    Chuancan.write(B_num,G_num)


