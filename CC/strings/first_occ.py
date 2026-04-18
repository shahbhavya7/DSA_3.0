class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_size = len(haystack)
        n_size = len(needle)
        for i in range(h_size - n_size + 1):
            if haystack[i:i+n_size] == needle:
                return i
        return -1
# Example usage:
solution = Solution()
print(solution.strStr("hello", "ll"))  # Output: 2
        