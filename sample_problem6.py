n = int(input())
o = [0]
e = []
t = []

for i in range(1,50,+2):
  o.append(i)
  
for j in range(0,50,+2):
  e.append(j)
  
for k in range(n):
  t.append(e[k])
  t.append(o[k])
  
print(t[n-1])

