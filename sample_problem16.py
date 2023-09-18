a = [-1,0,1,2,-1,-4]
li = []
for i in range(0,len(a),+1):
  for j in range(1,len(a),+1):
    for k in range(2,len(a),+1):
      if a[i] + a[j] + a[k] == 0:
        li.append(a[i])
        li.append(a[j])
        li.append(a[k])
        print(li)
        
  