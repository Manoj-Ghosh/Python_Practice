n = int(input())
nlist = []
for i in range(n):
  num = int(input())
  nlist.append(num)
  
k = int(input())
l = len(nlist)
s = l-(k)

for p in range(-k,s,+1):
  print(nlist[p],end=" ")
  
