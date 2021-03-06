import time

t1 = time.time()

# string ddeducted with winword

string = "75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"

# string = "03 07 04 02 04 06 08 05 09 03"

numbers = {}

maxNumbers = {}

r = 15

for i in range(0,r):
    for j in range(0,r):
        numbers[i,j] = 0
        maxNumbers[i,j] = 0

# turn the numbers into a matrix of numbers

for i in range(0,r):
    for j in range(0,i+1):
        dig =((i*(i+1))//2)*3 + j*3
        n1 = ord(string[dig])-48
        n2 = ord(string[dig+1])-48
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
                
