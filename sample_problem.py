n1 = int(input())
n2 = int(input())
c = 0
for i in range(n1,n2+1):
  l = i
  
  ddict = {}
  while l>0:
    rem = l%10
    if str(rem) not in str(i):
      c += 1
      
    l = l//10
  print(c)
  
  