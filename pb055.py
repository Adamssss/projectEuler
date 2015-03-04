# use array to represent numbers backwards
def toArray(num):
    a = []
    while num >0:
        a.append(num%10)
        num = num //10

    return a

def addReverse(x):
    result = []
    for i in range(0,len(x)):
        result.append(x[i]+x[len(x)-1-i])
    for i in range(0,len(result)-1):
        if result[i] > 9:
            result[i] -= 10
            result[i+1] += 1
    if result[-1] > 9:
        result[-1] -= 10
        result.append(1)
    return result

def isPalindrome(x):
    for i in range(0,len(x)//2):
        if x[i] != x[len(x)-1-i]:
            return False
    return True

def isLychrel(x,it):
    if it >= 50:
        return True
    if it > 0 and isPalindrome(x):
        return False
    return isLychrel(addReverse(x),it+1)


count = 0
for i in range(1,10001):
    if isLychrel(toArray(i),0):
        count += 1
print (count)       
    
