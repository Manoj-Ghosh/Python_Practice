class flower:
  def __init__(self,fid,fn,fp,fr,ft):
    self.flowerid = fid
    self.flowername = fn
    self.flowerprice = fp
    self.flowerrating = fr
    self.flowertype = ft
    
    
class solution:
  def __init__(self,flist):
    self.flist = flist
    
  def findminpricebytype(self,type):
    l = []
    for i in self.flist:
      if i.flowertype.lower() == type.lower():
        if i.flowerrating > 3:
          l.append(i.flowerprice)
          
          
    if len(l) == 0:
      print("condition not satisfied!!")
      
      
      
    else:
      
      m = min(l)
    
      for j in self.flist:
        if j.flowerprice == m:
          
          print(j.flowerid,"\t",j.flowername,"\t",j.flowerprice)
          
        
        
n = int(input())
flist = []
for i in range(n):
  fid = int(input())
  fn = input()
  fp = float(input())
  fr = int(input())
  ft = input()
  flist.append(flower(fid,fn,fp,fr,ft))
  
t = input()

obj = solution(flist)

obj.findminpricebytype(t)



        