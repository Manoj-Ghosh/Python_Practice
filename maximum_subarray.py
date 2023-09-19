class Solution():
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        db = []
        db.append(nums[0])
        current_largest_sum = db[0]
        for i in range(1,len(nums)):
            db.append(max(db[i-1] + nums[i], nums[i]))
        
            if db[i] > current_largest_sum:
                current_largest_sum = db[i]
                
        return current_largest_sum, db
            
            
nums = [-2,1,-3,4,-1,2,1,-5,4]
obj = Solution()
ans1, ans2 = obj.maxSubArray(nums)
print(ans1)
print(ans2)

