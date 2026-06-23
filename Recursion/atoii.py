class Solution:
    def helperr(s, i, num, sign):
        if i >= len(s) or not s[i].isdigit():
            return num * sign
        
        num = num * 10 + int(s[i])
        
        if num * sign < -2**31:
            return -2**31
        if num * sign > 2**31 - 1:
            return 2**31 - 1
        
        return Solution.helperr(s, i + 1, num, sign) # for next digit, we call the function recursively with updated index and number
    
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s) 
       
        while i < n and s[i] == ' ':
            i += 1
            
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            else:
                sign = 1
            i += 1
            
        return Solution.helperr(s, i, 0, sign)
        
        
# Example usage
s = "   -42"
solution = Solution()
result = solution.myAtoi(s)
print(result)  # Output: -42