i = 9876
t = 0
while t == 0:
    i -= 1
    temp = i
    stop = 0
    num = []
    numl = [1,2,3,4,5,6,7,8,9]
    for j in range(0,4):
        num.append(temp%10)
        temp = temp//10
        if num[j] in numl:
            numl.remove(num[j])
        else:
            stop = 1
    if stop == 0:
        temp = i*2
        for j in range(4,9):
            num.append(temp%10)
            temp = temp//10
            if num[j] in numl:
                numl.remove(num[j])
            else:
                stop = 1        
    if stop == 0:
        t = 1

print (i*100002)
