

def FindMissingNumber(A):
    x=max(A)

    n=len(A)
    for i in range(1,x+1):

        found=0
        for j in range(0,n):


            if i==A[j]:
                found =1
            continue
        if found ==0:

            print("Missing number is",i)
A=[8,7,5,6,5,2,9,12,10,20,4,11,1,20]
FindMissingNumber(A)
