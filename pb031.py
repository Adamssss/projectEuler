import time

t1 = time.time()

# f(i,j) = f(i-1,j)+f(i,j-Pi)
# i kinds of notes to make up money equals j


coins = [1,2,5,10,20,50,100,200]

def f(i,j):
    if i == 1:
        return 1
    if i == 0:
        return 0
    if j < 0:
        return 0
    if j == 0:
        return 1
    return f(i-1,j)+f(i,j-coins[i-1])

    
print (f(8,200))

print("time:",time.time()-t1)
