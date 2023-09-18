#l1 = [2,4,3]
#l2 = [5,6,4]
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
l11 = l1[::-1]
l22 = l2[::-1]
tt = []
#print(l11)
#print(l22)
n1 = 0
n2 = 0
for i in l11:
  n1 = (n1*10)+i
  
for j in l22:
  n2 = (n2*10) + j
  
t = int(n1) + int(n2)

for i in str(t):
  tt.append(int(i))
  
print(tt[::-1])

