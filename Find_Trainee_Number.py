olist =[]
flist =[]
c = 0
t1 = 0
t2 = 0
t3 = 0
for i in range(9):
  n = int(input())
  if 100>n>1:
    olist.append(n)
  else:
    print("INVALID INPUT!!")
for j in range(0,9,+3):
  t1 += olist[j]
a1 = t1//3 
flist.append(a1)
    
for p in range(1,9,+3):
  t2 += olist[p]
a2 = t2 // 3 
flist.append(a2)
    
for k in range(2,9,+3):
  t3 += olist[k]
a3 = t3//3 
flist.append(a3)
    
mx = max(flist)
if mx>70:
  for j in flist:
    c += 1
    if mx == j:
      print("Trainee Number: ",c)
else:
  print("All trainees are unfit!!")
      

        