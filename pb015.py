import time

t1 = time.time()

matrix ={}
# the way to the all first row points are 1
for i in range(0,21):
    matrix[0,i] = 1
# the first column is also 1
for j in range(0,21):
    matrix[j,0] = 1
# the way to the points equal to the ways on the left and top
for i in range(1,21):
    for j in range(1,21):
        matrix[i,j] = matrix[i-1,j] +matrix[i,j-1]

print (matrix[20,20])

print("time:",time.time()-t1)
