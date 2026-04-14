from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        final = []
        a, b = 0, 1
        while b < len(nums):
            if nums[b] - nums[a] == 1:
                b += 1
            else:
                pass