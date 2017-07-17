import math
import time

t1 = time.time()

# read the trianlges into a list
f = open('pb102_triangles.txt','r')

tris= f.read().split('\n')

f.close()

def totri(tl):
    triangle = []
    temp = tl.split(',')
    for i in range(0,3):
        triangle.append([tonumber(temp[2*i]),tonumber(temp[2*i+1])])
    return triangle

def tonumber(ts):
    neg = False
    result = 0
    temp = ts[:]
    if temp[0] == '-':
        neg = True
        temp = temp[1:]
    for i in temp:
        result = result*10 + ord(i)-48
    if neg:
        result *= -1
    return result

def contain(tri):
    if not onthesameside(tri[0],tri[1],tri[2]):
        return False
    if not onthesameside(tri[1],tri[2],tri[0]):
        return False
    if not onthesameside(tri[2],tri[0],tri[1]):
        return False
    return True

def onthesameside(A,B,C):
    BA = [A[0]-B[0],A[1]-B[1]]
    BO = [-B[0],-B[1]]
    BC = [C[0]-B[0],C[1]-B[1]]
    k = BO[1]/BO[0]
    if BA[0]*k > BA[1] and BC[0]*k > BC[1]:
        return False
    if BA[0]*k < BA[1] and BC[0]*k < BC[1]:
        return False
    return True

count = 0   
for i in range(0,1000):
    if contain(totri(tris[i])):
        count += 1

print(count)

print("time:",time.time()-t1)
    
