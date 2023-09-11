stack = []
def push():
  e = int(input("ENTER THE ELEMENT: "))
  stack.append(e)
  print(stack)
  
def pop():
  if len(stack) == 0:
    print("STACK IS EMPTY!!")
    
  else:
    p = stack.pop()
    
    print("remove elements: ",p)
    
    print(stack)
    
while True:
  print("SELECT THE OPTION:")
  print("1.PUSH")
  print("2.POP")
  print("3.QUIT")
  
  c = int(input())
  if c == 1:
    push()
  
  elif c == 2:
    pop()
  
  elif c==3:
    break
  else:
    print("YOUR INPUT IS WRONG!!")
  
  