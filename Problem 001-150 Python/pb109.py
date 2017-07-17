import math
import time

t1 = time.time()

pset = []

for i in range(1,21):
    pset.append(i)
    pset.append(2*i)
    pset.append(3*i)

pset.append(25)
pset.append(50)

dset = []

for i in range(1,21):
    dset.append(2*i)

dset.append(50)

# fisrt two different 62*61/2*21
# fisrt two same 62*21
# only two 62*21
# only one 21
# total 42336

checkout = []

for i in range(len(pset)):
    for j in range(i+1,len(pset)):
        for k in dset:
            temp = pset[i]+pset[j]+k
            checkout.append(temp)

for i in pset:
    for j in dset:
        temp = i*2+j
        checkout.append(temp)

for i in pset:
    for j in dset:
        temp = i+j
        checkout.append(temp)

for i in dset:
    checkout.append(i)

count = 0
for i in checkout:
    if i < 100:
        count += 1

print(count)

print("time:",time.time()-t1)  


    
