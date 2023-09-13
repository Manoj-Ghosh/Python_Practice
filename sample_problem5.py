n = int(input())
l=[]
c=0
d=0
p=[]
q=[]

for i in range(n):
  num = int(input())
  l.append(num)
  
maxx=l[0]
for i in l:
  if i>maxx:
    maxx=i
    
print(maxx)

minn=l[0]
for i in l:
  if i<minn:
    minn=i
    
print(minn)

for i in l:
  if i%2==0:
    c+=1
print(c)

for i in l:
  for j in range(1,i+1):
    if i%j==0:
      d+=1
      
    if d==2:
      p.append([i])
      
print(p)
      
  
  
  