# recursive solution
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2) # the number of ways to climb n stairs is the sum of the ways to climb n-1 and n-2 stairs
        # for n stairs, you can either take a single step from n-1 or a double step from n-2, so the total ways to climb n stairs is the sum of these two possibilities
        # for example, to climb 3 stairs, you can take a single step from 2 stairs (which has 2 ways) or a double step from 1 stair (which has 1 way), resulting in a total of 3 ways to climb 3 stairs
        # so when n is 3, the function will return climbStairs(2) + climbStairs(1) which is 2 + 1 = 3, and for n=4, it will return climbStairs(3) + climbStairs(2) which is 3 + 2 = 5, and so on, 
        # following the Fibonacci sequence pattern where each number is the sum of the two preceding ones.

    # memoization (top-down)
    def climbStairsMemo(self, n: int, memo={}):
        if n in memo: # check if the result for n is already computed and stored in the memo dictionary
            return memo[n] # if it is, return the stored value to avoid redundant calculations
        if n <= 2:
            return n
        memo[n] = self.climbStairsMemo(n-1, memo) + self.climbStairsMemo(n-2, memo) # compute the value for n and store it in the memo dictionary before returning it
        return memo[n] # return the computed value for n
    
    # tabulation (bottom-up)
    def climbStairsTab(self, n: int):
        if n <= 2:
            return n
        dp = [0] * (n + 1) # create a list to store the number of ways to climb stairs up to n, initialized with zeros
        dp[1] = 1 # base case: there is 1 way to climb 1 stair
        dp[2] = 2 # base case: there are 2 ways to climb 2 stairs (1+1 or 2)
        for i in range(3, n + 1): # fill the dp list iteratively from 3 to n
            dp[i] = dp[i - 1] + dp[i - 2] # each entry is the sum of the two preceding entries, following the same logic as the recursive solution
        return dp[n] # return the number of ways to climb n stairs, which is stored in dp[n]
    
    # space optimized version
    def climbStairsSpaceOptimized(self, n: int):
        if n <= 2:
            return n
        a, b = 1, 2 # initialize the first two values for climbing stairs (1 way to climb 1 stair and 2 ways to climb 2 stairs)
        for _ in range(3, n + 1): # iterate from 3 to n
            a, b = b, a + b # update a and b to the next two values in the sequence, where a becomes the previous value of b and b becomes the sum of the previous a and b
        return b # after the loop, b will hold the number of ways to climb n stairs


# example usage
solution = Solution()
print(solution.climbStairs(3))  # Output: 8