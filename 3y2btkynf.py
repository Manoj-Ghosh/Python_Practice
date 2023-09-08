class object:
  def __init__(self,no,name,c,l,li,s):
    self.no = no
    self.name = name
    self.c = c
    self.l = l
    self.li = li
    self.s = s
    
    
class main:
  def __init__(self,elist,ddict):
    self.elist = elist
    self.ddict = ddict
    
    
  def fun1(self,ids):
    for i in self.elist:
      if i.no == ids:
        avg = sum(i.li)/7
        if avg > 6:
          for p in self.ddict:
            if i.l.lower() == p.lower():
              
              co = i.c + (i.c * self.ddict[p]*0.01)
    print(co) 
    
  
  def fun2(self,loc,pr):
    d =  {}
    for i in self.elist:
      if i.l.lower() == loc.lower():
        if i.s.lower() == "available":
         
          if i.c < pr:
            #d =  {}
            d[i.name] = i.c
            
    di = dict(sorted(d.items(),key = lambda x:x[1],reverse = True))
   # print(di)
    if di:
      for i in di:
        print(i,di[i])
        break
    else:
      print("no match found!!")
      
  
  
n = int(input())
elist = []

for i in range(n):
  no = int(input())
  name = input()
  c = int(input())
  l = input()
  rl = []
  for j in range(7):
    r = int(input())
    rl.append(r)
    
  s= input()
  
  elist.append(object(no,name,c,l,rl,s))
  
pdict = {}

for j in range(4):
  l = input()
  p = int(input())
  pdict[l]=p 
  
iids = int(input())
iloc = input()
ic = int(input())

obj = main(elist,pdict)

obj.fun1(iids)
obj.fun2(iloc,ic)


