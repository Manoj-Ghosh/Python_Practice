#print("please enter your date in format(DD/MM/YYYY)")
d1 = input("please enter your date in format(DD/MM/YYYY)\n")
#d2 = input()
date1, month1, year1 = d1.split("/")
#date2, month2, year2 = d1.split("/")

if int(month1) > 0 and int(month1) < 13:
  dic = {"01":"January", "02":"February", "03":"March","04":"April","05":"May","06":"June","07":"July","08":"August","09":"September","10":"October","11":"November","12":"December"}
  for i in dic:
    if i == month1:
      print(date1, dic[i], year1)
      
else:
  print("your input is not correct!!")
