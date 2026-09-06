from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack  and ast < 0 < stack[-1]: # if current ast is negative and the top of the stack is positive, it means they are moving towards each other and will collide
                if stack[-1] < abs(ast): # if the top of the stack is smaller than the absolute value of the current asteroid, 
                    # it means the top of the stack will explode and we need to pop it from the stack and continue checking for collisions with the next asteroid in the stack
                    stack.pop()
                    continue
                elif stack[-1] == abs(ast): # if the top of the stack is equal to the absolute value of the current asteroid,
                    # it means both will explode and we need to pop the top of the stack and break out of the for loop and move to next ast
                    stack.pop()
                break
            else:
                stack.append(ast) # if the current asteroid is positive or the stack is empty or the top of the stack is negative,
                # we can safely add the current asteroid to the stack
        return stack

        
    
    
# Example usage:
solution = Solution()

print(solution.asteroidCollision([5, 10, -5])) # [5, 10]
print(solution.asteroidCollision([8, -8])) # []
