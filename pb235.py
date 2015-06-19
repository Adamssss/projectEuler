import math
import time

t1 = time.time()

# u(k) = (900-3k)*r^k-1
# S(n) = u(1)+u(2)+....+u(n)

# u(k)*r = (900-3k)*r^k
# u(k+1) = (900-3k-3)*r^k
# u(k)*r-u(k+1) = 3*r^k

# S(n)*r = u(1)*r+u(2)*r+.....+u(n-1)*r+u(n)*r
# s(n) = u(2)+u(3)+.......+u(n)+u(1)
# S(n)*(r-1) = 3*r+3*r^2+...+3*r^n-1+(900-3n)*r^n-1-(900-3)*r
# S(n)*(r-1) = 3*r*(r^n-1-1)/(r-1)+(900-3n)*r^n-897*r 

# s(5000)*(r-1) = 3*r*(r^4999-1)/(r-1)-14100*r^5000-897*r
# rslt = -600,000,000,000
# rslt*r-rslt+897*r+14100*r^4999 = (3*r^5000-3*r)/(r-1)

def sft(r):
    rft = math.pow(r,4999)
    return (3*r*(rft-1)/(r-1)-14100*rft*r-897*r)/(r-1)

rslt = -600000000000
'''
print(sft(1.000001)-rslt)
print(sft(1.01)-rslt)
print(sft(1.005)-rslt)
'''
a = 1.0000001
b = 1.01
while True:
    mid = (a+b)/2
    t = sft(mid)
    if t < rslt:
        b = mid
    elif t == rslt:
        break
    else:
        a = mid
    if b-a < 0.0000000000001:
        break
    
print(round(mid*math.pow(10,12))/math.pow(10,12))

print("time:",time.time()-t1)  


    
