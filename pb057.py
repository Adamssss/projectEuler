import math

it = []
it.append([3,2])
# the relationship between iterations can be easily deducted
# a(n+1) = 1+ 1/(a(n)+1)
for i in range(1,1000):
    a = 2*it[i-1][1] + it[i-1][0]
    b = it[i-1][1] + it[i-1][0]
    it.append([a,b])

count = 0
for i in range(0,1000):
    dig1 = math.floor(math.log10(it[i][0]))+1
    dig2 = math.floor(math.log10(it[i][1]))+1
    if dig1-dig2 == 1:
        count += 1

print (count)
