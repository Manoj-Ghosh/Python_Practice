a = input()
b = input()
pp = int(input())
n = int(input())
ppp=str(pp)
r = int(ppp[::-1])
#print(r)
#print(str(pp)[n-1])
#print(str(r)[n-1])

if len(a) == len(b):
  l = []
  l.append(a)
  l.append(b)
  l.sort()
  #print(l)
  #m = str(l[0])
  #n = str(l[1])
  #print(m[-1]+n+str(pp[n-1]))
  print(m)
  print(n)
  print(str(m[-1].upper()) + str(n.upper()) +str(pp)[n-1]+str(r)[n-1])
  

elif len(a)<len(b):
  print(str(a[-1].upper()) + str(b.upper()) +str(pp)[n-1]+str(r)[n-1])
  #p.append(b)
else:
  print(str(b[-1].upper()) + str(a.upper()) +str(pp)[n-1]+str(r)[n-1])
  #p.append(a)
  
  

  
#print(p)


  