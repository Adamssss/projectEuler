import time

t1 = time.time()

# read the triangle into a list
f = open('pb067_triangle.txt','r')

rows = f.read().split('\n')

f.close()

numbers = {}

maxNumbers = {}

r = 100

for i in range(0,r):
    for j in range(0,r):
        numbers[i,j] = 0
        maxNumbers[i,j] = 0

# turn the numbers into a matrix of numbers

for i in range(0,r):
    for j in range(0,i+1):
        dig = j*3
        n1 = ord(rows[i][dig])-48
        n2 = ord(rows[i][dig+1])-48
        numbers[i,j] = n1*10+n2

maxNumbers[0,0] = numbers[0,0]

# produce a matrix match the max sum of the numbers 


for i in range(1,r):
    for j in range(0,i+1):
        if j == 0:
            maxNumbers[i,j] = numbers[i,j] + maxNumbers[i-1,j]

        if j == i:
            maxNumbers[i,j] = numbers[i,j] + maxNumbers[i-1,j-1]

        if j > 0 and j < i:
            if maxNumbers[i-1,j] >= maxNumbers[i-1,j-1]:
                maxNumbers[i,j] = numbers[i,j] + maxNumbers[i-1,j]
                
            if maxNumbers[i-1,j] < maxNumbers[i-1,j-1]:
                maxNumbers[i,j] = numbers[i,j] + maxNumbers[i-1,j-1]

# find the largest in the last row

largest = 0
for i in range(0,r):
    if maxNumbers[r-1,i] > largest:
        largest = maxNumbers[r-1,i]

print (largest)
                
print("time:",time.time()-t1)
                
