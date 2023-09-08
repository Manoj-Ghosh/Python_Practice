class Courses:
  def __init__(self,cname,iname,price,subs,sdate,ctype):
    self.cname = cname
    self.iname = iname
    self.price = price
    self.subs = subs
    self.sdate = sdate
    self.ctype = ctype
    
    
class Bootcamp:
  def __init__(self,clist,ddict):
    self.clist = clist
    self.ddict = ddict
    
  def fun1(ctype1,pprice):
    ndict = {}
    for j in self.clist:
      if j.ctype.lower() == ctype1.lower():
        if j.price<pprice:
          for k in self.ddict:
            if j.iname.lower() == k.lower():
              if ddict[k]>6:
                ndict[j.cname] = j.price
    ndict = dict(sorted(ndict.items(),key = lambda x:x[1]))
    return ndict
    
  
  
  def fun2(year):
    amnt = 0
    for i in self.clist:
      if i.sdate == year:
        if i.ctype.lower() == "online":
          for l in i.subs:
            if l.lower() == "python":
              amnt += i.price
              
    if amnt:
      return amnt
    else:
      return None
      
  
  
  
n = int(input())
clist = []

for i in range(n):
  cname = input()
  iname = input()
  price = float(input())
  n1 = int(input())
  slist = []
  for j in range(n1):
    sn = input()
    slist.append(sn)
  sdate = input().split("/")
  date = int(sdate[2])
  ctype = input()
  
  clist.append(Courses(cname,iname,price,slist,date,ctype))
  
  
rdict = {}
for p in range(3):
  k = input()
  v = int(input())
  rdict[k] = v 
  
obj = Bootcamp(clist,rdict)

ictype = input()
iprice = int(input())
iyear = int(input())

ans1 = obj.fun1(ictype,iprice)

if ans1:
  for k in ans1:
    print(k,ans1[k])
    
else:
  print("no match found!!")
  
ans2 = obj.fun2(iyear)
print(ans2)





  
  
  
  
  
  
  
  
  
  
  
  