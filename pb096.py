import math
import time

t1 = time.time()

# read the sudoku into a list
f = open('pb096_sudoku.txt','r')

sdk= f.read().split('Grid')

f.close()

def toGrid(sdk):
    line = sdk.split('\n')
    grid = []
    for i in range(9):
        grid.append([0]*9)
    for i in range(9):
        for j in range(9):
            grid[i][j] = ord(line[i+1][j])-48
    return grid

def showGrid(grid):
    print('+ — — — + — — — + — — — +')
    for i in range(9):
        line = '| '
        for j in range(9):
            if grid[i][j] >= 0:
                line += chr(grid[i][j] +48) + ' '
            else:
                line += '? '
            if j < 8 and j%3 == 2:
                line += '| '
        line += '|'
        print(line)
        if i < 8 and i%3 == 2:
            print('+ — — — + — — — + — — — +')
    print('+ — — — + — — — + — — — +')
            
def get3d(grid):
    return grid[0][0]*100+grid[0][1]*10+grid[0][2]

def solved(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] <= 0:
                return False
    return True

def conflict(grid,i,j):
    for k in range(9):
        if grid[i][k] == grid[i][j] and k != j:
            return True
    for k in range(9):
        if grid[k][j] == grid[i][j] and k != i:
            return True
    for a in range(3):
        for b in range(3):
            ti = (i//3)*3+a
            tj = (j//3)*3+b
            if ti != i or tj != j:
                if grid[ti][tj] == grid[i][j]:
                    return True
    return False

def brutalforce(grid):
    #showGrid(grid)
    o = []
    for i in range(9):
        o.append([False]*9)
    for i in range(9):
        for j in range(9):
            if grid[i][j] > 0:
                o[i][j] = True
    i = 0
    j = 0
    while True:
        if not o[i][j]:
            grid[i][j] += 1
            if grid[i][j] > 9:
                grid[i][j] = 0
                while True:
                    j -= 1
                    if j == -1:
                        i -= 1
                        j = 8
                    if not o[i][j]:
                        break
                continue
            if conflict(grid,i,j):
                continue
        j += 1
        if j == 9:
            i += 1
            j = 0

        if i == 9:
            break
    #showGrid(grid)    
    return solved(grid)

total = 0

for i in range(1,51):
    gsdk = toGrid(sdk[i])
    if brutalforce(gsdk):
        total += get3d(gsdk)
    else:
        showGrid(gsdk)

print(total)

print("time:",time.time()-t1)
    
