class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        if root.val == p.val or root.val == q.val: # if root is either p or q, then root is the LCA 
            return root
        
        leftsubtree = self.lowestCommonAncestor(root.left, p, q)
        rightsubtree = self.lowestCommonAncestor(root.right, p, q)
        
        if leftsubtree and rightsubtree: # if both left and right subtrees return a value equal to p or q, then root is the LCA
            return root
        
        if leftsubtree: # if leftsubtree is not None, then it means that either p or q is found in the left subtree, so we return leftsubtree
            return leftsubtree
        
        if rightsubtree: # if rightsubtree is not None, then it means that either p or q is found in the right subtree, so we return rightsubtree
            return rightsubtree
        