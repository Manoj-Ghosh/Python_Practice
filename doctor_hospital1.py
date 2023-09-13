class Doctor:
  
  def __init__(self,did,dname,dspec,dfee):
    self.did = did
    self.dname = dname
    self.dspec = dspec
    self.dfee = dfee
    
class Hospital:
  
  def __init__(self,doctordb):
    self.doctordb = doctordb
    
  def search_by_doctor_name(self,idname):
    dlist = []
    for i in self.doctordb.values():
      
      if i.dname.lower() == idname.lower():
        dlist.append(i)
        
    return dlist
    
    
  def calculate_fee_by_spec(self,idspec):
    fee = 0
    for i in self.doctordb.values():
      if i.dspec.lower() == idspec.lower():
        fee += i.dfee
        
    return fee
  
  
  
n = int(input())
doctordb = {}
for i in range(n):
  did = int(input())
  dname = input()
  dspec = input()
  dfee = int(input())
  
  obj = Doctor(did,dname,dspec,dfee)
  
  doctordb[did] = obj
  
idname = input()

idspec = input()

objj = Hospital(doctordb)

ans1 = objj.search_by_doctor_name(idname)

if ans1:
  for i in ans1:
    print(i.did)
    print(i.dname)
    print(i.dspec)
    print(i.dfee)
    
else:
  print("No doctor found with this name!!")
  
  
ans2 = objj.calculate_fee_by_spec(idspec)

if ans2 :
  print(ans2)
  
else:
  print("No doctor found with the given speclization!!")


