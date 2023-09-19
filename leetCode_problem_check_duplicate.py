class Solution():
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        li = []
        for i in nums:
            if i in li:
                return True
            li.append(i)
        return False
        
n = int(input())

nums = []
for i in range(n):
  nu = int(input())
  nums.append(nu)
  
obj = Solution()

ans = obj.containsDuplicate(nums)

print(nums)

print(ans)
