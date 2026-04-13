from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = len(nums)
        for i, num in enumerate(nums):
            if num == target:
                res = min(res, abs(i - start)) #
        return res
    
# Example usage:
solution = Solution()
print(solution.getMinDistance([1,1,1,1,1,1,1,1,1,1], 1, 9))  # Output: 0