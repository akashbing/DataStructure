

arr=[1,2,"akash",3,4,"soni",67,65]

n="akash"


def search_alpha(arr,n):
    for i in range(len(arr)):
        if arr[i]==n:
            return True
    return False
if search_alpha(arr,n):
    print("Found")
else:
    print("not found")