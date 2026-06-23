class Solution:
    
    def helper(self, x: float, n: int) -> float:
        if n == 0: return 1
        
        if n % 2 == 0:
            return self.helper(x * x, n // 2)
        else:
            return x * self.helper(x, n - 1)
    
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        return self.helper(x, n)


# Example usage
solution = Solution()
x = 2.0
n = 10
result = solution.myPow(x, n)
print(result)  # Output: 1024.0