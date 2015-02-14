
# a function that returns the recurring cycle
# returns 0 when divided totally
# get a list of previous remainder
# same remainder means a cycle
def rc(n):
    remain = 1
    previous = []
    count = 0
    while remain < n:
        remain *= 10
    remain = remain % n
    while not remain in previous:
        if remain == 0:
            return 0
        previous.append(remain)
        while remain < n:
            remain *= 10
            count += 1
        remain = remain % n

    return (count - previous.index(remain))


largest = 0
largesti = 0
for i in range(2,1000):
    if largest < rc(i):
        largest = rc(i)
        largesti = i

print (largesti)
    
    
