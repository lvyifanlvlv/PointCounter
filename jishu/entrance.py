#the entrance of data processing
from jishu.mainprocess import process
from zhuanhuan.entrance import Chuancan
from zhuanhuan.DeletePicture import Delete
def ent():
    img = Chuancan.read()
    B_num,G_num = process(img)
    Chuancan.write(B_num,G_num)
    Delete.DPictrue("../images/%s"%Chuancan.data.get_ID())

if __name__ == '__main__':
    ent()