elist =[]
rlist =[]
flist = []
c = 0
r = 0
t = int(input())
for i in range(t):
  n1 = int(input())
  elist.append(n1)
  
for j in range(t):
  n2 = int(input())
  rlist.append(n2)
 
for p in range(t):
  c = elist[p] - rlist[p]
  r += c
  flist.append(r)
  
mx = max(flist)

for p in range(len(flist)):
  if mx == flist[p]:
    print("MAXIMUM GUEST: {} HOUR: {} ".format(mx,p+1))
  
