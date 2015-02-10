# code copy from pb007

a = [2,3,5]
n = 2

while a[n]<2000000:
    b = a[n]
    t = 1
    while (t == 1):
        b = b+2
        i = 0
        t = 0
        while (a[i]*a[i] < b) and( t==0 ):
            i=i+1
            if (b%a[i] == 0):
                t = 1

                
        if (t == 0):
            n = n+1
            a.append(b)


totalSum = 0
for i in range(0,n):
    totalSum = totalSum + a[i]

print (totalSum)


                
