def getsponser(slist,scat):
  name = []
  for i in slist:
    if i.scat.lower() == scat.lower():
      name.append(i.sname)
      
  name.sort()
  for i in name:
    return i
      
      
def findsponserwithmaxtieups(slist):
  mx = 0
  for i in slist:
    if len(i.stieups) > mx:
      mx = len(i.stieups)
      
  for j in slist:
    if len(j.stieups) == mx:
      name = j.sname
      
  return name
  
    


class sponser:
  def __init__(self,sname,scompany,stieups,scat):
    self.sname = sname
    self.scompany = scompany
    self.stieups = stieups
    self.scat = scat
    


n = int(input())
slist = []

for i in range(n):
  sname = input()
  scompany = input()
  stieups = int(input())
  mytups = []
  for j in range(stieups):
    t = input()
    mytups.append(t)
  scat = input()
  
  slist.append(sponser(sname,scompany,mytups,scat))
  
scat = input()

ans1 = getsponser(slist,scat)
print(ans1)

ans2 = findsponserwithmaxtieups(slist)
print(ans2)

