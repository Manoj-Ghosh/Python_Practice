num = list(range(1,6,1))
num1 = num[-3:-1]# + num[4] + num[0:2]
print(num)
print(num1)


"""num2 = list(range(1,6,1))
num3 = num[-3:-1] + list(num[4]) + num[0:2] // not possible like this
print(num2)
print(num3)"""


num2 = list(range(1,6,1))
num3 = num[4]
new_list = []
new_list.append(num3)
num4=num[-3:-1] + new_list + num[0:2]
print(num4)
