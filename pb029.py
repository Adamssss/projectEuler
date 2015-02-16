import math

def downTo(origin):
    i = 2
    while i <= 10:
        if int(math.log(origin[0],i))-math.log(origin[0],i)== 0:
            origin[1] *= int(math.log(origin[0],i))
            origin[0] = i
        i += 1

    return origin

string = []
for i in range(2,101):
    for j in range(2,101):
        temp = [i,j]
        if not downTo(temp) in string:
            string.append(downTo(temp))

print (len(string))
            
    
    

