import time

t1 = time.time()

# date: 1900/1/1 is Monday
date = [1900,1,1,1]

count = 0

temp = 1
while temp == 1:
    date[2] += 1
    date[3] += 1

    # 7 days a week
    if date[3] == 8:
        date[3] = 1

    # 28/29 days Feb.
    if date[1] == 2:
        if (date[0]%4 > 0 or date[0] == 1900) and date[2] == 29:
            date[2] = 1
            date[1] = 3

        if date[0]%4 == 0 and date[2] == 30:
            date[2] = 1
            date[1] = 3

    # 30 days Apr. Jun. Sep. Nov.
    if date[2] == 31:
        if date[1] == 4 or date[1] == 6 or date[1] == 9 or date[1] == 11:
            date[2] = 1
            date[1] += 1

    # 31 days Jan. Mar. May. Jul. Aug. Oct. Dec.
    if date[2] == 32:
        if date[1] < 12:
            date[2] = 1
            date[1] += 1

        if date[1] == 12:
            date[2] = 1
            date[1] = 1
            date[0] += 1

    # 1/1 is Sunday
    if date[2] == 1 and date[3] == 7:
        if date[0] > 1900:
            count += 1

    if date[0] == 2000 and date[1] == 12 and date[2] == 31:
        temp = 0

print (count)

print("time:",time.time()-t1)        

    
