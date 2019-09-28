



def Binarysearch(arr,l,r,x):

    while l<=r:
        mid=l+(r-l)//2

        if arr[mid]==x:
            return mid

        elif arr[mid]<x:
            l=mid+1

        else :
            r=mid-1

    return -1

arr=[1,2,3,4,5,50,60,70]
x=50

result=Binarysearch(arr,0,len(arr)-1,x)

if result != -1:
    print(result)
else:
    print("not found in list")