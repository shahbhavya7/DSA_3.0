from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        def backtrack(open_count, close_count):
            if open_count == close_count == n:
                res.append("".join(stack))
                return
            
            if open_count < n: # if we have not used all the open parentheses, we can add an open parenthesis
                stack.append("(")
                backtrack(open_count + 1, close_count) # go further down the tree with one more open parenthesis
                stack.pop() # coming back up the tree, we remove the last added open parenthesis to explore other possibilities and tree branches
                
            if close_count < open_count: # if we have more open parentheses than close parentheses, we can add a close parenthesis
                stack.append(")")
                backtrack(open_count, close_count + 1) # go further down the tree with one more close parenthesis
                stack.pop() # coming back up the tree, we remove the last added close parenthesis to explore other possibilities and tree branches
                
        backtrack(0, 0) # we start the backtracking with 0 open and 0 close parentheses
        return res
    
# Example usage
solution = Solution()
n = 3
result = solution.generateParenthesis(n)
print(f"The generated parentheses combinations for n={n} are: {result}")

