class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        t = len(nums)
        res = [1] * t
        
        left = 1
        right = 1
        
        for i in range(t):
            res[i] = left
            left *= nums[i]
            
        for i in range(t - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
            
        return res