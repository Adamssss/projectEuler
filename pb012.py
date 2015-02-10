# prime number generator copied from pb 7


a = [2,3,5]
n = 2

while n < 2000:
    b = a[n]
    t = 1
    while (t == 1):
        b = b+2
        i = 0
        t = 0
        while (a[i]*a[i] < b)and (t == 0):
            i=i+1
            if (b%a[i] == 0):
                t = 1

                
        if (t == 0):
            n = n+1
            a.append(b)

# to find out how many divisors
def dvsr(number):
    dvsrs = 1
    i = 0
    count = 0
    while number >1:
        while(number%a[i] == 0):
            count=count+1
            number = number / a[i]
            
        if count > 0:
            dvsrs = dvsrs * (count +1)
            count = 0
            
        i = i+1

    return dvsrs


# main program

requirement = 0
triangle = 2
while requirement == 0:
    triangleNumber = 0
    for i in range(1,triangle+1):
        triangleNumber = triangleNumber +i

    if dvsr(triangleNumber)> 500:
        requirement = 1
        print (triangleNumber)

    triangle = triangle + 1
    
    
    
        

            
