import math
import time

t1 = time.time()

# get one color
# = 1 - not get the color
# = 1 - 20 out of 60/20 out of 70
# c(n,k) = # n!/k!/(n-k)!
# 60!/20!/40!/70!*20!*50!
# 60!/70! * 50!/40!

temp = 1
for i in range(41,51):
    temp = temp*i

for i in range(61,71):
    temp = temp/i

pgoc = 1-temp

answer = 7*pgoc

answer = round(answer*math.pow(10,9))/math.pow(10,9)

print(answer)

print("time:",time.time()-t1)  


    
