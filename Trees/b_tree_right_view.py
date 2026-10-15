from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        ans = []
        
        q = deque()
        q.append(root)
        
        while q:
            right_side = None
            
            for _ in range(len(q)): # level wise traversal
                node = q.popleft() # pops the leftmost node in the queue
                
                if node:
                    right_side = node
                    q.append(node.left)
                    q.append(node.right)
         
            if right_side:
                ans.append(right_side.val)

            # as this condition sits outside for loop, it will only be executed once per level, 
            # and the last node processed in that level will be the rightmost node as we are traversing from left to right. 
            # Hence, we can append the value of the rightmost node to the answer list.
            
        return ans
    

                
                