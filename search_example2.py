

#max repititions

def MaxrepitionBruteForce(arr):
    n=len(arr)
    count=max=0
    for i in range(0,n):
        count=1
        for j in range(0,n):
            if (i !=j and arr[i]==arr[j]):
                count +=1
        if max<count:
            max=count
            maxrep=arr[i]
    print(maxrep,"repeated for ",max)

arr=[3,2,1,2,2,3,2,1,3]

MaxrepitionBruteForce(arr)

#improve above function

def Maxrepitionswithsort(arr):

    j=0
    count=max=1
    element=arr[0]
    print("element",element)
    for i in range(1,len(arr)):
        print("i print",i)
        if arr[i]==element:
            print("arr in if ",arr[i])
            count +=1
            if count > max:
                max=count
                print("max",max)
                maxRepetedElement=element
                print("maxRe",maxRepetedElement)
        else:
            count=1
            element=arr[i]
    print(maxRepetedElement,max)
Maxrepitionswithsort(arr)

#hash table
arr=[3,1,4,2,3,2,1,3,2,2]
def MaxRepititionsWithHash(arr):
    table={}
    print(table)
    max=0
    for element in arr:
        if element in table:
            table[element] +=1
            print(table)
        elif element !=" ":
            table[element]=1
        else:
            table[element]=0
    for element in arr:
        if table[element] > max:
            max=table[element]
            maxRepeatedElement=element
    print(maxRepeatedElement,"repeated",max,"times")
    print(table)
MaxRepititionsWithHash(arr)
