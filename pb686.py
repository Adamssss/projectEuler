import math
import time

def init():
    global init_time
    init_time = time.time()

def timespent():
    print("time:",time.time()-init_time)


def test1():
    print("log(2,10)=",math.log(2,10))
    print("2**7/10=",2**7/10)
    print("log(128,10)-1=",math.log(128,10)-1)
    print("log(12,10)=",math.log(12,10))
    print("log(13,10)=",math.log(13,10))
    print("2**80/10**23=",2**80/10**23)
    print("log(2**80,10)-23=",math.log(2**80,10)-23)

def pv1(a,b):
    log210 = math.log(2,10)
    lower = math.log(a,10)-math.floor(math.log(a,10))
    upper = math.log(a+1,10)-math.floor(math.log(a+1,10))
    #print(log210,lower,upper)
    c = 0
    i = 1
    temp = log210
    while True:
        temp += log210
        i += 1
        if temp > 1:
            temp -= 1
        #print(temp,i,ttemp)
        if temp > lower and temp < upper:
            c += 1
            #print("p(",a,",",c,")=",i)
            if c ==b:
                return i
                break

def test2():
    pv1(12,1)
    pv1(12,2)
    pv1(123,45)
    

def main():
    result = 0
    result = pv1(123,678910)
    print("result:", result)


if __name__ == '__main__':
    init()
    #test2()
    main()
    timespent()
