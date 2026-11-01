class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    def helper(self, preorder: list[int], inorder: list[int], preIdx: int, left: int, right: int) -> TreeNode | None:
        if left > right:
            return None
        
        rootVal = preorder[preIdx]
        root = TreeNode(rootVal)
        
        index = inorder.index(rootVal) # search for the index of the root value in the inorder list to determine the boundary between left and right subtrees
        
        root.left = self.helper(preorder, inorder, preIdx + 1, left, index - 1)
        root.right = self.helper(preorder, inorder, preIdx + (index - left) + 1, index + 1, right)
        
        return root # goes back up the recursion stack, returning the constructed subtree and control to parent node
    
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        return self.helper(preorder, inorder, 0, 0, len(inorder) - 1)