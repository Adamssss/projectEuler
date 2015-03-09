import time

t1 = time.time()

# read the names into a list
f = open('pb022_names.txt','r')

names = f.read().split(',')

for i in range(0,len(names)):
    names[i] = names[i][1:len(names[i])-1]

f.close()

# sort the names

#quick sort
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



names = quickSort(names,0,len(names)-1)



# get the sum of the score

totalScore = 0
for i in range(0,len(names)):
    position = i+1
    nameScore = 0
    for j in range(0,len(names[i])):
        nameScore += ord(names[i][j])-64

    totalScore += position*nameScore

print(totalScore)

print("time:",time.time()-t1)
    
