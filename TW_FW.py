v = int(input())
w = int(input())
if (w == 1 or w < 2 or w <= v):
  print("INVALID INPUT!!")
  
else:
  x = ((4*v)-w)//2
  print("TW = {} FW = {}".format(x,v-x))