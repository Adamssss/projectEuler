import math
import time

def init():
    global init_time
    init_time = time.time()

def timespent():
    print("time:",time.time()-init_time)


def shuffle(deck):
    decksize = len(deck)
    ndeck = []
    for i in range(decksize//2):
        ndeck.append(deck[i])
        ndeck.append(deck[i+decksize//2])
    return ndeck

def test():
    deck1 = [1,2]
    print(deck1, shuffle(deck1))
    deck2 = [1,2,3,4]
    print(deck2, shuffle(deck2),shuffle(shuffle(deck2)))
    deck3 = [1,2,3,4,5,6]
    print(deck3, shuffle(deck3),shuffle(shuffle(deck3)),shuffle(shuffle(shuffle(deck3))))

def inorder(deck):
    for i in range(len(deck)-1):
        if deck[i]>deck[i+1]:
            return False
    return True

def test2():
    slist = []
    for i in range(500):
        slist.append([])
    for i in range(2,400+1,2):
        deck = range(1,i+1,1)
        s = 0
        tdeck = deck
        #print(tdeck)
        while True:
            tdeck = shuffle(tdeck)
            s += 1
            #print(tdeck,s)
            if inorder(tdeck):
                break
        print(i,s)
        slist[s+1].append(i)
    for i in range(1,62):
        if len(slist[i+1])>0:
            print(i,slist[i+1])

    ''' first 400
    1 [2]
    2 [4]
    3 [8]
    4 [6, 16]
    5 [32]
    6 [10, 22, 64]
    7 [128]
    8 [18, 52, 86, 256]
    9 [74]
    10 [12, 34, 94, 342]
    11 [24, 90]
    12 [14, 36, 40, 46, 66, 92, 106, 118, 196, 274, 316]
    14 [44, 130, 382]
    15 [152, 218]
    16 [258]
    18 [20, 28, 58, 134, 172, 190, 220, 400]
    20 [26, 42, 56, 76, 124, 156, 166, 206, 276]
    21 [50, 338]
    22 [70, 268]
    23 [48]
    24 [120, 154, 222, 242, 358]
    28 [30, 88, 114, 146, 216, 340]
    29 [234]
    30 [78, 100, 232, 280, 332]
    33 [162]
    35 [72]
    36 [38, 96, 110, 112, 136, 186, 248, 260, 286, 328, 334, 352, 366]
    37 [224]
    39 [80]
    40 [188]
    42 [148, 302, 388]
    44 [116, 346, 398]
    46 [142]
    48 [98, 292]
    50 [252]
    51 [104]
    52 [54, 158, 160, 266]
    54 [82]
    58 [60, 178]
    60 [62, 144, 176, 184, 226, 288, 306, 326, 370, 386]
    '''
    # s(2^n)=n
    # s(2^n+2)=2n
    # s(2^n-2)=2^n-4


def test3():
    for i in range(2,10**3+1,2):
        deck = range(1,i+1,1)
        s = 0
        tdeck = deck
        #print(tdeck)
        while True:
            tdeck = shuffle(tdeck)
            s += 1
            #print(tdeck,s)
            if inorder(tdeck):
                break
        if s==60:
            print(i,s)
            '''
            62 60
            144 60
            176 60
            184 60
            226 60
            288 60
            306 60
            326 60
            370 60
            386 60
            404 60
            428 60
            430 60
            496 60
            526 60
            534 60
            550 60
            672 60
            716 60
            756 60
            794 60
            862 60
            916 60
            976 60
            1002 60
            1086 60
            1156 60
            1210 60
            1282 60
            1288 60
            1322 60
            1396 60
            1436 60
            1526 60
            1576 60
            1600 60
            1656 60
            1846 60
            1892 60
            1926 60
            1964 60
            2014 60
            2016 60
            2136 60
            2146 60
            2266 60
            2276 60
            2380 60
            2476 60
            2502 60
            2584 60
            2666 60
            2746 60
            2822 60
            2926 60
            3004 60
            3158 60
            3256 60
            3356 60
            3466 60
            3576 60
            3628 60
            3732 60
            3776 60
            3844 60
            3964 60
            3966 60
            4060 60
            4304 60
            4306 60
            4434 60
            4576 60
            4698 60
            4798 60
            4966 60
            5006 60
            5286 60
            5426 60
            5552 60
            5674 60
            5776 60
            5864 60
            5890 60
            6040 60
            6046 60
            6192 60
            '''

def test4():
    # https://oeis.org/A002326
    # In other words, least m > 0 such that 2n+1 divides 2^m-1.
    for i in range(2,400,2):
        s = 1
        while True:
            if (2**s-1)%(i-1) == 0:
                break
            s += 1
        print(i,s)


def test5():
    result = 0
    for i in range(2,2**60+1,2):
        s = 1
        while True:
            if (2**s-1)%(i-1) == 0:
                break
            s += 1
        if s == 60:
            result += i
            print(i,s)
    print("result:", result)
    
def main():
    # 2*60-1 = (2**30+1)(2**15+1)(2**15-1)
    #        = (5*5*13*41*61*1321)(3*3*11*331)(7*31*151)
    #[1 3 9][1 5 25][1 7][1 11][1 13][1 31][1 41][1 61][1 151][1 331][1 1321]
    candidates = [1, 3, 9, 5, 15, 45, 25, 75, 225]
    for f in [7, 11, 13, 31, 41, 61, 151, 331, 1321]:
        for i in range(len(candidates)):
            candidates.append(candidates[i]*f)
    result = 0
    for i in candidates:
        s = 1
        while True:
            if (2**s-1)%i == 0:
                break
            s += 1
        if s == 60:
            result += (i+1)
            #print(i+1,s)
    print("result:", result)


if __name__ == '__main__':
    init()
    main()
    #test4()
    timespent()
