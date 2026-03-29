class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l  = res = 0 
        for idx, char in enumerate(s):
            if char in seen and seen[char] >= l: # if the character is in the seen dictionary and its index is greater than or equal to the left pointer 
            # if seen[char] >= l it means that the repeating character is within the current window of the substring we are considering
                l = seen[char] + 1 # we need to move the left pointer to the right of the last occurrence of the repeating character
            seen[char] = idx # we need to update the index of the current character in the seen dictionary
            res = max(res, idx - l + 1) # we need to update the result with the maximum length of the substring without repeating characters
        return res