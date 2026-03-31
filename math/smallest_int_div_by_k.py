class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k == 1: return 1
        if k % 2 == 0 or k % 5 == 0: return -1
        remainder = 0
        for length in range(1, k + 1): # range till k as after k, the remainders will start repeating and we will never get a remainder of 0
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length
        return -1
    
# Example usage
sol = Solution()
k = 3
result = sol.smallestRepunitDivByK(k)
print(f"The length of the smallest repunit divisible by {k} is: {result}")