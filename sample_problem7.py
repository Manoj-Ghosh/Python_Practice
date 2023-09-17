s1 = input()
s2 = input()
r = 0
k = 0

if len(s2)<len(s1):
  r = len(s1) - len(s2)
  
for i in s2:
  for j in s1:
    if i.lower() == j.lower():
      k+=1 
      break
  continue

r += (len(s2) - k)

print(r)
