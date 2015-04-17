import time

t1 = time.time()

power = 15
number = [8,6,7,2,3]

while power < 1000:
    for i in range(0,len(number)):
        number[i] = 2*number[i]

    for i in range(0,len(number)-1):
        if number[i] > 9:
            number[i+1] += 1
            number[i] -= 10

    if number[len(number)-1] >9:
        number[len(number)-1] -= 10
        number.append(1)

    power += 1

sums = 0
for i in range(0,len(number)):
    sums += number[i]

print (sums)

print("time:",time.time()-t1)
