row = int(input("enter row: \n"))
for i in range(0,row):
  for j in range(0,i+1):
    print("*"*j,end = "")
  print(" ")