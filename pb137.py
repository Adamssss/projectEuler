import math
import time

t1 = time.time()

# AF(x) = xF1+x^2F2+x^3F3+...
# AF(x)*x = x^2F1+x^3F2+....
# AF(x)*(1+x) = xF1+x^2(F1+F2)+x^3(F2+F3)+...
# AF(x)*(1+x)-x = x^2F3+x^3F4+...
# AF(x)*(1+x)-x = (AF(x)-x-x^2)/x
# AF(x)*(x+x^2)-x^2 = AF(x)-x-x^2
# x = AF(x)*(1-x-x^2)
# AF(x) = x/(1-x-x^2)

'''
# test the result
x = math.sqrt(2)-1
print(x/(1-x-x*x))
x = 1/2
print(x/(1-x-x*x))
x = (math.sqrt(13)-2)/3
print(x/(1-x-x*x))
x = (math.sqrt(89)-5)/8
print(x/(1-x-x*x))
x = (math.sqrt(34)-3)/5
print(x/(1-x-x*x))
'''

# AF(x) = n = x/(1-x-x^2)
# n-nx-nx^2 = x
# nx^2+(n+1)x-n = 0
# delta = (n+1)^2+4n^2
# sqrt(delta) must be integer
# (aa-bb)^2 + (2ab)^2 = (aa+bb)^2
# n+1 = aa-bb = (a-b)(a+b)
# n = ab

# (a+b)(a+2b) = aa+3ab+2bb
# (a+2b)^2-(a+b)^2 = 2ab+3bb
# if aa-ab-bb = 1
# a,b & a+b,a+2b are two solutions to n

# for a = 1, b = 2
# 3,5   3*5+1 = 5*5-3*3
# 8,13  8*13+1 = 13*13-8*8

a = 1
b = 2
n = a*b
for i in range(14):
    a = a+b
    b = a+b
    n = a*b
    
print(n)
    
print("time:",time.time()-t1)  


    
