n = int(input())
l = []
def d2b(n):
  if n>=1:
    d2b(n//2)
  print(n%2,end = " ")
  #l.append(n%2)
  return l

print(l)
