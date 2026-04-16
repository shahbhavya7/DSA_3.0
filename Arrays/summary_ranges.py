from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        final = []
        a, b = 0, 1
        for i in range(len(nums)):
            if b < len(nums) and nums[b] - nums[i] == 1:
                b += 1
            else:
                if a == b - 1:
                    final.append(str(nums[a]))
                else:
                    final.append(str(nums[a]) + "->" + str(nums[b - 1]))
                a = b
                b += 1
        return final
               
    
# Example usage:
solution = Solution()
print(solution.summaryRanges([0,1,2,4,5,7]))  # Output: ["0->2","4->5","7"]