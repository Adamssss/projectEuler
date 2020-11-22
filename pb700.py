import math
import time

def init():
    global init_time
    init_time = time.time()

def timespent():
    print("time:",time.time()-init_time)

def nchain(bn,c,d):
    lb = len(bn)
    temp = c/d
    for i in range(lb):
        temp = 1/(bn[-1-i]+temp)
    return temp

def test():
    numberA = 1504170715041707
    numberB = 4503599627370517

    print(numberA/numberB,"=A/B")

    a1 = 1
    b1 = numberB//numberA
    c1 = numberB-b1*numberA
    d1 = numberA

    print(a1/(b1+c1/d1),"=a1/(b1+c1/d1)",a1,b1,c1,d1)

    a2 = 1
    b2 = d1//c1
    c2 = d1-b2*c1
    d2 = c1

    print(a1/(b1+a2/(b2+c2/d2)),"=a1/(b1+a2/(b2+c2/d2))",a1,[b1,b2],[c1,c2],d1)

    barray = [b1]
    carray = [c1]
    darray = [d1]
    
    print(a1,b1,c1,d1,d1-c1)
    for i in range(15):
        an = 1
        bn = darray[-1]//carray[-1]
        cn = darray[-1]-bn*carray[-1]
        dn = carray[-1]

        print(nchain(barray,carray[-1],darray[-1]),an,bn,cn,dn,dn-cn)
        
        barray.append(bn)
        carray.append(cn)
        darray.append(dn)


def nchain2(bn,c,d):
    lb = len(bn)
    temp = c/d
    for i in range(lb):
        temp = 1/(bn[-1-i]-temp)
    return temp

# fraction chain
def test2():
    numberA = 1504170715041707
    numberB = 4503599627370517

    print(numberA/numberB,"=A/B")

    a1 = 1
    b1 = numberB//numberA +1
    c1 = b1*numberA -numberB
    d1 = numberA

    barray = [b1]
    carray = [c1]
    darray = [d1]
    
    print(a1,b1,c1,d1)
    for i in range(15):
        an = 1
        bn = darray[-1]//carray[-1] + 1
        cn = bn*carray[-1] - darray[-1]
        dn = carray[-1]

        print(nchain2(barray,carray[-1],darray[-1]),an,bn,cn,dn)
        
        barray.append(bn)
        carray.append(cn)
        darray.append(dn)


def main():
    numberA = 1504170715041707
    numberB = 4503599627370517

    eulercoins = []
    lastec = numberA + 1
    count = 0
    ecsum = 0


    '''
    # eulercoin        sum              n
    1 1504170715041707 1504170715041707 1
    2 8912517754604 1513083232796311 3
    3 2044785486369 1515128018282680 506
    4 1311409677241 1516439427959921 2527
    5 578033868113 1517017461828034 4548
    6 422691927098 1517440153755132 11117
    7 267349986083 1517707503741215 17686
    8 112008045068 1517819511786283 24255
    9 68674149121 1517888185935404 55079
    10 25340253174 1517913526188578 85903
    11 7346610401 1517920872798979 202630
    12 4046188430 1517924918987409 724617
    13 745766459 1517925664753868 1246604
    14 428410324 1517926093164192 6755007
    15 111054189 1517926204218381 12263410
    16 15806432 1517926220024813 42298633
    '''

    temp = numberA

    for i in range(10000):
        if temp < lastec:
            eulercoins.append(temp)
            count += 1
            lastec = temp
            ecsum += lastec
            #print(count,lastec,ecsum,i+1)
        temp += numberA
        if temp > numberB:
            temp -= numberB


    a1 = 1
    b1 = numberB//numberA +1
    c1 = b1*numberA -numberB
    d1 = numberA

    barray = [b1]
    carray = [c1]
    darray = [d1]

    ecsum = numberA
    
    print(a1,b1,c1,d1)
    for i in range(100):
        an = 1
        bn = darray[-1]//carray[-1] + 1
        cn = bn*carray[-1] - darray[-1]
        dn = carray[-1]

        print(nchain2(barray,carray[-1],darray[-1]),an,bn,cn,dn)
        
        barray.append(bn)
        carray.append(cn)
        darray.append(dn)

        ecsum += dn

        if cn == 1:
            break
    ecsum += 1
    print("result:", ecsum)


if __name__ == '__main__':
    init()
    main()
    #test2()
    timespent()
