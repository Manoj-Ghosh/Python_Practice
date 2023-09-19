def reverse_array(a,start,end):
  while start < end :
    a[start], a[end] = a[end], a[start]
    
    start += 1 
    end -= 1 
    
  return a 
    
a = [25,14,787,96,45,12,7,8]
start = 0 
end = len(a) - 1 
ans = reverse_array(a,start, end)
print(ans)


