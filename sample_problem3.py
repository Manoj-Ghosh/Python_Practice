l = []
n = int(input())
c = 1
r = 0
for i in range(n):
  num = int(input())
  l.append(num)
  
for i in range(1,n):
  for j in range(i-1,0,-1):
    if l[i]>l[j]:
      c += 1
  if c == i:
    r += 1
    
  
  
print(r+1)
