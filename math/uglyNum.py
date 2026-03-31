class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0: return False
        while n % 2 == 0: n //= 2
        while n % 3 == 0: n //= 3
        while n % 5 == 0: n //= 5
        return n == 1
    
# Example usage
sol = Solution()
n = 14
if sol.isUgly(n):
    print(f"{n} is an ugly number.")
else:    
    print(f"{n} is not an ugly number.")