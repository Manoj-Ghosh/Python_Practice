class fooditem:
  def __init__(self,ids,name,cat,price):
    self.ids = ids
    self.name = name
    self.cat = cat
    self.price = price
    
  def providediscount(self,per):
    self.price -= self.price * per * 0.01
    return self.price
    
class resturent:
  def __init__(self,rname,flist):
    self.rname = rname
    self.flist = flist
    
    
  def updatedprice(self,ids,per):
    if per > 0:
      for i in self.flist:
        if i.ids == ids:
          p = i.providediscount(per)
          print(i.name,"\t",p)
          return 0
          
        
    else:
      for i in self.flist:
        if i.ids == ids:
          print(i.name,"\t",i.price)
    
    if per > 0:
      if i.ids not in self.flist:
        print("NO MATCH FOUND!!")
      
      
n = int(input())
elist = []
for i in range(n):
  ids = int(input())
  name = input()
  cat = input()
  price = int(input())
  
  elist.append(fooditem(ids,name,cat,price))
  
rname = input()
per = int(input())
ids = int(input())

obj = resturent(rname,elist)

obj.updatedprice(ids,per)
          
      
  