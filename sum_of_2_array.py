n = int(input())
l1 = []
l2 = []
l3 = []

for i in range(n):
  num = int(input())
  l1.append(num)
  
for j in range(n):
  num = int(input())
  l2.append(num)
  

for k in range(n):
  s = l1[k] + l2[k]
  l3.append(s)

print(l3)

