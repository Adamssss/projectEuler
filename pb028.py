N = 1001

#length of diagonal
Nd = (N+1)//2

# the top right diagonal
# an = (2n+1)^2
tr = []
for i in range(0,Nd):
    an = (2*i+1)*(2*i+1)
    tr.append(an)

# the top left diagonal
# an = (2n+1)^2-(2n+1)+1
tl = []
for i in range(0,Nd):
    an = (2*i+1)*2*i+1
    tl.append(an)

# the bot left diagonal
# an = (2n+1)^2-(2n+1)+1-(2n+1)+1
bl = []
for i in range(0,Nd):
    an = (2*i+1)*(2*i-1)+2
    bl.append(an)

# the bot right diagonal
# an = (2n+1)^2-(2n+1)+1-(2n+1)+1-(2n+1)+1
br = []
for i in range(0,Nd):
    an = (2*i+1)*(2*i-2)+3
    br.append(an)

total = -3
for i in range(0,Nd):
    total += tr[i]+tl[i]+bl[i]+br[i]

print (total)
