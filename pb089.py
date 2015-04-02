import math
import time

t1 = time.time()

# read the roman numbers into a list
f = open('pb089_roman.txt','r')

rn= f.read().split('\n')

f.close()

def tonumber(rns):
    last = valueof(rns[0])
    result = last
    for i in range(1,len(rns)):
        temp = valueof(rns[i])
        if temp <= last:
            result += temp
            last = temp
        else:
            result -= last*2
            result += temp
            last = temp
    return result

def valueof(c):
    if c == 'I':
        return 1
    if c == 'V':
        return 5
    if c == 'X':
        return 10
    if c == 'L':
        return 50
    if c == 'C':
        return 100
    if c == 'D':
        return 500
    if c == 'M':
        return 1000

def toroman(num):
    result = ''
    while num >= 1000:
        result += 'M'
        num -= 1000
    
    h = num//100
    num = num%100
    if h == 4:
        result += 'CD'
        h = 0
    if h == 9:
        result += 'CM'
        h = 0
    if h >= 5:
        result += 'D'
        h -= 5
    while h > 0:
        result += 'C'
        h -= 1
    
    t = num//10
    num = num%10
    if t == 4:
        result += 'XL'
        t = 0
    if t == 9:
        result += 'XC'
        t = 0
    if t >= 5:
        result += 'L'
        t -= 5
    while t > 0:
        result += 'X'
        t -= 1

    d = num
    if d == 4:
        result += 'IV'
        d = 0
    if d == 9:
        result += 'IX'
        d = 0
    if d >= 5:
        result += 'V'
        d -= 5
    while d > 0:
        result += 'I'
        d -= 1
    return result

count = 0

for i in rn:
    count += len(i)
    count -= len(toroman(tonumber(i)))

print(count)

print("time:",time.time()-t1)
    
