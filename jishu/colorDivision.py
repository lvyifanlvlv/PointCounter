
class CNT:
    def cnt(fathers,img,fields,count):
        # 记录连通区域内的像素值之和

        # 统计点的个数
        p_cnt = 0

        #对二值图进行遍历
        (rows,cols) = fields.shape
        print(fields.shape)
        while count > 0:
            G_cnt = 0
            B_cnt = 0
            for i in fathers:
                sum1 = 0  # 绿色通道的像素值之和
                sum2 = 0  # 蓝色通道的像素值之和

                father=int(i)
                for i in range(rows):
                    for j in range(cols):
                        if fields[i,j]==father:
                            sum1 += img[i,j,1]
                            sum2 += img[i,j,0]
                if sum1 > sum2:
                    G_cnt = G_cnt + 1
                elif sum2 > sum1:
                    B_cnt = B_cnt + 1
            count = count - 1
        print("The number of green dots in the figure is",G_cnt)
        print("The number of blue dots in the figure is",B_cnt)
        return G_cnt,B_cnt
