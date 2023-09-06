class music:
  def __init__(self,mplist,mtype,mcount,mduration):
    self.mplist = mplist
    self.mtype = mtype
    self.mcount = mcount
    self.mduration = mduration
    
    
class solution:
  def __init__(self,mlist):
    self.mlist = mlist
    
    
  def findavgofcount(self,c):
    l = []
    for i in self.mlist:
      if i.mcount > c:
        l.append(i.mcount)
    
    if len(l) > 0:
      avg = (sum(l) / len(l))
      #print(avg)
    
      if avg > 0:
        return avg
      
      else:
        return 0
      
      
  def sorttypebyduration(self,d):
    tlist = []
    for i in self.mlist:
      if i.mduration > d:
        tlist.append(i.mtype)
    tlist.sort()
    
    if len(tlist) > 0:
      return tlist
      
    else:
      return 0
      
      
      
      
mlist = []
n = int(input())
for i in range(n):
  mplist = int(input())
  mtype = input()
  mcount = int(input())
  mduration = float(input())
  
  mlist.append(music(mplist,mtype,mcount,mduration))
  
  
c = int(input())
d = float(input())

obj = solution(mlist)

ans1 = obj.findavgofcount(c)

if ans1:
  print(ans1)
  
else:
  print("condition not satisfied!!")
  
  
ans2 = obj.sorttypebyduration(d)

if ans2 != 0:
  for i in ans2:
    print(i)
    
else:
  print("no match found")
  
  
    
  