class player:
  def __init__(self,pname,pcoumtry,noofmatches,noofrun,noofwicket):
    self.pname = pname
    self.pcountry = pcountry
    self.noofmatches = noofmatches
    self.noofrun = noofrun
    self.noofwicket = noofwicket
    
    
class team:
  def __init__(self,plist):
    self.plist = plist
    
    
  def getminrun(self):
    mrun = []
    for i in self.plist:
      mrun.append(i.noofrun)
      
      
    result = min(mrun)
    
    rlist = []
    for i in self.plist:
      if i.noofrun == result:
        rlist.append(i.pname)
        rlist.append(result)
        rlist.append(i.pcountry)
        
    return rlist
    
    
  def getmaxwicket(self):
    mwicket = []
    for i in self.plist:
      mwicket.append(i.noofwicket)
      
      
    result = max(mwicket)
    
    rlist = []
    for i in self.plist:
      if i.noofwicket == result:
        rlist.append(i.pname)
        rlist.append(result)
        rlist.append(i.pcountry)
        
    return rlist
    
    
    
n = int(input())
plist = []

for i in range(n):
  pname = input()
  pcountry = input()
  noofmatchs = int(input())
  noofrun = int(input())
  noofwicket = int(input())
  
  plist.append(player(pname,pcountry,noofmatchs,noofrun,noofwicket))
  
  
obj = team(plist)

ans1 = obj.getminrun()
ans2 = obj.getmaxwicket()

for i in ans1:
  print(i)
  
for i in ans2:
  print(i)
  

        
        
    