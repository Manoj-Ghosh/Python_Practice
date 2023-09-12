l = []
nl = []
n = int(input())
for i in range(n):
  num = int(input())
  l.append(num)
  
s = int(input())

if s < n:
  for p in range(s,n):
    nl.append(l[p])
  #nl.append(l[s:])
  
#print(nl)

  if len(nl) != n:
    for q in range(0,s):
      nl.append(l[q])
    
  print(nl)

if s > n:
  r = s % 5
  for p in range(r,n):
    nl.append(l[p])
    
  if len(nl) != n:
    for q in range(0,r):
      nl.append(l[q])
    
  print(nl)
    
    
if s == n:
  print(l)
    
    
if len(l) == 0:
  print("No element in the list!!")
    
    
  
  