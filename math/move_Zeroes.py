from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0) 
        for _ in range(zero_count): # loop from 0 to zero_count - 1
            nums.remove(0)
            nums.append(0)
# Example usage:
solution = Solution()
nums = [0, 1, 0, 3, 12]
solution.moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]