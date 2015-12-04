import time

t1 = time.time()

# read the ciphers into a list
f = open('pb059_cipher.txt','r')

ciphers = f.read().split(',')

f.close()

last = ciphers[-1][:-1]
ciphers = ciphers[:-1]
ciphers.append(last)

def tonumber(s):
    r = []
    for i in s:
        temp = 0
        for j in i:
            dig = ord(j)-48
            temp = temp*10 + dig
        r.append(temp)
    return r
        
ciphers = tonumber(ciphers)

def decrypt(key):
    k = 0
    temp = ciphers[:]
    for i in range(0,len(temp)):
        temp[i] = temp[i]^key[k]
        k += 1
        if k == 3:
            k = 0
    return temp

def show(cipher):
    line = ""
    for i in range(0,len(cipher)):
        line += chr(cipher[i])
    print(line)

def english(cipher):
    aas = 0
    ees = 0
    iis = 0
    oos = 0
    jjs = 0
    qqs = 0
    xxs = 0
    zzs = 0
    letters = len(cipher)
    jjl = letters*0.02
    qql = letters*0.01
    xxl = letters*0.01
    zzl = letters*0.01
    for i in range(letters):
        if cipher[i] == 65 or cipher[i] == 97:
            aas += 1
        if cipher[i] == 69 or cipher[i] == 101:
            ees += 1
        if cipher[i] == 73 or cipher[i] == 105:
            iis += 1
        if cipher[i] == 79 or cipher[i] == 111:
            oos += 1
            
        if cipher[i] == 74 or cipher[i] == 106:
            jjs += 1
            if jjs > jjl:
                return False
        if cipher[i] == 81 or cipher[i] == 113:
            qqs += 1
            if qqs > qql:
                return False
        if cipher[i] == 88 or cipher[i] == 120:
            xxs += 1
            if xxs > xxl:
                return False
        if cipher[i] == 90 or cipher[i] == 122:
            zzs += 1
            if zzs > zzl:
                return False
    
    if aas/letters < 0.04:
        return False
    if ees/letters < 0.09:
        return False
    if iis/letters < 0.05:
        return False
    if oos/letters < 0.05:
        return False

    return True
    
def sumOf(cipher):
    total = 0
    for i in range(0,len(cipher)):
        total += cipher[i]
    print (total)

def getkey():
    for i in range(97,123):
        for j in range(97,123):
            for k in range(97,123):
                temp = decrypt([i,j,k])
                if english(temp):
                    #print(i,j,k)
                    #show(temp)
                    sumOf(temp)
                    return

getkey()
         
print("time:",time.time()-t1)


