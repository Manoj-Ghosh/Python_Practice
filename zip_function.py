list1 = [1,2,3,4,5,6]
list2 = [7,8,9,10,11,12]
final = list(zip(list1,list2))
print(final)

for i in final:
  for j in i:
    print(j)
    