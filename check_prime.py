c = 0
num = int(input())
for i in range(1,num+1):
  if num % i == 0:
    c += 1 
    
if c == 2:
  print("prime number!!")
  
else:
  print("not a prime number !!")
  
  
  