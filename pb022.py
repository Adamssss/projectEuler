
# read the names into a list
f = open('pb022_names.txt','r')

names = f.read().split(',')

for i in range(0,len(names)):
    names[i] = names[i][1:len(names[i])-1]

f.close()

# sort the names


# get the sum of the score
