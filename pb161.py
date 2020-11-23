import math
import time

t1 = time.time()


width = 9
height = 5

# 2,3   3
# 2,6   11
# 2,9   41
# 3,9   3127
# 4,9   41813
# 5,9   1269900
# 5,3   62
# 5,6   8342
# 1,3   1
# 3,3   10
# 3,6   170
# 4,3   23
# 7,3   441
# 8,3   1173
# 6,6   80092

# 9,1   1
# 9,2   41          time: 0.011964797973632812
# 9,3   3127        time: 0.10466790199279785
# 9,4   41813       time: 3.5665953159332275
# 9,5   1269900     time: 127.50538086891174


def fillgrid(g,gridcount,result):
    #print(gridcount,result)
    if gridcount == 0:
        return result +1
    i = 0
    j = 0
    grid = g[:]
    while True:
        if grid[i][j]:
            break
        i += 1
        if i >= width:
            j += 1
            i = 0
            if j >= height:
                return result
    r = result
    # type 1
    if grid[i][j] and i +1 < width and grid[i+1][j] and j+1 < height and grid[i][j+1]:
        #print(gridcount,"type 1")
        grid[i][j] = False
        grid[i+1][j] = False
        grid[i][j+1] = False
        r = fillgrid(grid,gridcount-3,r)
        grid[i][j] = True
        grid[i+1][j] = True
        grid[i][j+1] = True

    # type 2
    if grid[i][j] and i +1 < width and grid[i+1][j] and j+1 < height and grid[i+1][j+1]:
        #print(gridcount,"type 2")
        grid[i][j] = False
        grid[i+1][j] = False
        grid[i+1][j+1] = False
        r = fillgrid(grid,gridcount-3,r)
        grid[i][j] = True
        grid[i+1][j] = True
        grid[i+1][j+1] = True

    # type 3
    if grid[i][j] and i +1 < width  and j+1 < height and grid[i][j+1] and grid[i+1][j+1]:
        #print(gridcount,"type 3")
        grid[i][j] = False
        grid[i+1][j+1] = False
        grid[i][j+1] = False
        r = fillgrid(grid,gridcount-3,r)
        grid[i][j] = True
        grid[i+1][j+1] = True
        grid[i][j+1] = True

    # type 4
    if grid[i][j] and i > 0 and j +1 < height and grid[i-1][j+1] and grid[i][j+1]:
        #print(gridcount,"type 4")
        grid[i][j] = False
        grid[i-1][j+1] = False
        grid[i][j+1] = False
        r = fillgrid(grid,gridcount-3,r)
        grid[i][j] = True
        grid[i-1][j+1] = True
        grid[i][j+1] = True
        
    # type 5
    if grid[i][j] and j+2 < height and grid[i][j+1] and grid[i][j+2]:
        #print(gridcount,"type 5")
        grid[i][j] = False
        grid[i][j+1] = False
        grid[i][j+2] = False
        r = fillgrid(grid,gridcount-3,r)
        grid[i][j] = True
        grid[i][j+1] = True
        grid[i][j+2] = True

    # type 6
    if grid[i][j] and i+2 < width and grid[i+1][j] and grid[i+2][j]:
        #print(gridcount,"type 6")
        grid[i][j] = False
        grid[i+1][j] = False
        grid[i+2][j] = False
        r = fillgrid(grid,gridcount-3,r)
        grid[i][j] = True
        grid[i+1][j] = True
        grid[i+2][j] = True
    return r


def solvegrid(w,h):
    grid = []
    for i in range(w):
        grid.append([])
        for j in range(h):
            grid[i].append(True)

    return fillgrid(grid,w*h,0)

#====================
#print(solvegrid(width,height))

# using 0~511 (010101010) to describe square availability
# 512*512*512 for solutions leading to the last three rows condition


def SA91():
    return 1

def SA92():
    TRSA = []
    bita = [256,128,64,32,16,8,4,2,1]

    for i in range(512):
        t = []
        for j in range(512):
            t.append([0]*512)
        TRSA.append(t)
    
    TRSA[0][0][0]=1
    F1 = [[384,256,0],[384,128,0],[256,384,0],[448,0,0]]
    for i in F1:
        TRSA[i[0]][i[1]][i[2]]=1

    F2 = []
    for fff in range(2,7):
        #F2
        for c in F1:
            #print(c,TRSA[c[0]][c[1]][c[2]])
            ai = -1
            aj = 0
            for i in range(9):
                if bita[i]&c[0] == 0:
                    ai = i
                    break
            if ai == -1:
                aj = 1
                for i in range(9):
                    if bita[i]&c[1] == 0:
                        ai = i
                        break

            # topleft
            if aj == 0 and ai < 8:
                if c[aj]&bita[ai+1] == 0 and c[aj+1]&bita[ai] == 0:
                    nc = c[:]
                    nc[aj] = nc[aj]|bita[ai]
                    nc[aj] = nc[aj]|bita[ai+1]
                    nc[aj+1] = nc[aj+1]|bita[ai]
                    if not nc in F2:
                        F2.append(nc)
                    TRSA[nc[0]][nc[1]][nc[2]] += TRSA[c[0]][c[1]][c[2]]

            # topright
            if aj == 0 and ai < 8:
                if c[aj]&bita[ai+1] == 0 and c[aj+1]&bita[ai+1] == 0:
                    nc = c[:]
                    nc[aj] = nc[aj]|bita[ai]
                    nc[aj] = nc[aj]|bita[ai+1]
                    nc[aj+1] = nc[aj+1]|bita[ai+1]
                    if not nc in F2:
                        F2.append(nc)
                    TRSA[nc[0]][nc[1]][nc[2]] += TRSA[c[0]][c[1]][c[2]]

            # botleft
            if aj == 0 and ai < 8:
                if c[aj+1]&bita[ai] == 0 and c[aj+1]&bita[ai+1] == 0:
                    nc = c[:]
                    nc[aj] = nc[aj]|bita[ai]
                    nc[aj+1] = nc[aj+1]|bita[ai]
                    nc[aj+1] = nc[aj+1]|bita[ai+1]
                    if not nc in F2:
                        F2.append(nc)
                    TRSA[nc[0]][nc[1]][nc[2]] += TRSA[c[0]][c[1]][c[2]]

            # botright
            if aj == 0 and ai >0:
                if c[aj+1]&bita[ai] == 0 and c[aj+1]&bita[ai-1] == 0:
                    nc = c[:]
                    nc[aj] = nc[aj]|bita[ai]
                    nc[aj+1] = nc[aj+1]|bita[ai]
                    nc[aj+1] = nc[aj+1]|bita[ai-1]
                    if not nc in F2:
                        F2.append(nc)
                    TRSA[nc[0]][nc[1]][nc[2]] += TRSA[c[0]][c[1]][c[2]]

            # horizontal
            if ai < 7:
                if c[aj]&bita[ai+1] == 0 and c[aj]&bita[ai+2] == 0:
                    nc = c[:]
                    nc[aj] = nc[aj]|bita[ai]
                    nc[aj] = nc[aj]|bita[ai+1]
                    nc[aj] = nc[aj]|bita[ai+2]
                    if not nc in F2:
                        F2.append(nc)
                    TRSA[nc[0]][nc[1]][nc[2]] += TRSA[c[0]][c[1]][c[2]]
        #F3
        F1 = F2[:]
        F2 = []
    print(TRSA[511][511][0])


            
def SA93():
    width = 9
    height = 6

    TN = width*height//3
    bita = [256,128,64,32,16,8,4,2,1]

    
    F1 = [[0]*height]
    F2 = []

    TRSA1 = []
    TRSA1.append(F1[0]+[1])
    TRSA2 = []
    
    for fff in range(TN):
        for c in F1:
            #first available slot
            ai = -1
            aj = -1
            for j in range(height):
                for i in range(9):
                    if bita[i]&c[j] == 0:
                        ai = i
                        break
                if ai >=0:
                    aj =j
                    break
            if c[aj]&bita[ai]==0:

                # topleft
                if aj < height-1 and ai < 8:
                    if c[aj]&bita[ai+1] == 0 and c[aj+1]&bita[ai] == 0:
                        nc = c[:]
                        nc[aj] = nc[aj]|bita[ai]
                        nc[aj] = nc[aj]|bita[ai+1]
                        nc[aj+1] = nc[aj+1]|bita[ai]
                        if not nc in F2:
                            F2.append(nc)
                            TRSA2.append(nc+[TRSA1[F1.index(c)][-1]])
                        else:
                            TRSA2[F2.index(nc)][-1] += TRSA1[F1.index(c)][-1]

                # topright
                if aj < height-1 and ai < 8:
                    if c[aj]&bita[ai+1] == 0 and c[aj+1]&bita[ai+1] == 0:
                        nc = c[:]
                        nc[aj] = nc[aj]|bita[ai]
                        nc[aj] = nc[aj]|bita[ai+1]
                        nc[aj+1] = nc[aj+1]|bita[ai+1]
                        if not nc in F2:
                            F2.append(nc)
                            TRSA2.append(nc+[TRSA1[F1.index(c)][-1]])
                        else:
                            TRSA2[F2.index(nc)][-1] += TRSA1[F1.index(c)][-1]

                # botleft
                if aj < height-1 and ai < 8:
                    if c[aj+1]&bita[ai] == 0 and c[aj+1]&bita[ai+1] == 0:
                        nc = c[:]
                        nc[aj] = nc[aj]|bita[ai]
                        nc[aj+1] = nc[aj+1]|bita[ai]
                        nc[aj+1] = nc[aj+1]|bita[ai+1]
                        if not nc in F2:
                            F2.append(nc)
                            TRSA2.append(nc+[TRSA1[F1.index(c)][-1]])
                        else:
                            TRSA2[F2.index(nc)][-1] += TRSA1[F1.index(c)][-1]

                # botright
                if aj < height-1 and ai >0:
                    if c[aj+1]&bita[ai] == 0 and c[aj+1]&bita[ai-1] == 0:
                        nc = c[:]
                        nc[aj] = nc[aj]|bita[ai]
                        nc[aj+1] = nc[aj+1]|bita[ai]
                        nc[aj+1] = nc[aj+1]|bita[ai-1]
                        if not nc in F2:
                            F2.append(nc)
                            TRSA2.append(nc+[TRSA1[F1.index(c)][-1]])
                        else:
                            TRSA2[F2.index(nc)][-1] += TRSA1[F1.index(c)][-1]

                # horizontal
                if ai < 7:
                    if c[aj]&bita[ai+1] == 0 and c[aj]&bita[ai+2] == 0:
                        nc = c[:]
                        nc[aj] = nc[aj]|bita[ai]
                        nc[aj] = nc[aj]|bita[ai+1]
                        nc[aj] = nc[aj]|bita[ai+2]
                        if not nc in F2:
                            F2.append(nc)
                            TRSA2.append(nc+[TRSA1[F1.index(c)][-1]])
                        else:
                            TRSA2[F2.index(nc)][-1] += TRSA1[F1.index(c)][-1]

                # vertical
                if aj < height-2:
                    if c[aj+1]&bita[ai] == 0 and c[aj+2]&bita[ai] == 0:
                        nc = c[:]
                        nc[aj] = nc[aj]|bita[ai]
                        nc[aj+1] = nc[aj+1]|bita[ai]
                        nc[aj+2] = nc[aj+2]|bita[ai]
                        if not nc in F2:
                            F2.append(nc)
                            TRSA2.append(nc+[TRSA1[F1.index(c)][-1]])
                        else:
                            TRSA2[F2.index(nc)][-1] += TRSA1[F1.index(c)][-1]
        #F3
        F1 = F2[:]
        F2 = []
        TRSA1 = TRSA2[:]
        TRSA2 = []
        print(fff,time.time()-t1)

    rc = [511]*height
    print(TRSA1[F1.index(rc)])
    #[511, 511, 511, 3127]
    #time: 1.7732722759246826
    #[511, 511, 511, 511, 41813]
    #time: 13.322401523590088
    #[511, 511, 511, 511, 511, 1269900]
    #time: 49.620991945266724
    #[511, 511, 511, 511, 511, 511, 45832761]
    #time: 111.89563751220703


def SA9nv2(n):
    width = 9
    height = n

    TN = width*height//3
    bita = [256,128,64,32,16,8,4,2,1]

    
    F1 = [[0,0,0,0]]
    F2 = []

    TRSA1 = [[0,0,0,0,1]]
    TRSA2 = []
    
    for fff in range(TN):
        for c in F1:
            #first available slot
            ai = -1
            aj = -1
            for j in [1,2,3]:
                for i in range(9):
                    if bita[i]&c[j] == 0:
                        ai = i
                        break
                if ai >=0:
                    aj =j
                    break
            if c[aj]&bita[ai]==0:

                # topleft
                if aj < 3 and ai < 8:
                    if c[aj]&bita[ai+1] == 0 and c[aj+1]&bita[ai] == 0:
                        nc = c[:]
                        nc[aj] = nc[aj]|bita[ai]
                        nc[aj] = nc[aj]|bita[ai+1]
                        nc[aj+1] = nc[aj+1]|bita[ai]
                        if nc[1] == 511 and nc[0]<n-3:
                            if nc[2] == 511 and nc[0]<n-4:
                                nc[1]=nc[3]
                                nc[3]=0
                                nc[2]=0
                                nc[0] += 2
                            else:
                                nc[1]=nc[2]
                                nc[2]=nc[3]
                                nc[3]=0
                                nc[0] += 1
                        if not nc in F2:
                            F2.append(nc)
                            TRSA2.append(nc+[TRSA1[F1.index(c)][-1]])
                        else:
                            TRSA2[F2.index(nc)][-1] += TRSA1[F1.index(c)][-1]

                # topright
                if aj < 3 and ai < 8:
                    if c[aj]&bita[ai+1] == 0 and c[aj+1]&bita[ai+1] == 0:
                        nc = c[:]
                        nc[aj] = nc[aj]|bita[ai]
                        nc[aj] = nc[aj]|bita[ai+1]
                        nc[aj+1] = nc[aj+1]|bita[ai+1]
                        if nc[1] == 511 and nc[0]<n-3:
                            if nc[2] == 511 and nc[0]<n-4:
                                nc[1]=nc[3]
                                nc[3]=0
                                nc[2]=0
                                nc[0] += 2
                            else:
                                nc[1]=nc[2]
                                nc[2]=nc[3]
                                nc[3]=0
                                nc[0] += 1
                        if not nc in F2:
                            F2.append(nc)
                            TRSA2.append(nc+[TRSA1[F1.index(c)][-1]])
                        else:
                            TRSA2[F2.index(nc)][-1] += TRSA1[F1.index(c)][-1]

                # botleft
                if aj < 3 and ai < 8:
                    if c[aj+1]&bita[ai] == 0 and c[aj+1]&bita[ai+1] == 0:
                        nc = c[:]
                        nc[aj] = nc[aj]|bita[ai]
                        nc[aj+1] = nc[aj+1]|bita[ai]
                        nc[aj+1] = nc[aj+1]|bita[ai+1]
                        if nc[1] == 511 and nc[0]<n-3:
                            if nc[2] == 511 and nc[0]<n-4:
                                nc[1]=nc[3]
                                nc[3]=0
                                nc[2]=0
                                nc[0] += 2
                            else:
                                nc[1]=nc[2]
                                nc[2]=nc[3]
                                nc[3]=0
                                nc[0] += 1
                        if not nc in F2:
                            F2.append(nc)
                            TRSA2.append(nc+[TRSA1[F1.index(c)][-1]])
                        else:
                            TRSA2[F2.index(nc)][-1] += TRSA1[F1.index(c)][-1]

                # botright
                if aj < 3 and ai >0:
                    if c[aj+1]&bita[ai] == 0 and c[aj+1]&bita[ai-1] == 0:
                        nc = c[:]
                        nc[aj] = nc[aj]|bita[ai]
                        nc[aj+1] = nc[aj+1]|bita[ai]
                        nc[aj+1] = nc[aj+1]|bita[ai-1]
                        if nc[1] == 511 and nc[0]<n-3:
                            if nc[2] == 511 and nc[0]<n-4:
                                nc[1]=nc[3]
                                nc[3]=0
                                nc[2]=0
                                nc[0] += 2
                            else:
                                nc[1]=nc[2]
                                nc[2]=nc[3]
                                nc[3]=0
                                nc[0] += 1
                        if not nc in F2:
                            F2.append(nc)
                            TRSA2.append(nc+[TRSA1[F1.index(c)][-1]])
                        else:
                            TRSA2[F2.index(nc)][-1] += TRSA1[F1.index(c)][-1]

                # horizontal
                if ai < 7:
                    if c[aj]&bita[ai+1] == 0 and c[aj]&bita[ai+2] == 0:
                        nc = c[:]
                        nc[aj] = nc[aj]|bita[ai]
                        nc[aj] = nc[aj]|bita[ai+1]
                        nc[aj] = nc[aj]|bita[ai+2]
                        if nc[1] == 511 and nc[0]<n-3:
                            nc[1]=nc[2]
                            nc[2]=nc[3]
                            nc[3]=0
                            nc[0] += 1
                        if not nc in F2:
                            F2.append(nc)
                            TRSA2.append(nc+[TRSA1[F1.index(c)][-1]])
                        else:
                            TRSA2[F2.index(nc)][-1] += TRSA1[F1.index(c)][-1]

                # vertical
                if aj == 1:
                    if c[aj+1]&bita[ai] == 0 and c[aj+2]&bita[ai] == 0:
                        nc = c[:]
                        nc[aj] = nc[aj]|bita[ai]
                        nc[aj+1] = nc[aj+1]|bita[ai]
                        nc[aj+2] = nc[aj+2]|bita[ai]
                        if nc[1] == 511 and nc[0]<n-3:
                            if nc[2] == 511 and nc[0]<n-4:
                                if nc[3] == 511 and nc[0]<n-5:
                                    nc[1]=0
                                    nc[3]=0
                                    nc[2]=0
                                    nc[0] += 3
                                else:
                                    nc[1]=nc[3]
                                    nc[3]=0
                                    nc[2]=0
                                    nc[0] += 2
                            else:
                                nc[1]=nc[2]
                                nc[2]=nc[3]
                                nc[3]=0
                                nc[0] += 1
                        if not nc in F2:
                            F2.append(nc)
                            TRSA2.append(nc+[TRSA1[F1.index(c)][-1]])
                        else:
                            TRSA2[F2.index(nc)][-1] += TRSA1[F1.index(c)][-1]
        #F3
        F1 = F2[:]
        F2 = []
        TRSA1 = TRSA2[:]
        TRSA2 = []
        print(fff,time.time()-t1)

    rc = [n-3,511,511,511]
    print(n,TRSA1[F1.index(rc)][-1],time.time()-t1)
    #3 3127 0.6856944561004639
    #4 41813 8.310003519058228
    #5 1269900 29.51517367362976
    #6 45832761 56.81271839141846
    #12 20574308184277971 223.0154857635498
    
    



SA9nv2(12)




print("time:",time.time()-t1)  


    
