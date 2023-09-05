class vegetables:
  def __init__(self,v_name,v_price,v_quamts):
    self.v_name = v_name
    
    self.v_price = v_price
    self.v_quants = v_quants
    
    
class store:
  def __init__(self,store_name,veg_list):
    self.store_name = store_name
    self.veg_list = veg_list
    
    
  def categorizedvegtablesAlphabetically(self):
    dict = {}
    for i in self.veg_list:
      if i.v_name[0] not in dict:
        dict[i.v_name[0]] = [] #empty list
        dict[i.v_name[0]].append(i.v_name) #append vale in emptylist
    for i in sorted(dict):
      print(i)
      for j in sorted(dict[i]):
        print(j)
            
      
  def filtervegforpricerange(self,min_pice,max_price):
    l= []
    for i in self.veg_list:
      #print(i.v_price)
      if min_price <= i.v_price and i.v_price <= max_price:
        #print(i.v_name)
        l.append(i.v_name)
        #li = li.sort()
    
    if len(l) != 0:
      print("========")
      for i in sorted(l):
       print(i)
        
    else:
      print("No veg in the given price criteria")
      
      
n= int(input())
veg_list = []
for i in range(n):
  v_name = input()
  v_price = int(input())
  v_quants = int(input())
  
  veg_list.append(vegetables(v_name,v_price,v_quants))
  
store_name = input()
min_price = int(input())
max_price = int(input())

obj = store(store_name,veg_list)

obj.categorizedvegtablesAlphabetically()

obj.filtervegforpricerange(min_price,max_price)
