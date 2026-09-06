class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack: # if the stack is empty, it means there is no matching opening bracket for the current closing bracket
                    return False
                top = stack.pop()
                if (char == ')' and top != '(') or (char == '}' and top != '{') or (char == ']' and top != '['):
                    return False
        return not stack # if the stack is empty, it means all opening brackets have been matched with closing brackets
    
    
# Example usage:
solution = Solution()

print(solution.isValid("()")) # True
print(solution.isValid("()[]{}")) # True
print(solution.isValid("(]")) # False
 