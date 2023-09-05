class parkedvehicles:
  def __init__(self,vseq,fourwheeler,parkedfor,valetparking,parkedstatus):
    self.vseq = vseq
    self.fourwheeler = fourwheeler
    self.parkedfor = parkedfor
    self.valetparking = valetparking
    self.parkedstatus = parkedstatus
    
class parkinglot:
  def __init__(self,location_id,parked_vehicles):
    self.location_id = location_id
    self.parked_vehicles = parked_vehicles
    
    
  def updateparkedststus(self,lot_number):
    if lot_number in self.parked_vehicles:
      self.parked_vehicles[lot_number].parkedstatus ="cleared"
      return (lot_number,self.parked_vehicles[lot_number].parkedstatus)
    return None
      
    
  def getparkingcharges(self,lot_number):
    amount = 0
    if self.parked_vehicles[lot_number].fourwheeler == "yes":
      amount += 50 * self.parked_vehicles[lot_number].parkedfor
      
    else:
      amount += 30 * self.parked_vehicles[lot_number].parkedfor
      
    if self.parked_vehicles[lot_number].valetparking == "yes":
      amount += 10
      
    return amount
    
    
    
    
n = int(input())

parked_vehicles = {}

for i in range(n):
  
  vseq = int(input())
  fourwheeler = input()
  parkedfor = float(input())
  valetparking = input()
  parkedstatus = "parked"
  lot_number = int(input())
  
  parked_vehicles[lot_number] = parkedvehicles(vseq,fourwheeler,parkedfor,valetparking,parkedstatus)
  
lot_number1 = int(input())

obj = parkinglot("chenni",parked_vehicles)

ans = obj.updateparkedststus(lot_number1)

if ans != None:
  print(ans)
  print(obj.getparkingcharges(lot_number1))
  
else:
  print("None")
  print("None")
  