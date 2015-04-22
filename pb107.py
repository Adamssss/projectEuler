import math
import time

t1 = time.time()

# read the networks into a list
f = open('pb107_network.txt','r')

networks= f.read().split('\n')

f.close()

def tonumber(E):
    result = 0
    for i in E:
        result = result*10+ord(i)-48
    return result

size = 40

nodes = []
for i in range(size):
    nodes.append([i])

edges = []
for i in range(size):
    temp = networks[i].split(',')
    for j in range(i+1,size):
        if temp[j] != '-':
            edges.append([tonumber(temp[j]),i,j])

'''
# test case
size = 7
nodes = []
for i in range(size):
    nodes.append([i])
edges = []
edges.append([16,0,1])
edges.append([12,0,2])
edges.append([21,0,3])
edges.append([17,1,3])
edges.append([20,1,4])
edges.append([28,2,3])
edges.append([31,2,5])
edges.append([18,3,4])
edges.append([19,3,5])
edges.append([23,3,6])
edges.append([11,4,6])
edges.append([27,5,6])
'''

def quickSort(L, low, high):
    i = low 
    j = high
    if i >= j:
        return L
    key = L[i]
    while i < j:
        while i < j and L[j] >= key:
            j = j-1                                                             
        L[i] = L[j]
        while i < j and L[i] <= key:    
            i = i+1 
        L[j] = L[i]
    L[i] = key 
    quickSort(L, low, i-1)
    quickSort(L, j+1, high)
    return L

def nodeindex(n):
    for i in range(len(nodes)):
        if n in nodes[i]:
            return i       

def testedge(edge):
    global nodes
    a = edge[1]
    b = edge[2]
    ia = nodeindex(a)
    ib = nodeindex(b)
    if ia == ib:
        return False
    temp = nodes[ia][:]+nodes[ib][:]
    if ia < ib:
        nodes.pop(ia)
        nodes.pop(ib-1)
    else:
        nodes.pop(ib)
        nodes.pop(ia-1)
    nodes.append(temp[:])
    return True

def solve():
    global edges
    edges = quickSort(edges,0,len(edges)-1)
    ow = 0
    nw = 0
    for i in edges:
        ow += i[0]
        if len(nodes)>1 and testedge(i):
            #print(nodes)
            nw += i[0]
    return ow-nw

print(solve())

print("time:",time.time()-t1)  


    
