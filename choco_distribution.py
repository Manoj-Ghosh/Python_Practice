def find_min_diff(arr,m,n):
  
  if m == 0 or n == 0:
    return 0
    
  if m > n:
    return -1
  
  
  arr.sort()
  
  min_diff = arr[n-1] - arr[0]
  #print(min_diff)
  
  
  for i in range(n-m+1):
    min_diff = min(arr[i+m-1] - arr[i], min_diff)
    
  return min_diff
  
  
#arr = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
#m = 7
arr = [3, 4, 1, 9, 56, 7, 9, 12]


m = 5
n = len(arr)

print("minimum difference is : ", find_min_diff(arr,m,n))


