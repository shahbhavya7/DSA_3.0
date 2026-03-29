from typing import List

class SolutionBruteForce:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen  = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = True
        return False
    
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       return len(set(nums)) != len(nums)
    
# Example usage
sol = Solution()
nums = [1, 2, 3, 1]
print(sol.containsDuplicate(nums)) # Output: True because 1 appears twice in the array