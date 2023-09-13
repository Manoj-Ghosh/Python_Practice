l = 0
s = input().split(" ")
for i in s:
  l += len(i)
  
print("TOTAL NUMBER OF LETTER IN THE GIVEN STRING: ",l)
  
ll = len(s)
print("TOTAL NUMBER OF WORDS IN THE GIVEN STRING: ",ll)

d = int(l)//int(ll)

d1 = int(l)/int(ll)

print("FLOOR DIVISION : ",d)

print("FLOAT DIVISION : ",d1)


  
