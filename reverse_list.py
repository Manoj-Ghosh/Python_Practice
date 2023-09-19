def reverse_list(a,start, end):
  if  start >= end:
    return 
  a[start], a[end] = a[end], a[start]
  reverse_list(a,start+1, end-1)
    
  return a
  
  
  
a = [78, 25, 48, 36, 84, 12, 73, 74]
start = 0
end = len(a) - 1 
ans = reverse_list(a, start, end)
print(ans)
