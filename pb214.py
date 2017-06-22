import math
import time

t1 = time.time()

N = 40000000
n = 25

prime = []

def primeSieve(n):
    global prime
    n = (n+1)//2
    p = [True]*(n)
    i = 1
    prime.append(2)
    while i < n:
        if p[i]:
            t = 2*i+1
            prime.append(t)
            p[i] = False
            j = 2*i*i+2*i
            while j < n:
                p[j] = False
                j += t
        i += 1
    p = []
    return prime

primeSieve(round(math.sqrt(N))+100)

# wikipedia phi function

ps = [0,1]

# phi(m*n) = phi(m)*phi(n) if gcd(m,n) == 1
# prime phi(p) = p-1
def phi(number):
    root = math.floor(math.sqrt(number))
    result = 1
    i = 0
    t = prime[i]
    while t <= root:
        count = 0
        while number%t == 0:
            count += 1
            number = number//t
        if count > 1:
            result *= int(math.pow(t,count-1))
        if count > 0:
            result *= ps[t]
            return result*ps[number]
        i += 1
        t = prime[i]
    return (number-1)

cls = [0,1]

def chainlength(number):
    return cls[ps[number]]+1

total = 0 
for i in range(2,N+1):
    t = phi(i)
    ps.append(t)
    u = chainlength(i)
    cls.append(u)
    if t == i-1 and u == n:
        #print(i,t,u)
        total += i
    #print(i,t,u)

print(total)
# 1677366278943
# 40000000 may cause memory overflow
# time: 638.8385391235352
'''
# number/phi/chainlength
2 1 2
3 2 3
4 2 3
5 4 4
6 2 3
7 6 4
8 4 4
9 6 4
10 4 4
11 10 5
12 4 4
13 12 5
14 6 4
15 8 5
16 8 5
17 16 6
18 6 4
19 18 5
20 8 5
21 12 5
22 10 5
23 22 6
24 8 5
25 20 6
26 12 5
27 18 5
28 12 5
29 28 6
30 8 5
31 30 6
32 16 6
33 20 6
34 16 6
35 24 6
36 12 5
37 36 6
38 18 5
39 24 6
40 16 6
41 40 7
42 12 5
43 42 6
44 20 6
45 24 6
46 22 6
47 46 7
48 16 6
49 42 6
50 20 6
51 32 7
52 24 6
53 52 7
54 18 5
55 40 7
56 24 6
57 36 6
58 28 6
59 58 7
60 16 6
61 60 7
62 30 6
63 36 6
64 32 7
65 48 7
66 20 6
67 66 7
68 32 7
69 44 7
70 24 6
71 70 7
72 24 6
73 72 7
74 36 6
75 40 7
76 36 6
77 60 7
78 24 6
79 78 7
80 32 7
81 54 6
82 40 7
83 82 8
84 24 6
85 64 8
86 42 6
87 56 7
88 40 7
89 88 8
90 24 6
91 72 7
92 44 7
93 60 7
94 46 7
95 72 7
96 32 7
97 96 8
98 42 6
99 60 7
100 40 7
'''
       
print("time:",time.time()-t1)
                
