l1 = ["manoj","saroj","piku","arunav","sanai"]
onj = enumerate(l1,2)
print(list(onj))
print()


for i in enumerate(l1):
  print(i)
print()


for count, ele in enumerate(l1,100):
  print(count, ele)
  
print()

for count, ele in enumerate(l1,100):
  print(count)
  print(ele)
  
print()

