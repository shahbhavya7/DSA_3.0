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
        
        root.left = self.helper(preorder, rootVal)
        root.right = self.helper(preorder, bound)
        
        return root # goes back up the recursion stack, returning the constructed subtree and control to parent node
    
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        self.index = 0
        return self.helper(preorder, float("inf"))
