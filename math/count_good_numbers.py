MOD = 10**9 + 7

class Solution:
    def binaryExponentiation(self, a: int, b: int) -> int:
        res = 1
        while b > 0:
            if b % 2 == 1: # when b is odd halving does not give us the correct result so we multiply res by a so it reduces the power of a by 1 
                # and then we can halve b to get the correct result
                res = (res * a) % MOD
            a = (a * a) % MOD # a is squared so that we can use it for the next iteration
            b //= 2
        return res

    def countGoodNumbers(self, n: int) -> int:
        return (self.binaryExponentiation(5, (n + 1) // 2) * self.binaryExponentiation(4, n // 2)) % MOD


# Example usage
solution = Solution()
n = 4
result = solution.countGoodNumbers(n)
print(f"The count of good numbers of length {n} is: {result}")