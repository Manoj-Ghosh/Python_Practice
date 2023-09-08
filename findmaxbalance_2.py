class bank:
  def __init__(self,name,account_no,balance):
    self.name = name
    self.account_no = account_no
    self.balance = balance
    
  def findmaxbalance(self,blist):
    if len(blist) == 0:
      return None
      
    else:
      max_balance = max(blist,key = lambda x:x.balance)
      return max_balance
      
  
  
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
  print("you does not give any input!!")
  
else:
  print(ans.name,"\t",ans.balance)
  
  
