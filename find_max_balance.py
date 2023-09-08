class bank:
  def __init__(self,name,account_no,balance):
    self.name = name
    self.account_no = account_no
    self.balance = balance
    
  
  def findmaxbalance(self,blist):
    
    if len(blist) == 0:
      return None
      
    else:
      m = 0
      for i in blist:
        
        if i.balance > m:
          m = i.balance
        
          
    for j in blist:
      if j.balance == m:
        return j 
          
        
        
n = int(input())
blist = []

for i in range(n):
  name = input()
  accountno = int(input())
  balance = int(input())
  
  blist.append(bank(name,accountno,balance))
  
obj = bank(name,accountno,balance)

ans = obj.findmaxbalance(blist)

if ans == None:
  print("list is empty!!")
  
else:
  print(ans.name)
  print(ans.balance)
  

