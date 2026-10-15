class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    prevOrder = 0
    
    def kthSmallest(self, root: TreeNode | None, k: int) -> int: # inorder traversal of BST gives sorted order of elements
        if not root:
            return None
        
        if root.left:
            left = self.kthSmallest(root.left, k) # left has smaller elements than root, so we traverse left first
            if left is not None: # 
                return left
        
        if self.prevOrder + 1 == k:
            return root.val

        self.prevOrder += 1
        
        if root.right:
            right = self.kthSmallest(root.right, k)
            if right is not None:
                return right
            

        
        