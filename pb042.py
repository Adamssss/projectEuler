import math

# read the words into a list
f = open('pb042_words.txt','r')

words = f.read().split(',')

for i in range(0,len(words)):
    words[i] = words[i][1:len(words[i])-1]

f.close()

def valueOf(word):
    value = 0
    for i in range(0,len(word)):
        value += ord(word[i])-64
        
    return value


# n(n+1)/2
def isTriangle(x):
    n = math.floor(math.sqrt(2*x))
    if n*(n+1) == 2*x:
        return True
    return False

count = 0
for i in range(0,len(words)):
    if isTriangle(valueOf(words[i])):
        count += 1

print (count)
