n1 = int(input())
n2 = int(input())
l = []
f = []
c = 0
for i in range(n1, n2+1):
  f.append(i)
  
print(f)
for i in f:
  print(i)
  r = i % 10
  l.append([r])
  a = i / 10
print(l)
for j in l:
  if j not in l:
    c += 1 
    
print(c)
    
  
  