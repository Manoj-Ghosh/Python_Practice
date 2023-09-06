n = int(input())
stock = list(map(int,input().split(" ")))

from collections import Counter
dict = Counter(stock)

x = int(input())

p=0

for i in range(x):
    size,price = map(int,input().split(" "))
    
    if (dict[size]):
        
        dict[size] -= 1
        p += price
        
print(p)