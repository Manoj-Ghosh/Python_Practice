import sys
lis = map(int,input().split(" "))
li = list(lis)
print(li)
a = set(li)
print(a)
print("size of set is : "+str(sys.getsizeof(a))+" bytes") #this gives the size with garbage value
print("size of set : "+str(a.__sizeof__())+" bytes") #this gives the size without garbage value