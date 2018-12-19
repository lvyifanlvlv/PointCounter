import cv2 as cv
import numpy as np
from img2bin import img2bin

img = cv.imread("images/thresholdtest.png")
sbl = img2bin.Sobel(img)
imgCut = img2bin.cutBackground(sbl)
imgBin = img2bin.SetGrey(imgCut)

n = 0
update = []

(rows,cols) = imgBin.shape
print(imgBin.shape)
for i in range(rows):
    for j in range(cols):
        update.append(img[i,j])
        n = n + 1
        print(imgBin[i, j], end=" ")
print()
print(n)

m = 0
original = []
q = 0
green = []
(row,col,k) = img.shape
for i in range(row):
    for j in range(col):
        if(imgBin[i,j] == 0):
            green.append(img[i,j,0])
        original.append(img[i,j,0])
        m = m + 1
        print(img[i, j, 0], end=" ")
print()
print(m)

def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    print(nsum / len(num))
averagenum(green)
