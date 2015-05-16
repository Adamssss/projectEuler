import math
import time

t1 = time.time()

ul = 25000

# for cuboid a,b,c
# the surface area is 2(ab+bc+ac)
# the length of the side is 4*(a+b+c)
# the vertex is 8*1

# for the nth layer
# the surface area needs to be covered
# (n-1) length of the side needs to be covered
# 1+2+3+...+(n-2) vertex needs to be covered

def covernum(cub,layer):
    s = cub[0]*cub[1]+cub[1]*cub[2]+cub[2]*cub[0]
    l = sum(cub)
    result = 2*s+(layer-1)*4*l
    if layer > 2:
        result += 8*(layer-1)*(layer-2)//2
    return result

def testcub():
    temp = []
    # a<=b<=c
    # 2*3*a^2 <= ul
    il = math.floor(math.sqrt(ul/6))+1
    # 4*a*b+2*b^2 <= ul
    jl = math.floor(math.sqrt(ul/2))
    # 2*a^2+4*a*c <= ul
    for i in range(1,il):
        for j in range(i,jl):
            for k in range(j,ul//4//i):
                temp.append([i,j,k])
    return temp

C = [0]*ul

for i in testcub():
    #j = 1
    #temp = covernum(i,j)
    temp = 2*(i[0]*i[1]+i[1]*i[2]+i[2]*i[0])
    l = 4*sum(i)
    v = -8
    while temp < ul:
        C[temp] += 1
        #j += 1
        #temp = covernum(i,j)
        v += 8
        temp += l+v

for i in range(154,ul,2):
    if C[i] == 1000:
        print(i)
        break

print("time:",time.time()-t1)  


    
