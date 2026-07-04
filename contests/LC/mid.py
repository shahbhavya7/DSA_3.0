class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n = len(nums)
        
        mid = n // 2 + 1 
        mid_elem = nums[mid - 1]  
        
        c = nums.count(mid_elem)
        
        if c == 1:
            return True
        else:
            return False