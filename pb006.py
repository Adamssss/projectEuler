N = 100
sumOfSquare = 0
totalSum = 0
squareOfSum = 0

for i in range(1,N+1):
    sumOfSquare = sumOfSquare + i*i

for i in range(1,N+1):
    totalSum = totalSum + i

squareOfSum = totalSum * totalSum

difference = squareOfSum - sumOfSquare

print (difference)
