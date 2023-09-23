def func(n):
  li = []
  l1 = []
  if n<10:
    return n + 10
  
  if n>=10:
    for i in range(9,1,-1):
      
      if n % i == 0:
        li.append(i)
    rli = int(''.join(map(str, li)))
    reli = int(str(rli)[::-1])
    l1.append(rli)
    l1.append(reli)
    ans = min(l1)
    return ans
      
  else:
    return "not possible!!"
    
        

    
  
n = int(input())
print(func(n))

