from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_indices = {} # we will use a dictionary to store the indices of the numbers we have seen so far
        for i, num in enumerate(nums): # enumerate will give us both the index and the number at that index
            complement = target - num
            if complement in pair_indices: # if the complement is in the dictionary it means we have found a pair of numbers that add up to the target
                return [pair_indices[complement], i] # we return the indices of the complement and the current number
            pair_indices[num] = i # else we add the current number and its index to the dictionary
        return [] # if we have gone through the entire list and haven't found a pair we return
    
# Example usage
sol = Solution()
nums = [2, 7, 11, 15]
target = 9
print(sol.twoSum(nums, target)) # Output: [0, 1] because nums[0] + nums[1] = 2 + 7 = 9