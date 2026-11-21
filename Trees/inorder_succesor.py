from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        successor = None
        
        while root:
            
            if p.val >= root.val: # if the value of p is greater than or equal to the value of the current root, we move to the right subtree to find a larger value that could be the successor
                root = root.right
            else: # if the value of p is less than the value of the current root, we update the successor to the current root and move to the left subtree to find a smaller value that could be the successor
                successor = root
                root = root.left
                
        return successor
    
    def inorderPredecessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        predecessor = None
        
        while root:
            
            if p.val <= root.val:
                root = root.left
            else:
                predecessor = root
                root = root.right
                
        return predecessor
    