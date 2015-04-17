import time

t1 = time.time()

def toArray(num):
    temp = []
    while num > 0:
        temp.append(num%10)
        num = num//10
    return temp

def isPalindrome(lst):
    for i in range(0,len(lst)//2):
        if lst[i] != lst[-1-i]:
            return False
    return True

largest = 0
for i in range(900,1000):
    for j in range(900,1000):
        number = i*j
        if isPalindrome(toArray(number)):
            if largest < number:
                largest = number

              
print (largest)

print("time:",time.time()-t1)
