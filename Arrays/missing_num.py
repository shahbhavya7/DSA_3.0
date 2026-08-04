from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        missing_elements = []
        
        sorted_nums = sorted(nums)
        
        smallest_num = sorted_nums[0]
        largest_num = sorted_nums[-1]
        
        for num in range(smallest_num, largest_num + 1):
            if num not in sorted_nums:
                missing_elements.append(num)
                
        return missing_elements
    
# Example usage:
solution = Solution()

nums = [3, 7, 1, 2, 8, 4, 5]
missing_elements = solution.findMissingElements(nums)
print("Missing elements:", missing_elements)  # Output: Missing elements: [6]