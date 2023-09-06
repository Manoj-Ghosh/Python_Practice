class cricketplayer:
  def __init__(self,pname,pcountry,page,pcountryform):
    self.pname = pname
    self.pcountry = pcountry
    self.page = page
    self.pcountryform = pcountryform
    
    
class solution:
  def __init__(self,plist):
    self.plist = plist
    
  def countplayer(self,cname):
    c = 0
    for i in self.plist:
      if i.pcountryform.lower() == cname.lower():
        c += 1
    return c 
    
    
  
  
  def getplayerplayedformaxcountry(self):
    dict = {}
    name = []
    for i in self.plist:
      dict[i.pname] = len(i.pcountry)
        
    l = max(dict.values())
    
    for j in dict:
      if dict[j] == l:
        name.append(j)
    
    return name
    
  
n = int(input())
plist = []
for i in range(n):
  pname = input()
  pcountry = int(input())
  clist = []
  for j in range(pcountry):
    clist.append(input())
  page = int(input())
  pcountryfrom = input()
  clist = set(clist)
  
  plist.append(cricketplayer(pname,clist,page,pcountryfrom))
  
cname = input()

obj = solution(plist)

print("player of the same country : ",obj.countplayer(cname))

a = obj.getplayerplayedformaxcountry()

for i in a:
  print("player played max match against diff countery: ",i)


  
  
    
  