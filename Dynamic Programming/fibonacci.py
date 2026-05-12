# normal recursive solution
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))  # Output: 55

# memoization (top-down)
def fib_memo(n, memo={}): # memo is passed as a default argument to avoid reinitialization of the dictionary on every function call, 
    # the same dictionary will be used across all calls to fib_memo
    if n in memo: # if n is already computed at some point, return the stored value from the memo dictionary
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo) # compute the value for n and store it in the memo dictionary before returning it, 
    # so that future calls with the same n can return the stored value directly without redundant calculations
    return memo[n]

print(fib_memo(10))  # Output: 55

# tabulation (bottom-up)
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1) # create a list to store Fibonacci values up to n, initialized with zeros
    dp[1] = 1 # base case: F(1) = 1
    for i in range(2, n + 1): # fill the dp list iteratively from 2 to n
        dp[i] = dp[i - 1] + dp[i - 2] # each Fibonacci number is the sum of the two preceding ones
    return dp[n] # return the nth Fibonacci number

print(fib_tab(10))  # Output: 55

# space optimized version
def fib_space_optimized(n):
    if n <= 1:
        return n
    a, b = 0, 1 # initialize the first two Fibonacci numbers
    for _ in range(2, n + 1): # iterate from 2 to n
        a, b = b, a + b # update a and b to the next two Fibonacci numbers
    return b # after the loop, b will hold the value of F(n)