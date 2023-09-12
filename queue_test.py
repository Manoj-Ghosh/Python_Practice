queue = []
def enqueue(d):
  if d == 5:
    e = int(input("ENTER THE ELEMENTS: "))
    queue.append(e)
  else:
    e = int(input("ENTER THE ELEMENTS: "))
    queue.insert(0,e)
    
  print("AFTER INSERTING ELEMENTS QUEUE IS :",queue)
  
  
def dequeue(d):
  if d == 5:
    r = queue.pop(0)
    print("removed elements is :",r)
    print("after removing elements queue is: ",queue)
    
  else:
    r = queue.pop()
    print("removed elements is :",r)
    print("after removing elements queue is: ",queue)
    


print("5.ENTER ELEMENTS FROM RIGHT TO LEFT!")
print("6.ENTER ELEMENTS FROM LEFT TO RIGHT!")
d = int(input("enter your choice: \n"))
while True:
  print("1.ENQUEUE\n2.DEQUEUE\n3.QUIT")
  
  cho = int(input("enter your choice: \n"))
  
  if cho == 1:
    enqueue(d)
    
  elif cho == 2:
    dequeue(d)
    
  elif cho == 3:
    break
  else:
    print("YOU HAVE CHOSEN WRONG INPUT!!")
    
    
