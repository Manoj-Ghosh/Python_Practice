class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c = 0
        li = []
        n = len(nums)
        for i in nums:
          for j in range(n):
            if i == nums[j]:
              c += 1 
              
          print(c)    
          if c >= 2:
            return True 
          else:
            return False 
            
          
nums = [2, 14, 18, 22, 22]
obj = Solution()
ans = obj.containsDuplicate(nums)
print(ans)
