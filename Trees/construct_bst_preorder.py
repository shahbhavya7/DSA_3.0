class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def helper(self, preorder: list[int], bound: int) -> TreeNode | None:
        if self.index >= len(preorder) or preorder[self.index] > bound:
            return None
        
        rootVal = preorder[self.index]
        root = TreeNode(rootVal)
        self.index += 1
        
        root.left = self.helper(preorder, rootVal) # we set the bound for the left subtree to be the value of the current root, since all values in the 
        # left subtree must be less than the root's value, while recursion comes we attach the left subtree to the current root node
        root.right = self.helper(preorder, bound) # we set the bound for the right subtree to be the same as the current bound that comes from above,
        # since all values in the right subtree must be less than the current bound but greater than the root's value
        
        return root # goes back up the recursion stack, returning the constructed subtree and control to parent node
    
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        self.index = 0
        return self.helper(preorder, float("inf"))
