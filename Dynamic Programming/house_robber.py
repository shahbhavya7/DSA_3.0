from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums) #initialize dp array with 0s
        dp[0] = nums[0] #base case: rob the first house
        dp[1] = max(nums[0], nums[1]) #base case: rob the second house or the first house, whichever is greater
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2]) #either skip the current house and take the maximum from the previous house, or rob the current house and add it to the maximum from two houses back
        
        return dp[-1] #the last element of the dp array will contain the maximum amount that can be robbed
    
# Example usage:
nums = [1,2,3,1]
solution = Solution()
print(solution.rob(nums))  # Output: 4 (rob house 1 and 3)