import time

t1 = time.time()

fifthPower = []
for i in range(0,10):
    fifthPower.append(i*i*i*i*i)

numbers = []
for i in range(2,299999):
    iorigin = i
    temp = 0
    for j in range(0,6):
        temp += fifthPower[i%10]
        i = i//10
    if temp == iorigin:
        numbers.append(iorigin)
        
total = 0
for i in range(0,len(numbers)):
    total += numbers[i]

print(total)

print("time:",time.time()-t1)
