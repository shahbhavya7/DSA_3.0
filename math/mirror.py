class Solution:
    def mirrorDistance(self, n: int) -> int:
        if n < 10:
            return 0
        str_n = str(n)
        mirror_str = str_n[::-1] 
        mirror_n = int(mirror_str)
        return abs(n - mirror_n)
# Example usage:
solution = Solution()
print(solution.mirrorDistance(25))  # Output: 198