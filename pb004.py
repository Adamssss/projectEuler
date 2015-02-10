
largestNumber = 0
for i in range(900,1000):
    for j in range(900,1000):
        number = i*j
        dig = []
        dig.append(number//100000)
        dig.append(number//10000-dig[0]*10)
        dig.append(number//1000-(number//10000)*10)
        dig.append(number//100-(number//1000)*10)
        dig.append(number//10-(number//100)*10)
        dig.append(number%10)
        if dig[0] == dig[5]:
            if dig[1] == dig[4]:
                if dig[2] == dig[3]:
                    if number > largestNumber:
                        largestNumber = number

              
print (largestNumber)
