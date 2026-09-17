from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right # Initialize the answer to the maximum pile size, as this is the worst-case scenario for eating speed 
        # i.e., if Koko eats at the speed of the largest pile, eg: [3, 6, 7, 11], h = 8, the maximum eating speed is 11, which is the largest pile size.
        # if Koko eats at the speed of 11, she will take one hour to eat the largest pile,
        # and she will take 3 hours to eat the other piles, which is a total of 4 hours, which is less than h = 8.
        # so, the answer is 11. But we can try to find a smaller eating speed that allows Koko to eat all bananas within h hours.
        # binary search os between 1 and the maximum pile size to find the minimum eating speed that allows Koko to eat all bananas within h hours.
        
        while left <= right:
            mid = (left + right) // 2 # Calculate the middle eating speed
            
            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid # Calculate the total hours needed to eat all piles at speed mid
                # pile + mid - 1 is used to round up the division, as Koko can only eat whole bananas and cannot eat a fraction of a banana.
                # same as math.ceil(pile / mid), but without importing the math module. 
                
            if hours <= h: # If the total hours is less than or equal to h, it is okay but we can try to find small eating speed
                ans = mid
                right = mid - 1
            else: # If the total hours is greater than h, we need to increase the eating speed
                left = mid + 1
            
        return ans # Return the minimum eating speed that allows Koko to eat all bananas within h hours
    
# Example usage:
solution = Solution()
piles = [3, 6, 7, 11]
h = 8
print(solution.minEatingSpeed(piles, h))  # Output: 4