date = input()
dd, mm, yyyy = date.split("/")
a = ["1","3","5","7","9","11"] # 31 days
b = ["4","6","8","10","12"] # 30days month
if int(mm) > 0  and int(mm) < 13 :
  #print("valid month")
  
  if mm in a:
    maxx = 31
  
  elif mm in b:
    
    maxx = 30
   
   
  #if mm == 2:
  else:
    
    if int(yyyy) % 4 == 0 and int(yyyy) % 100 != 0 and int(yyyy) % 400 != 0 :
      maxx = 29
    
    else:
      maxx = 28
    
    
  if int(dd) > 0 and int(dd) <= maxx:
    print("valid date")
    
  else:
    print("invalid date !!")
    
    
  
    
  