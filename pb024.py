
# the number of order of the one that is wanted
N = 1000000

# p is possible numbers total
p = 10

string = []

def fact(x):
    if x == 0:
        return 1
    if x == 1:
        return 1
    return x*fact(x-1)

def lexico (st,n):
    x = p-1-len(st)
    remain = n%fact(x)
    num = n // fact(x)
    number = -1
    for i in range(0,p):
        if i in st:
            num += 1
        if num == i and number < 0:
            number = i
    st.append(number)
    if x > 0:
        return lexico(st,remain)
    return st
    
answer = lexico(string,N-1)
number = 0
for i in range(0,10):
    number = number*10 + answer[i]

print (number)
