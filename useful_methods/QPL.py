def QPL(mylist):
    if len(mylist) == 1:
        return [mylist]
    qpl = []
    for i in mylist:
        rest = mylist[:]
        rest.remove(i)
        for j in QPL(rest):
            qpl.append([i]+j)
    return qpl

