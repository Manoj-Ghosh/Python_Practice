s = input()
l = []
n = 0
for i in s:
  if i.isalpha():
    l.append(i)
    
  else:
    i = int(i)
    n = (n * 10) + i 
    
if len(l) == n:
  print("YES!!")
  
else:
  print("NO!!")
  