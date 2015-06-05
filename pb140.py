import math
import time

t1 = time.time()

# AG(x) = xG1+x^2G2+x^3G3+...
# AG(x)*x = x^2G1+x^3G2+....
# AG(x)*(1+x) = xG1+x^2(G1+G2)+x^3(G2+G3)+...
# AG(x)*(1+x)-x = x^2G3+x^3G4+...
# AG(x)*(1+x)-x = (AG(x)-x-4x^2)/x
# AG(x)*(x+x^2)-x^2 = AG(x)-x-4x^2
# AG(x)*(x+x^2-1) = -x-3x^2
# AG(x) = (x+3x^2)/(1-x-x^2)

'''
# test the result
x = (math.sqrt(5)-1)/4
print((x+3*x*x)/(1-x-x*x))
x = 2/5
print((x+3*x*x)/(1-x-x*x))
x = (math.sqrt(22)-2)/6
print((x+3*x*x)/(1-x-x*x))
x = (math.sqrt(137)-5)/14
print((x+3*x*x)/(1-x-x*x))
x = 1/2
print((x+3*x*x)/(1-x-x*x))
'''

# AG(x) = n = (x+3*x*x)/(1-x-x*x)
# n-nx-nx^2 = x+3*x*x
# (n+3)x^2+(n+1)x-n = 0
# delta = (n+1)^2+4n^2+12n
# sqrt(delta) must be integer

# 2
# 5
# 21    3*7
# 42    3*14
# 152   8*19
# 296   8*37
# 1050      21*50
# 2037     21*97 
# 7205      55*131

# 1,1,2,3,5,8,13,21,34,55,89,
# 2,5,7,12,19,31,50,81,131,
# 1,4,5,9,14,23,37,60,97,157

tset = [2,5]

a1 = 3
b1 = 5
a2 = 7
b2 = 12
a3 = 14
b3 = 23
while True:
    tset.append(a1*a2)
    tset.append(a1*a3)
    if len(tset) == 30:
        break
    a1 = a1+b1
    b1 = a1+b1
    a2 = a2+b2
    b2 = a2+b2
    a3 = a3+b3
    b3 = a3+b3

print(sum(tset))
    
print("time:",time.time()-t1)  


    
