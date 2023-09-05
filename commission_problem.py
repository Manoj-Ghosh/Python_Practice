p = input()
s = input()
c = []
if s == "y":
  c = list(map(str,input().split(",")))

  
l = len(c)

print("TOTAL MEMBER : ",l+1)

if l > 0:
  
  print("COMMISSION DETAILS")
  print(p,"\t",5000*(10*l)*0.01)

  for i in c:
    print(i,"\t",5000*5*0.01)
    
else:
  print(p,"\t",5000*5*0.01)
  
  
  
  

  