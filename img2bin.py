import cv2 as cv
import numpy as np

np.set_printoptions(threshold=10000000000)
class img2bin:
    #背景平滑
    def Sobel(img):
        img = cv.fastNlMeansDenoisingColored(img,None,6.5,6.5,7,21)
        #利用Sobel算子进行过滤
        x=cv.Sobel(img,cv.CV_16S,1,0)
        y=cv.Sobel(img,cv.CV_16S,0,1)
        absx=cv.convertScaleAbs(x)
        absy=cv.convertScaleAbs(y)
        dist=cv.addWeighted(absx,0.1,absy,0.4,0)
        LowerSet = np.array([20,20,0])
        UpperSet = np.array([255,255,255])
        mask = cv.inRange(dist,LowerSet ,UpperSet )
        imgCo = cv.bitwise_and(img, img, mask=mask)
        return imgCo
    #去除原图背景
    def cutBackground(img):
        (rows,cols,channel) = img.shape
        i=0
        j=0
        for i in range(rows):
            for j in range(cols):
                if img[i,j,0]!=0:
                    img[i,j,0]=255
                    img[i,j,1]=255
                    img[i,j,2]=255
        return img
    #转换为二值化图像
    def SetGrey(img):
        GreyImage=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        ret,binimg=cv.threshold(GreyImage,0,255,cv.THRESH_BINARY_INV)
        return binimg