import math
import time

t1 = time.time()

# a
#   H -> (1+2f)*a
#   T ->  (1-f)*a

# r = (1+2f)^h*(1-f)^(1000-h)
#   = ((1+2f)/(1-f))^h*(1-f)^1000

# h >= log(r/(1-f)^1000)/log((1+2f)/(1-f))
#   >= (log(r)-1000*log(1-f))/(log(1+2f)-log(1-f))

# Find f Min: (log(r)-1000*log(1-f))/(log(1+2f)-log(1-f))

'''
# failed to use derivative approach
# achieved to find 431.25+ by testing by hand

r = 1000000000

fmin = 0.00001
fmax = 0.99999


# derivative of min h
def getdh(f):
    return 0


def geth(f):
    return (math.log(r)-1000*math.log(1-f))/(math.log(1+2*f)-math.log(1-f))


for i in range(1,10):
    f = i/5000+0.146
    print(f,geth(f))

'''

# find that h >= 432 when f is around 0.147

# so the sum of chances of getting more than 431 heads out of 1000 flips

fact = [0]*1001

fact[0] = 1
for i in range(1,1000+1):
    fact[i] = fact[i-1]*i

r = 0
for i in range(432,1000+1):
    r += fact[1000]//fact[i]//fact[1000-i]

r = r/math.pow(2,1000)

print(round(r*(10**12))/(10**12))

print("time:",time.time()-t1)  


    
