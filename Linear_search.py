
x=5
arr=[4,5,6,7,9,8,2,1,44,34]


def search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1
print(search(arr,x))