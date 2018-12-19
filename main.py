import cv2 as cv
from img2bin import img2bin
from count import Count

def main():
    img = cv.imread("images/thresholdtest.png")
    sbl = img2bin.Sobel(img)
    imgCut = img2bin.cutBackground(sbl)
    imgBin = img2bin.SetGrey(imgCut)
    count=Count.counter(imgBin)
    print("hhahah")
    print(count)
    cv.namedWindow("Image")
    cv.imshow("Image", imgBin)

    cv.namedWindow("yuantu")
    cv.imshow("yuantu", img)
    cv.waitKey(0)
    # 释放窗口
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()