def thirdMax(nums):
  
  nums = list(set(nums))
        
  if len(nums)<3:
    return max(nums)
  else:
    nums.sort(reverse = True)
    return nums[2]
    
n = int(input())
l = []
for i in range(n):
  nums = int(input())
  l.append(nums)
  
ans = thirdMax(l)
print(ans)


  