lis = map(int,input().split(" "))
lis = list(lis)
import time
c= 0
start_time_loop = time.time()
for i in lis:
    c += 1
end_time_loop = time.time() - start_time_loop
print("length is : "+str(c))
print("Time required : "+str(end_time_loop))

start_time_len = time.time()
l = len(lis)
end_time_len = time.time()-start_time_len

print("length is : "+ str(l))
print("time required : "+str(end_time_len))


