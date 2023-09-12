class Node:
  def __init__(self,data):
    self.data = data
    self.ref = None
    
class Linkedlist:
  def __init__(self):
    self.head = None
    
    
  def print_ll(self):
    if self.head == None:
      print("LINKEDLIST IS EMPTY!!")
      
    else:
      n = self.head
      while n!= None:
        print(n.data,"-->",end = " ")
        n = n.ref
        
  def add_begin(self,data):
    new_node = Node(data)
    new_node.ref = self.head
    self.head = new_node
    
  """def add_end(self,data):
    
    new_node = Node(data)
    
    if self.head == None:
      self.head = new_node
    else:
      n = self.head
      while n != None:
        n = n.ref
      n.ref = new_node"""
      
      
  def add_after(self,data,x):
    n = self.head
    while n != None:
      if n.data == x:
        break
      
      n = n.ref
      
    if n == None:
      print("node is not present in linkedlist!!")
      
    else:
      new_node = Node(data)
      new_node.ref = n.ref
      n.ref = new_node
      
      
    
        
        
obj = Linkedlist()
obj.add_begin(10)
obj.add_begin(20)
obj.add_begin(30)
obj.add_after(40,20)
obj.add_after(600,10)
#obj.add_end(40)
#obj.add_end(50)
obj.print_ll()



