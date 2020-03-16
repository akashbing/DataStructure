

def binary_search(arr,val):
    low=0
    high=len(arr)-1
    while low<high:
        mid=(low+high)//2
        if arr[mid]>val:
            high=mid-1
        elif arr[mid]<val:
            low=mid+1
        else:return mid
    return -1
arr=[1,2,3,5,6,7]
val=6
print(binary_search(arr,val))