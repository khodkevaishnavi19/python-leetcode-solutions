class Solution:
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            n = nums[i]
            total = 0
            while n > 0:
                total = total + n % 10
                n = n // 10
            
            if total == i:
                return i
        
        return -1
        