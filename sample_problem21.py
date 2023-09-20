n = int(input())
arr = list(map(int, input().split(":")))[:n]
print(*arr)
k = int(input())
for i in range(k):
  x = arr.pop(-1)
  arr.insert(0,x)
print(*arr)

