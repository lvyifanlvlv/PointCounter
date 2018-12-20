import cv2 as cv
from img2bin import img2bin
from count import Count

def main():
    img = cv.imread("images/thresholdtest.png")
    sbl = img2bin.Sobel(img)
    imgCut = img2bin.cutBackground(sbl)
    imgBin = img2bin.SetGrey(imgCut)
    count,fathers,fields=Count.counter(imgBin)
    #count:number of points
    #fathers:fathers of every pixels in each point
    #fields:an array size of(rows*cols) in which fathers are marked
    print("The number of points:")
    print(count)
    print("The position of fathers:")
    print(fathers)
    cv.namedWindow("Image")
    cv.imshow("Image", imgBin)

    cv.namedWindow("yuantu")
    cv.imshow("yuantu", img)
    cv.waitKey(0)
    # 释放窗口
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()