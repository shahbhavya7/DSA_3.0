class Solution:
    def longestConsecutivebrute(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(set(nums))
        longest_streak = 1
        current_streak = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1
                
        return max(longest_streak, current_streak)
    
    
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums) # set as it allows O(1) lookups
        longest_streak = 0
        
        for num in numSet:
            if num - 1 not in numSet: # if num is the start of a sequence, if previous number is not in the set
                length = 1
                while num + length in numSet: # loop will continue until the next number is not in the set, if found, increment the length of the sequence
                    length += 1
                
                longest_streak = max(longest_streak, length)
        return longest_streak  