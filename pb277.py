import math
import time

t1 = time.time()

def CollatzString(n):
    if n == 1:
        return ""
    r = n%3
    if r == 0:
        return "D"+CollatzString(n//3)
    if r == 1:
        return "U"+CollatzString((4*n+2)//3)
    if r == 2:
        return "d"+CollatzString((2*n-1)//3)

#print(CollatzString(231))
#print(CollatzString(1004064))

# ax+b
# reverse string operation
def Reverse(string,a,b):
    if len(string) == 0:
        return [a,b]
    o = string[-1]
    if o == "D":
        # 3*(ax+b) = 3a*x+3b
        return Reverse(string[:-1],3*a,3*b)
    if o == "U":
        # (3*(ax+b)-2)/4 = 3a/4*x+(3b-2)/4
        return Reverse(string[:-1],3*a/4,(3*b-2)/4)
    if o == "d":
        # (3*(ax+b)+1)/2 = 3a/2*x+(3b+1)/2
        return Reverse(string[:-1],3*a/2,(3*b+1)/2)

def answer(string,threshold):
    # error e
    e = math.pow(10,-10)
    # ax+b
    R = Reverse(string,1,0)
    x = math.floor((threshold-R[1])/R[0])-1
    while True:
        t = R[0]*x+R[1]
        if abs(t-round(t)) < e and t > threshold:
            if checkstring(round(t),string):
                return round(t)
        x += 1

def checkstring(n,string):
    comparestring = CollatzString(n)
    for i in range(len(string)):
        if string[i] != comparestring[i]:
            return False
    return True
        
#print(answer("DdDddUUdDD",10**6))
print(answer("UDDDUdddDDUDDddDdDddDDUDDdUUDd",10**15))


print("time:",time.time()-t1)  





