a = input()
b = input()
pp = int(input())
n = int(input())
ppp=str(pp)
r = ppp[::-1]
p = []
if len(a)<len(b):
  p.append(a[-1] + b+str(ppp[n-1])+str(r[n-1]))
  #p.append(b)
else:
  p.append(b[-1] + a+str(ppp[n-1])+str(r[n-1]))
  #p.append(a)
  
print(p)


  