c = int(input())

numlist = []

v = 0

for i in range(c):
  num = int(input())
  numlist.append(num)
  

elist = []
olist = []

for i in numlist:

  p = i
  p = str(p)
  print(p)
  for j in range(0,len(p)):
    #print(int(p[j:j+1]))
    v +=  int(p[j:j+1]) % 2 
  if v == 0:
    elist.append(i)
    print(elist)
  
  else:
    olist.append(i)
    
    
      
#print(len(elist))
#print(len(olist))
