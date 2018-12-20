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
        return len(st),st,fields
