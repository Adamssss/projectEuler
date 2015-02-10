a = [2,3,5]
n = 2
while n < 10000:
    b = a[n]
    t = 1
    while (t == 1):
        b = b+2
        i = 0
        t = 0
        while (i < n):
            i=i+1
            if (b%a[i] == 0):
                t = 1

                
        if (t == 0):
            print (b)
            n = n+1
            a.append(b)

                
