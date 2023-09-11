clist = []
dic = {}
n = int(input())
for i in range(n):
  c = input().lower()
  clist.append(c)
  
for j in clist:
  if j not in dic:
    dic[j] = 1 
  else:
    dic[j] += 1 
      
for p in dic:
  if dic[p] % 2 != 0:
    print(p)
    break
    
    
  