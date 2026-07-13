from typing_extensions import List

class Solution:
    
    def helper(self, s, index, current, res):
        
        if index == len(s): # if we reach last level of the tree, we add the current subset to the result and return
            # last level of the tree is when we have considered all elements in the input array and we have either included or excluded each element in the current subset
            res.append(current.copy())
            return
        
        current.append(s[index]) # we include the current element in the subset and go further down the tree
        self.helper(s, index + 1, current, res) # we go further down the tree with the next element in the input array
        current.pop() # while coming back up the tree, we remove the last added element from the current subset to explore other possibilities and tree branches
        self.helper(s, index + 1, current, res) # we go further down the tree with the next element left in input arr, after excluding the current element from the subset
        
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        new_arr = set(nums)
        res = []
        current = []
        
        self.helper(list(new_arr), 0, current, res)
        
        return res
    
# Example usage
solution = Solution()
nums = [1, 2, 2]
result = solution.subsetsWithDup(nums)
print(f"The subsets of {nums} are: {result}")
