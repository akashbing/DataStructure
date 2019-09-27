arr=[1,2,3,4,5,66,343,44,7,8]

n=8
i=flag=0

while i < len(arr):
    if arr[i]==n:
        flag=1
        break


    i=i+1
if flag ==1:
    print("item found in position",i)
else:
    print("item not found")