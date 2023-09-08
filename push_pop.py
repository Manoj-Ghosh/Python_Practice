stack = []

def push():
  a = int(input("enter the element: "))
  stack.append(a)
  print("after push operation stack is : ",stack)
  
def pop_elements():
  
  if len(stack) == 0:
    print("stack is empty!!")
  else:
    e = stack.pop()
    print("removed element is: ",e)
    print("after pop operation stack is: ",stack)
    

while True:    
  print("choose the operation:-")
  print("1.push")
  print("2.pop")
  print("3.quite")
  c = int(input("enter your choice: "))

  if c == 1:
    push()
  
  elif c == 2:
    pop_elements()
  
  elif c == 3:
    break
    
  else:
    print("choose correct option!!")
  
  