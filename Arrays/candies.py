from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings) 
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1): # start from second last and -1 for backwards and -1 for stop at 0
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1) # take the max of current candies and the next one + 1
                # it ensures we dont give less candies to the current child if it already has more than the next child + 1 in the first pass
        return sum(candies)
    
# Example usage:
solution = Solution()
ratings = [1, 0, 2]
print(solution.candy(ratings))  # Output: 5