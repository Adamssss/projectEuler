
# read the ciphers into a list
f = open('pb059_cipher.txt','r')

ciphers = f.read().split(',')

f.close()

for i in range(0,len(ciphers)-1):
    temp = 0
    for j in range(0,len(ciphers[i])):
        dig = ord(ciphers[i][j]) -48
        temp = temp*10 + dig
    ciphers[i] = temp

temp = 0
for j in range(0,len(ciphers[-1])-1):
    dig = ord(ciphers[-1][j]) -48
    temp = temp*10 + dig
ciphers[-1] = temp

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
    for i in range(0,letters):
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
        if cipher[i] == 81 or cipher[i] == 113:
            qqs += 1
        if cipher[i] == 88 or cipher[i] == 120:
            xxs += 1
        if cipher[i] == 90 or cipher[i] == 122:
            zzs += 1
    
    if aas/letters < 0.04:
        return False
    if ees/letters < 0.09:
        return False
    if iis/letters < 0.05:
        return False
    if oos/letters < 0.05:
        return False
    if jjs/letters > 0.02:
        return False
    if qqs/letters > 0.01:
        return False
    if xxs/letters > 0.01:
        return False
    if zzs/letters > 0.01:
        return False
    
    return True
    
def sumOf(cipher):
    total = 0
    for i in range(0,len(cipher)):
        total += cipher[i]
    print (total)
          
for i in range(97,123):
    for j in range(97,123):
        for k in range(97,123):
            temp = decrypt([i,j,k])
            if english(temp):
                #print(i,j,k)
                #show(temp)
                sumOf(temp)

