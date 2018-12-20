import cv2 as cv
import numpy as np
from img2bin import img2bin


#记录连通区域内的像素值之和
sum1 = 0 #绿色通道的像素值之和
sum2 = 0 #蓝色通道的像素值之和

#统计点的个数
G_cnt = 0
B_cnt = 0
def cnt(fathers,img,imgBin,count):
        p_cnt = 0
        G_cnt = 0
        B_cnt = 0
        #对二值图进行遍历
        (rows,cols) = imgBin.shape
        print(imgBin.shape)
        while count > 0:
            for i in range(rows):
                for j in range(cols):
                    if imgBin[i,j] == fathers[p_cnt]:
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

cnt(fathers,img,imgBin,count)

#
# n = 0
# update = []
#
# (rows,cols) = imgBin.shape
# print(imgBin.shape)
# for i in range(rows):
#     for j in range(cols):
#         update.append(img[i,j])
#         n = n + 1
#         print(imgBin[i, j], end=" ")
# print()
# print(n)
#
# m = 0
# original = []
# q = 0
# green = []
# (row,col,k) = img.shape
# for i in range(row):
#     for j in range(col):
#         if(imgBin[i,j] == 0):
#             green.append(img[i,j,0])
#         original.append(img[i,j,0])
#         m = m + 1
#         print(img[i, j, 0], end=" ")
# print()
# print(m)
#
# def averagenum(num):
#     nsum = 0
#     for i in range(len(num)):
#         nsum += num[i]
#     print(nsum / len(num))
# averagenum(green)
