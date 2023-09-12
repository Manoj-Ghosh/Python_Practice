"""import math
f = math.factorial(5)
print(f)"""


"""n = 5
fact = 1 
for i in range(1,n+1):
  fact = fact * i
  
print(fact)"""

def fact(n):
  f = 1 
  for i in range(1,n+1):
    f = f*i
  
  return f
  
a = fact(5)
print(a)
