
cases =[]
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            for l in range(1,10):
                cases.append([i,j,k,l])

def test(case):
    a = case[0]*10 + case[1]
    b = case[2]*10 + case[3]
    t = 0
    if a == b or a > b:
        return 1
    if a/b == case[0]/case[2] and case[1] == case[3]:
        t = 1
    if a/b == case[1]/case[2] and case[0] == case[3]:
        t = 1
    if a/b == case[0]/case[3] and case[1] == case[2]:
        t = 1
    if a/b == case[1]/case[3] and case[0] == case[2]:
        t = 1

    if t == 1:
        #print (case)
        return b/a
    if t == 0:
        return 1

product = 1
for i in range(0,len(cases)):
    product *= test(cases[i])

print (product)
