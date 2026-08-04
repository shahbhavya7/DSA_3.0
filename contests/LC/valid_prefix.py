from typing import List

class Solution:
    def countValidPrefixes(self, s: str) -> int:
        
        count_zero = 0
        count_one = 0
        
        valid_total = 0
        
        for char in s:
            if char == '0':
                count_zero += 1
            else:
                count_one += 1
            
            if abs(count_zero - count_one) <= 1:
                valid_total += 1
                
        return valid_total