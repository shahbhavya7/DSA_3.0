class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    def travel(self,node):
        if not node:
            return [0,0]
        
        left = self.travel(node.left)
        right = self.travel(node.right)
        
        options = [0,0] # initialize an array to store the maximum values for robbing and not robbing this node

        # rob this node, then we cannot rob its children, so we take the value of this node and add the values of not robbing its children
        
        options[0] = node.val + left[1] + right[1]
        
        # don't rob this node, then we can choose to rob or not rob its children, so we take the maximum of robbing or not robbing its children
        options[1] = max(left[0], left[1]) + max(right[0], right[1])
        
        return options
        
    
    def rob(self, root: TreeNode | None) -> int:
        options = self.travel(root)
        return max(options[0], options[1])
    

        
        