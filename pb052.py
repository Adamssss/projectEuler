# it's common sense that 142857 is the answer
# I've been knowing it through my lifetime
# so the code would be

print(142857)

# okay I'm gonna pretend I don't know it and do it properly

import math

def digs(num):
    return math.floor(math.log10(num)+1)

# define a method to change the number into a sequence that represent the digits
# for example : 998642 would be 2101010100
# the fisrt two stands for two nines and the following ones stand for 2,4,6,8
def comp(num):
    temp = num
    result = 0
    while temp > 0:
        n = temp%10
        temp = temp//10
        result += math.pow(10,n)
    return result

# print(comp(998642))

i = 0
while True:
    i += 1
    if digs(6*i) > digs(i):
        continue
    target = comp(i)
    if comp(2*i) != target:
        continue
    if comp(3*i) != target:
        continue
    if comp(4*i) != target:
        continue
    if comp(5*i) != target:
        continue
    if comp(6*i) != target:
        continue
    print (i)
    break
