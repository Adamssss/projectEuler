import time

t1 = time.time()

# i-1 kinds of number make of i
# f(i,j) = f(i-1,j)+f(i,j-Pi)

def f(i,j):
    if i == 1:
        return 1
    if i == 0:
        return 0
    if j < 0:
        return 0
    if j == 0:
        return 1
    if i > j:
        return f(j,j)
    return f(i-1,j)+f(i,j-i)

print(f(99,100))

print("time:",time.time()-t1)
