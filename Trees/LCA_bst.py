class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        
        if p.val < root.val and q.val < root.val: # if both p and q are smaller than root, then LCA lies in left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        
        if p.val > root.val and q.val > root.val: # if both p and q are greater than root, then LCA lies in right subtree
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root
    