s = input()
f = s[1:] + s[0]
b = s[-1] + s[:-1]
  
if f == b:
  print(1)
else:
  print(0)
  