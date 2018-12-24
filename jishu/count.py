import cv2 as cv
import numpy as np

class Count:
    def counter(img):
        (rows,cols) = img.shape
        fa = np.zeros((rows*cols),dtype=int)
        for i in range(cols*rows):
            fa[i] = i
        def union(x, y):
            fax = getFa(x)
            fay = getFa(y)
            if fax!=fay:
                fa[fay] = fax

        def getFa(idx):
            if fa[idx] != idx:
                fa[idx] = getFa(fa[idx])
                return fa[idx]
            else:
                return fa[idx]

        for i in range(rows-1):
            for j in range(cols-1):
                if i!=0 and j!=0 and i!=rows and j!= rows:
                    if img[i,j]==img[i,j+1] and img[i,j]==0:
                        union(i*rows+j,i*rows+j+1)
                    if img[i,j]==img[i+1,j-1]and img[i,j]==0:
                        union(i*rows+j,i*rows+rows+j-1)
                    if img[i,j]==img[i+1,j] and img[i,j]==0:
                        union(i*rows+j,i*rows+rows+j)
                    if img[i,j]==img[i+1,j+1] and img[i,j]==0:
                        union(i*rows+j,i*rows+rows+j+1)
        for i in range(rows):
            for j in range(cols):
                fa[i*rows+j]=getFa(i*rows+j)
        st=set()
        st.clear()
        fields=np.zeros((rows,cols))
        for i in range(rows-1):
            for j in range(cols-1):
                if img[i,j]==255:
                    continue
                else:
                    st.add("%s"%getFa(i*rows+j))
                    fields[i,j]=getFa(i*rows+j)
        for i in st:
            print(i)
            print(int(i))
        # st = list(st)
        # new_numbers = []
        # for s in st:
        #     new_numbers.append(int(s))
        # st = new_numbers
        return len(st),st,fields

