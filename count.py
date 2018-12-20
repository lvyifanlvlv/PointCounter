import cv2 as cv
import numpy as np


class CNT:
    def cnt(fathers,img,fields,count):
        # 记录连通区域内的像素值之和
        sum1 = 0  # 绿色通道的像素值之和
        sum2 = 0  # 蓝色通道的像素值之和

        # 统计点的个数
        p_cnt = 0
        G_cnt = 0
        B_cnt = 0
        #对二值图进行遍历
        (rows,cols) = fields.shape
        print(fields.shape)
        while count > 0:
            for i in range(rows):
                for j in range(cols):
                    if fields[i,j] == fathers[p_cnt]:
                        sum1 += img[i,j,1]
                        sum2 += img[i,j,0]
            if sum1 > sum2:
                G_cnt = G_cnt + 1
            elif sum2 > sum1:
                B_cnt = B_cnt + 1
            count = count - 1
            p_cnt = p_cnt + 1
        print(G_cnt)
        print(B_cnt)

class Count:
    def counter(img):
        (rows,cols) = img.shape
        fa = np.zeros((rows*cols),dtype=int)
        for i in range(cols*rows):
            fa[i] = i

        def union(x, y):
            fax = getFa(x)
            fay = getFa(y)
            fa[fax] = fay

        def getFa(idx):
            if fa[idx] != idx:
                fa[idx] = getFa(fa[idx])
                return fa[idx]
            else:
                return fa[idx]


        for i in range(rows-1):
            for j in range(cols-1):
                if img[i,j]==img[i,j+1]:
                    union(i*rows+j,i*rows+j+1)
                if img[i,j]==img[i+1,j-1]:
                    union(i*rows+j,i*rows+rows+j-1)
                if img[i,j]==img[i+1,j]:
                    union(i*rows+j,i*rows+rows+j)
                if img[i,j]==img[i+1,j+1]:
                    union(i*rows+j,i*rows+rows+j+1)
        st=set()
        st.clear()
        fields=np.zeros((rows,cols))
        for i in range(rows):
            for j in range(cols):
                if img[i,j]==255:
                    continue
                else:
                    st.add("%s"%getFa(i*rows+j))
                    fields[i,j]=getFa(i*rows+j)
        st = list(st)
        new_numbers = []
        for s in st:
            new_numbers.append(int(s))
        st = new_numbers
        return len(st),st,fields
