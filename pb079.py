import time

t1 = time.time()

# read the keys into a list
f = open('pb079_keylog.txt','r')

keyslog = f.read().split('\n')

f.close()

keys = []

for i in range(0,50):
    a = ord(keyslog[i][0])-48
    b = ord(keyslog[i][1])-48
    c = ord(keyslog[i][2])-48
    keys.append([a,b,c])

ok = []

def inok(test):
    if not test[0] in ok:
        return False
    a = ok.index(test[0])
    if not test[1] in ok:
        return False
    b = ok.index(test[1])
    if a > b:
        return False
    if not test[2] in ok:
        return False
    c = ok.index(test[2])
    if b > c:
        return False
    return True

def cleank():
    global keys
    temp = []
    for i in keys:
        if not inok(i):
            temp.append(i)
    keys = temp
    
ok = keys[0][:]
cleank()

while True:
    
    j = 0
    k = True
    while j < len(ok)-1 and k:
        for i in keys:
            if ok[j] == i[0] and ok[j+1] == i[2]:
                k = False
                ok.insert(j+1,i[1])
                break
        j += 1

    for i in keys:
        if i[1] == ok[0] and i[2] in ok:
            ok.insert(0,i[0])
            break

    for i in keys:
        if i[1] == ok[-1] and i[0] in ok:
            ok.append(i[2])
            break
    
    cleank()
    if len(keys) == 0:
        break

answer = 0
for i in ok:
    answer = answer*10+i

print(answer)

print("time:",time.time()-t1)
    
