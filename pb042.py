
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

print (valueOf(words[2]))

def isTriangle(x):
    
