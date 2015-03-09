import time

t1 = time.time()

count = 0
for i in range(1,1001):
    #one 3
    if i%10 == 1:
        count += 3
        
    #two 3
    if i%10 == 2:
        count += 3
        
    #three 5
    if i%10 == 3:
        count += 5

    #four 4
    if i%10 == 4:
        count += 4

    #five 4
    if i%10 == 5:
        count += 4

    #six 3
    if i%10 == 6:
        count += 3 

    #seven 5
    if i%10 == 7:
        count += 5

    #eight 5
    if i%10 == 8:
        count += 5

    #nine 4
    if i%10 == 9:
        count += 4

    #ten 3
    if i%100 == 10:
        count += 3

    #eleven from one 6-3
    if i%100 == 11:
        count += 3

    #twelve from two 6-3
    if i%100 == 12:
        count += 3

    #thirteen from three 8-5
    if i%100 == 13:
        count += 3

    #fourteen from four 8-4
    if i%100 == 14:
        count += 4

    #fifteen from five 7-4
    if i%100 == 15:
        count += 3

    #sixteen from six 7-3
    if i%100 == 16:
        count += 4

    #seventeen from seven 9-5
    if i%100 == 17:
        count += 4

    #eighteen from eight 8-5
    if i%100 == 18:
        count += 3

    #nineteen from nine 8-4
    if i%100 == 19:
        count += 4

    #twenty 6
    if i%100 > 19 and i%100 < 30:
        count += 6

    #thirty 6
    if i%100 > 29 and i%100 < 40:
        count += 6

    #forty 5
    if i%100 > 39 and i%100 < 50:
        count += 5

    #fifty 5
    if i%100 > 49 and i%100 < 60:
        count += 5

    #sixty 5
    if i%100 > 59 and i%100 < 70:
        count += 5

    #seventy 7
    if i%100 > 69 and i%100 < 80:
        count += 7

    #eighty 6
    if i%100 > 79 and i%100 < 90:
        count += 6

    #ninety 6
    if i%100 > 89:
        count += 6

    #hundred 7
    if i > 99 and i%1000 > 0:
        count += 7
        
    #one h 3
    if i//100 == 1:
        count += 3
        
    #two h 3
    if i//100 == 2:
        count += 3
        
    #three h 5
    if i//100 == 3:
        count += 5

    #four h 4
    if i//100 == 4:
        count += 4

    #five h 4
    if i//100 == 5:
        count += 4

    #six h 3
    if i//100 == 6:
        count += 3 

    #seven h 5
    if i//100 == 7:
        count += 5

    #eight h 5
    if i//100 == 8:
        count += 5

    #nine h 4
    if i//100 == 9:
        count += 4

    #and (from 101) 3
    if i > 100 and i%100 > 0:
        count += 3

    #thousand 8
    if i > 999:
        count += 8

    #one t 3
    if i//1000 == 1:
        count += 3
    

print (count)
    
print("time:",time.time()-t1)
