class Solution:
    def minDays(self, n: int) -> int:
        award = 0
        min_day = 0
        sk = 1   
        while award != n:
            if award + sk <= n:
                award += sk
                sk += 1
                min_day += 1
            else:
                sk = 1
                min_day += 1        
        return min_day
    
# Example usage:
if __name__ == "__main__":
    solution = Solution()
    n = 2
    result = solution.minDays(n)
    print(result)  # Output: 4
                
        