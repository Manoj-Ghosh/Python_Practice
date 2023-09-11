li = []
l = []
r = int(input())
c = int(input())
t = int(r*c) 


for i in range(t):
  v = int(input())
  
  li.append(v)

for k in range(0,len(li),+3):
  
  s = sum(li[k:k+3])
  l.append(s)
  
mx = max(l)

for k in range(len(l)):
  if mx == l[k]:
    print("row number with max one = ",k+1)
    
  
  
 
 
 

