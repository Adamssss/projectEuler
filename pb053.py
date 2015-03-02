fact = [1]

for i in range(1,101):
    fact.append(fact[i-1]*i)


def C(n,r):
    return fact[n]//fact[r]//fact[n-r]

count = 0

for i in range(1,101):
    for j in range(1,i+1):
        if C(i,j) > 1000000:
            count += 1

print (count)
