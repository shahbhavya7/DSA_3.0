class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        start = 0
        end  = len(s) - 1
        biggest = ""
        string = ""
        while start <= end:
            if s[start] == s[end]:
                string = s[start] + string + s[end]
                start += 1
                end -= 1
                if len(string) > len(biggest):
                    biggest = string
            else:
                string = ""
                end -= 1
        return biggest
# Example usage:
s = "babad" 
solution = Solution()
print(solution.longestPalindrome(s))  # Output: "aba" or "bab"