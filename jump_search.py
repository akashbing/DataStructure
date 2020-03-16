
import math

def jumpsearch(lis,val):
    length=len(lis)
    jump=int(math.sqrt(length))
    left,right=0,0
    while left < length and lis[left]<=val:
        right=min(length -1,left + jump)
        if lis[left] <= val and lis[right] >=val:
            break
        left += jump;

    if left>=length or lis[left]> val:
        return -1
    right=min(length -1,right)
    i=left
    while i<= right and lis[i] <=val:
        if lis[i] == val:
            return i
        i +=1
    return -1

lis=[1,2,3,4,5,6,7,8,9]
print(jumpsearch(lis,5))

