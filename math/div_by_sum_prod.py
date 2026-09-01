class Solution:
    def checkDivisibility(self, n: int) -> bool:
        
        sum = 0
        prod = 1
        num  = n
        
        while n > 0:
            digit = n % 10
            sum += digit
            prod *= digit
            n //= 10
            
        if num % (prod + sum) == 0:
            return True
        return False