import math
import time

t1 = time.time()

def digToNumber(num):
    result = 0
    while num>0:
        a = num%10
        result += math.pow(10,a)
        num = num//10
    return int(result)

def insert(my_list,item):
    for i in range(0,len(my_list)):
        if my_list[i][0] > item[0]:
            my_list.insert(i,item)
            return my_list
    my_list.append(item)
    return my_list

# define a binary search 
def isInList(item,lst):
    firstPoint = 0
    endPoint = len(lst)-1
    index = -1
    while firstPoint <= endPoint:
        midPoint = (firstPoint+endPoint)//2
        if lst[midPoint][0] == item:
            index = midPoint
            return index
        elif item > lst[midPoint][0]:
            firstPoint = midPoint +1
        else:
            endPoint = midPoint -1

    return index

whole = []
whole.append([digToNumber(1),1,1])
whole.append([digToNumber(8),1,2])

for i in range(3,15000):
    c = i*i*i
    n = digToNumber(c)
    t = isInList(n,whole)
    if t < 0:
        insert(whole,[n,1,i])
    else:
        whole[t][1] += 1
        whole[t].append(i)
        if whole[t][1] == 5:
            print (math.pow(whole[t][2],3))
            break

print("time:",time.time()-t1)
