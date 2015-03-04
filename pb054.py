import math

# read the pokers into a list
f = open('pb054_poker.txt','r')

games = f.read().split('\n')

f.close()

# return the cards and the sixth term indicates same suit or not
def cards(game,player):
    c = [0,0,0,0,0,1]
    p = game[1+(player-1)*15]
    for i in range(0,5):
        c[i] = ord(game[3*i+(player-1)*15])-48
        if game[1+3*i+(player-1)*15] != p:
            c[5] = 0
        if c[i] == 27:
            c[i] = 13
        elif c[i] == 26:
            c[i] = 11
        elif c[i] == 36:
            c[i] = 10
        elif c[i] == 33:
            c[i] = 12
        elif c[i] == 17:
            c[i] = 14

    return c

# sort the first five terms
def sort(c):
    for i in range(0,4):
        for j in range(0,4-i):
            if c[4-j] < c[3-j]:
                temp = c[3-j]
                c[3-j] = c[4-j]
                c[4-j] = temp

    return c


# return the value of the hand
def showhand(c):
    
    #Royal Flush
    if c == [10,11,12,13,14,1]:
        return 99*math.pow(10,10)

    # straight
    st = 0
    if c[4]-c[3] == 1:
        if c[3]-c[2] == 1:
            if c[2] -c[1] == 1:
                if c[1] - c[0] == 1:
                    st = 1

    #Straight Flush
    if c[5] == 1:
        if st == 1:
            v = 98*math.pow(10,10)+c[4]*math.pow(10,8)
            return v

    tc = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(0,5):
        tc[c[i]-2] += 1
        

    #Four of a Kind
    if 4 in tc:
        v = 80*math.pow(10,10)
        a = tc.index(4)
        b = tc.index(1)
        v += (a+2)*math.pow(10,8)
        v += (b+2)*math.pow(10,6)
        return v

    #Full House
    if 3 in tc and 2 in tc:
        v = 70*math.pow(10,10)
        a = tc.index(3)
        b = tc.index(2)
        v += (a+2)*math.pow(10,8)
        v += (b+2)*math.pow(10,6)
        return v

    #Flush
    if c[5] == 1:
        return 65*math.pow(10,10)

    #Straight
    if st == 1:
        return 60*math.pow(10,10)+c[4]*math.pow(10,8)

    #Three of a kind
    if 3 in tc:
        v = 50*math.pow(10,10)
        a = tc.index(3)
        v += (a+2)*math.pow(10,8)
        c = tc.index(1)
        b = tc[c+1:].index(1) +c+1
        v += (b+2)*math.pow(10,6)
        v += (c+2)*math.pow(10,4)
        return v

    #Two Pairs
    if 2 in tc:
        b = tc.index(2)
        if b!= 12 and 2 in tc[b+1:]:
            a = tc[b+1:].index(2) +b+1
            c = tc.index(1)
            v = 30*math.pow(10,10)
            v += (a+2)*math.pow(10,8)
            v += (b+2)*math.pow(10,6)
            v += (c+2)*math.pow(10,4)
            return v

    #One Pair
    if 2 in tc:
        a = tc.index(2)
        d = tc.index(1)
        c = tc[d+1:].index(1) +d+1
        b = tc[c+1:].index(1) +c+1
        v = 15*math.pow(10,10)
        v += (a+2)*math.pow(10,8)
        v += (b+2)*math.pow(10,6)
        v += (c+2)*math.pow(10,4)
        v += (d+2)*math.pow(10,2)
        return v

    #High Card
    v = 1*math.pow(10,10)
    v += c[4]*math.pow(10,8)
    v += c[3]*math.pow(10,6)
    v += c[2]*math.pow(10,4)
    v += c[1]*math.pow(10,2)
    v += c[0]*math.pow(10,0)
    return v
    
    
# count player 1 win    
cp1w = 0

for i in range(0,1000):
    p1 = sort(cards(games[i],1))
    p2 = sort(cards(games[i],2))
    if showhand(p1) > showhand(p2):
        cp1w += 1

print (cp1w)
    
