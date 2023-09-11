class Employee:
  def __init__(self,ename,eid,eage,egender):
    self.ename = ename
    self.eid = eid
    self.eage = eage
    self.egender = egender
    
class Organization:
  def __init__(self,oname,elist):
    self.oname = oname
    self.elist = elist
    
  def add_employee(ename,eid,eage,egender):
    e = Employee(ename,eid,eage,egender)
    self.elist.append(e)
    
    
  def view_employee(self):
    for i in self.elist:
      print(i.ename)
      print(i.eid)
      print(i.eage)
      print(i.egender)
      
      
  def employee_count(self):
    print("total count of employee:",len(self.elist))
    
  def find_employee(self,eid):
    for i in self.elist:
      if i.eid == eid:
        age = i.eage
    return age
    
  def count_employee(self,age):
    c = 0
    for j in self.elist:
      if j.eage > age:
        c += 1 
    return c 
    
    
elist = []
n = int(input())

for i in range(n):
  ename = input()
  eid = int(input())
  eage = int(input())
  egender = input()
  
  elist.append(Employee(ename,eid,eage,egender))
  
  
  
obj = Organization("MSG GROUP",elist)

obj.view_employee()

eid = int(input())

r = obj.find_employee(eid)
print("the age of the employee is :",r,"whose id = ",eid)

eage = int(input())

r1 = obj.count_employee(eage)
print("count of employee whose age is greater than ",eage,"is: ",r1)
  