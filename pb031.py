coinMakeUp = []
coinMakeUp.append([200,0,0,0,0,0,0,0,0])
# the money that has not be contributed and the coins for
# 200,100,50,20,10,5,2,1
coins = [200,100,50,20,10,5,2,1]

t = 1
while t > 0:
    temp = coinMakeUp[-1][:]
    if temp[0] > 0:
        for i in range(0,8):
            dig = temp[0]//coins[i]
            if dig > 0:
                temp[i+1] += dig
                temp[0] -= dig*coins[i]

        coinMakeUp.append(temp)
        
    else:
        j = 7
        while temp[j] == 0:
            j -= 1

        temp[j] -= 1
        temp[0] += coins[j-1]
        for k in range(j+1,9):
            temp[0] += temp[k]*coins[k-1]
            temp[k] = 0
            
        dig = temp[0]//coins[j]
        temp[j+1] += dig
        temp[0] -= dig*coins[j]
        coinMakeUp.append(temp)
       
    #print(temp)   

    t = 0
    for i in range(0,8):
        t += temp[i]


count = 0
for i in range(0,len(coinMakeUp)):
    if coinMakeUp[i][0] == 0:
        count += 1
        
print (count)
                


    
