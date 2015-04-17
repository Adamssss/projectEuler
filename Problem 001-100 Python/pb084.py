import math
import time
import random

t1 = time.time()

# run a simluation of playing the game
# Turns:
T = 1000000

# dice side:
D = 4

def rollthedice():
    return [random.randint(1,D),random.randint(1,D)]

def isdouble(dices):
    return dices[0] == dices[1]

# the grid visited
E = [0]*40

# current at & doubles
ca = 0
ds = 0

def moveto(square):
    #print('you are now at:',square)
    global E,ca
    ca = square
    E[ca] += 1
    return ca

def playaturn():
    global E,ca,ds
    dices = rollthedice()
    
    #print('you rolled:',dices)
    
    if isdouble(dices):
        ds += 1
    else:
        ds = 0
    # 3 doubles go to jail rule
    if ds == 3:
        ds = 0
        return moveto(10)
    # move forward
    steps = dices[0]+dices[1]
    ca += steps
    if ca >= 40:
        ca -= 40
    # specials rulse:
    # go to jail
    if ca == 30:
        return moveto(10)
    # community chest
    if ca == 2 or ca == 17 or ca == 33:
        cc = random.randint(1,16)
        # 1 advance to go
        if cc == 1:
            return moveto(0)
        # 2 go to jail
        if cc == 2:
            return moveto(10)
    # chance
    if ca == 7 or ca == 22 or ca == 36:
        ch = random.randint(1,16)
        # 1 advance to go
        if ch == 1:
            return moveto(0)
        # 2 go to jail
        if ch == 2:
            return moveto(10)
        # 3 go to c1
        if ch == 3:
            return moveto(11)
        # 4 go to e3
        if ch == 4:
            return moveto(24)
        # 5 go to h2
        if ch == 5:
            return moveto(39)
        # 6 go to r1
        if ch == 6:
            return moveto(5)
        # 7/8 go to next r
        if ch == 7 or ch == 8:
            if ca == 7:
                return moveto(15)
            if ca == 22:
                return moveto(25)
            if ca == 36:
                return moveto(5)
        # 9 go the next u
        if ch == 9:
            if ca == 7 or ca == 36:
                return moveto(12)
            if ca == 22:
                return moveto(28)
        # 10 go back 3 squares
        if ch == 10:
            ca -= 3
    # nothing special
    return moveto(ca)

for i in range(0,T):
    playaturn()

def stringnumber(num):
    a = num//10
    b = num%10
    return chr(a+48)+chr(b+48)

def toprobability(temp):
    a = math.floor(temp*100)
    b = math.floor(temp*1000)-10*a
    c = math.floor(temp*10000)-100*a-10*b
    return chr(a+48)+'.'+chr(b+48)+chr(c+48)+'%'
    

def showgrid():
    for i in range(0,40):
        temp = E[i]/T
        output = 'square'+stringnumber(i)
        output += ' has probability of '+toprobability(temp)
        print(output)

#showgrid()

def answer():
    first = 0
    ef = 0
    second = 0
    es = 0
    third = 0
    et = 0
    for i in range(0,40):
        if E[i] > ef:
            ef = E[i]
            first = i
    for i in range(0,40):
        if E[i] > es and E[i] < ef:
            es = E[i]
            second = i
    for i in range(0,40):
        if E[i] > et and E[i] < es:
            et = E[i]
            third = i
    result = stringnumber(first)
    result += stringnumber(second)
    result += stringnumber(third)
    return result

print(answer())    
  
print("time:",time.time()-t1)
    


    
