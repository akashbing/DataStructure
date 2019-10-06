#Checking duplicates in list

def ck_dup(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[i]==arr[j]):
                print("Duplicates exist",arr[i])
                return
    print("no duplicate")

arr=[1,2,2,3,4,5,6,6,7]

ck_dup(arr)