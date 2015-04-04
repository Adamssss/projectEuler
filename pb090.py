import math
import time

t1 = time.time()

# turn dice into a boolean list of ten booleans
# [ 1,2,3,4,5,6] is turned into [F,T,T,T,T,T,T,F,F,F]

def check(dice1,dice2):
    # check digits:0,1,4,2,5,3,8,6or9
    if not (dice1[0] or dice2[0]):
        return False
    if not (dice1[1] or dice2[1]):
        return False
    if not (dice1[4] or dice2[4]):
        return False
    if not (dice1[2] or dice2[2]):
        return False
    if not (dice1[5] or dice2[5]):
        return False
    if not (dice1[3] or dice2[3]):
        return False
    if not (dice1[8] or dice2[8]):
        return False
    if not (dice1[6] or dice2[6] or dice1[9] or dice2[9]):
        return False
    #check combination 01,04,25,81
    if not (dice1[0] or dice1[1]):
        return False
    if not (dice2[0] or dice2[1]):
        return False
    if not (dice1[0] or dice1[4]):
        return False
    if not (dice2[0] or dice2[4]):
        return False
    if not (dice1[2] or dice1[5]):
        return False
    if not (dice2[2] or dice2[5]):
        return False
    if not (dice1[8] or dice1[1]):
        return False
    if not (dice2[8] or dice2[1]):
        return False
    #check combination 09,16,36,49,64
    if not (dice1[0] and (dice2[6] or dice2[9])):
        if not (dice2[0] and (dice1[6] or dice1[9])):
                return False
    if not (dice1[1] and (dice2[6] or dice2[9])):
        if not (dice2[1] and (dice1[6] or dice1[9])):
                return False
    if not (dice1[3] and (dice2[6] or dice2[9])):
        if not (dice2[3] and (dice1[6] or dice1[9])):
                return False
    if not (dice1[4] and (dice2[6] or dice2[9])):
        if not (dice2[4] and (dice1[6] or dice1[9])):
                return False
    return True

dicelist = [[True,1],[False,0]]

def addface(alldice):
    newdice = []
    for i in alldice:
        if len(i)-i[-1] < 5: 
            newdice.append([False]+i)
        if i[-1] < 6:
            i[-1] += 1
            newdice.append([True]+i)
    return newdice

def makedice():
    result = dicelist
    for i in range(0,9):
        result = addface(result)
    return result

def showdice(dice):
    result = []
    for i in range(0,10):
        if dice[i]:
            result.append(i)
    return result

alldice =  makedice()

l = len(alldice)

count = 0

for i in range(0,l):
    for j in range(i,l):
        if check(alldice[i],alldice[j]):
            #print(showdice(alldice[i]),'&',showdice(alldice[j]))
            count += 1
        
print(count)    
  
print("time:",time.time()-t1)
    


    
