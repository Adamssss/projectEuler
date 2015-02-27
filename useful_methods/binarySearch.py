# define a binary search 
def isInList(item,lst):
    firstPoint = 0
    endPoint = len(lst)-1
    index = -1
    while firstPoint <= endPoint:
        midPoint = (firstPoint+endPoint)//2
        if lst[midPoint] == item:
            index = midPoint
            return index
        elif item > lst[midPoint]:
            firstPoint = midPoint +1
        else:
            endPoint = midPoint -1

    return index
