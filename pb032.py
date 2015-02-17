# it's the combination of 1 to 9 and * and = in a sequence
# let 11 be '*'
# let 12 be '='


def test(seq):
    times = seq.index(11)
    equals = seq.index(12)

    # */= cannot be at the first place or at the end of the sequence
    # * must come before = and the equation to be possible
    if times < 1 or times > 4:
        return 0
    if equals > 7 or equals < 5:
        return 0
    if equals-times < 2:
        return 0
    
    part1 = seq[0:times]
    part2 = seq[times+1:equals]
    part3 = seq[equals+1:11]

    a = 0
    for i in range(0,len(part1)):
        a = a*10 + part1[i]

    b = 0
    for i in range(0,len(part2)):
        b = b*10 + part2[i]

    c = 0
    for i in range(0,len(part3)):
        c = c*10 + part3[i]
    
    if a*b-c == 0:
        return c
    else:
        return 0


#sequence = [3,9,11,1,8,6,12,7,2,5,4]
#print(test(sequence))

allTheSeq = []

def makeSeq():

