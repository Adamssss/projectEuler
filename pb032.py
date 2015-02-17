# list the first five numbers
# there is no way that 10*1000 or 100*100 can be 3 digits

allTheSeq = []
allTheSeq.append([1,2,3,4,5])

def dfs(seq,x):
    #print(seq,x)
    L = 5
    Q = 6
    if seq[0] > Q:
        return seq
    temp = seq[:]
    if x == L-1 and(not temp[x] in temp[0:x]) and temp[x] <= Q:
        print (temp)
    if x == 0:
        temp[x+1] = 1
        x += 1
    elif x < L-1 and (not temp[x] in temp[0:x]) and temp[x] <= Q:
        temp[x+1] = 1
        x += 1
    else:
        temp[x] += 1
        if temp[x] > Q:
            temp[x-1] += 1
            temp[x] = 1
            x -= 1

    dfs(temp,x)
        
            



        

        
dfs([1,2,3,4,5],4)
    
        
