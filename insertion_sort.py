




def insertion_sort(arr):
    for i in range(1,len(arr)):

        key=arr[i]


        j=i-1

        while j>=0 and key< arr[j]:
            arr[j+1]=arr[j]
            j -=1

        arr[j+1]=key

arr1=input("Enter list:")
arr=[]
for i in arr1.split(','):
    y=int(i)
    arr.append(y)
insertion_sort(arr)


#########################################
l=[]
for i in range(len(arr)):
    l.append(arr[i])

print(l)
n=int(input("Enter number for search:"))
def linear_search(l,n):
    for i in range(len(l)):
        if l[i]==n:
            return i
print(linear_search(l,n))
