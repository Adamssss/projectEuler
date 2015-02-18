# list the first five numbers
# there is no way that 10*1000 or 100*100 can be 3 digits

def test1(seqc):
    seq = seqc[:]
    n1 = 0
    for i in range(0,2):
        n1 = n1*10 + seq[i]
    n2 = 0
    for i in range(2,5):
        n2 = n2*10 + seq[i]
    n3 = n2 * n1
    if n3 > 9876 or n3 < 1234:
        return 0
    temp = [0,0,0,0]
    temp[0] = n3 // 1000
    temp[1] = n3 // 100 - temp[0]*10
    temp[2] = n3 // 10 - temp[0]*100 -temp[1]*10
    temp[3] = n3 % 10
    for i in range(0,4):
        if temp[i] in seq[0:5+i] or temp[i] == 0:
            return 0
        else:
            seq.append(temp[i])

    return n3

#print(test1([3,9,1,8,6]))

def test2(seqc):
    seq = seqc[:]
    n1 = seq[0]
    n2 = 0
    for i in range(1,5):
        n2 = n2*10 + seq[i]
    n3 = n2 * n1
    if n3 > 9876 or n3 < 1234:
        return 0
    temp = [0,0,0,0]
    temp[0] = n3 // 1000
    temp[1] = n3 // 100 - temp[0]*10
    temp[2] = n3 // 10 - temp[0]*100 -temp[1]*10
    temp[3] = n3 % 10
    for i in range(0,4):
        if temp[i] in seq[0:5+i] or temp[i] == 0:
            return 0
        else:
            seq.append(temp[i])

    return n3

# make the possible first 5 numbers
allTheSeq = []

temp = [0,0,0,0,0]
for i in range(1,10):
    temp[0] = i
    for j in range(1,10):
        if not i == j:
            temp[1] = j
            for k in range(1,10):
                if not k in temp[0:2]:
                    temp[2] = k
                    for l in range(1,10):
                        if not l in temp[0:3]:
                            temp[3] = l
                            for m in range(1,10):
                                if not m in temp[0:4]:
                                    temp[4] = m
                                    allTheSeq.append(temp[:])


#print(len(allTheSeq))



possibleSums =[]
for i in range(0,len(allTheSeq)):
    product = test1(allTheSeq[i])
    if product > 0 and not product in possibleSums:
        possibleSums.append(product)
    product = test2(allTheSeq[i])
    if product > 0 and not product in possibleSums:
        possibleSums.append(product)

total = 0
for i in range(0,len(possibleSums)):
    total += possibleSums[i]

print (total)

    
                    
        
