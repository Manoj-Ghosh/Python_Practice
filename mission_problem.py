n = int(input())
n = str(n)
elist =[]
olist = []
for i in range(0,len(n)):
  print(int(n[i:i+1]))
  
  if i % 2 == 0:
    elist.append(int(n[i:i+1]))
    
  else:
    olist.append(int(n[i:i+1]))

print(elist)
print(olist)

e = sum(elist)
o = sum(olist)

if e == o:
  print("MISSION SUCCESSFULL")
  
else:
  print("MISSION FAILED")

  