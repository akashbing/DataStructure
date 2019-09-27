


tup=(1,2,3,"akash","soni",5,6,7)

n=3

def search_tup(tup,n):
    for i in range(len(tup)):
        if tup[i]==n:
         return True
    return False
if search_tup(tup,30):
    print("found")

else:
    print("not found")
