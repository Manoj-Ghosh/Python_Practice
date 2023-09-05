class doctor:
  def __init__(self,d_ids,d_name,d_sep,d_fee):
    self.d_ids = d_ids
    self.d_name = d_name
    self.d_sep = d_sep
    self.d_fee = d_fee
    
    
class hospital:
  
  def searchdoctbyname(self,d_name,doctordb):
    c = 0
    for i in doctordb.values():
      if i.d_name == d_name:
        c += 1 
        print(i.d_name)
        print(i.d_ids)
        print(i.d_sep)
        print(i.d_fee)
        print("++++++++")
        
    if c == 0:
      print("NO MATCH FOUND WITH THE GIVEN NAME")
      
      
      
  def calculatefeeswithsep(self,d_sep,doctordb):
    fees = 0
    for i in doctordb.values():
      if i.d_sep == d_sep:
        fees += i.d_fee
        
        
    if fees == 0:
      print("NO MATCH FOUN WITH THE SPECIFICATION")
      
    else:
      print(fees)
      
      
      
      
n = int(input())
dict = {}


for i in range(n):
  ids = int(input())
  name = input()
  sep = input()
  fees = int(input())
  
  dict[i+1]  = doctor(ids,name,sep,fees)
  
  
dname = input()
dsep = input()

obj = hospital()

obj.searchdoctbyname(dname,dict)

obj.calculatefeeswithsep(dsep,dict)

#print(list(dict.values()))
  
      