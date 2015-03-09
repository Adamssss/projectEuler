import time

t1 = time.time()

# factor
def fact(x):
    if x == 1:
        return 1
    if x > 1:
        return x*fact(x-1)

number = str(fact(100))
sumOfDigits = 0
for i in range(0,len(number)):
    sumOfDigits += ord(number[i])-48

print (sumOfDigits)

print("time:",time.time()-t1)
