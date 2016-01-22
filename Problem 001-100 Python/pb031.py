import time

t1 = time.time()

# f(i,j) = f(i-1,j)+f(i,j-Pi)
# i kinds of notes to make up money equals j

# dynamic programming 

coins = [1,2,5,10,20,50,100,200]

f =[]
f += [[0]*201]
f += [[1]*201]

for i in range(7):
    f += [[0]*201]

for i in range(2,9):
    c = coins[i-1]
    f[i][0] = 1
    for j in range(1,c):
        f[i][j] = f[i-1][j]
    for j in range(c,201):
        f[i][j] = f[i-1][j]+f[i][j-c]

print(f[8][200])

print("time:",time.time()-t1)
