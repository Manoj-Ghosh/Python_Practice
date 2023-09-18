n = int(input())
li = []
p = []
for i in range(n):
  num = int(input())
  li.append(num)
  
t = int(input())

for j in range(0,n,+1):
  for k in range(1,n,+1):
    if int(li[j]) + int(li[k]) == t:
      p.append(j)
      p.append(k)
    
print((list(set(p))))

      
  
  
  