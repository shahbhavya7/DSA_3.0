class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cnt = 0
        while left != right:
            left >>= 1
            right >>= 1
            cnt += 1
        return left << cnt
    
# Example usage
sol = Solution()
left = 5
right = 7
result = sol.rangeBitwiseAnd(left, right)
print(f"The bitwise AND of all numbers in the range [{left}, {right}] is: {result}")

# The idea is to right shift both left and right until they are equal, counting the number of shifts. This effectively finds the common prefix of left and 
# right in binary form. Once we have the common prefix, we left shift it back by the count of shifts to get the final result.
# For example, for left = 5 (101 in binary) and right = 7 (111 in binary):
# - After 1 right shift: left = 2 (10 in binary), right = 3 (11 in binary), cnt = 1
# - After 2 right shifts: left = 1 (1 in binary), right = 1 (1 in binary), cnt = 2
# Now left and right are equal, so we take left (which is 1) and left shift it back by cnt (2) to get 1 << 2 = 4, 
# which is the bitwise AND of all numbers in the range [5, 7].
# We keep the part where bits are stable (don’t change across the range), and we zero out the unstable part because those bits will inevitably become 
# 0 during AND anyway. If a bit changes even once in the range → it is guaranteed to become 0 in the final AND result beacuse of the nature of AND operation.
# i.e 1 AND 0 = 0, so if a bit changes from 1 to 0 or from 0 to 1 at any point in the range, it will contribute a 0 to the final result.
# only same bits like 1 AND 1 = 1 and 0 AND 0 = 0 will contribute to the final result, so we keep the common prefix and zero out the rest.