class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def isMirror(self, left: TreeNode | None, right: TreeNode | None) -> bool:
        if not left and not right: # both left and right are None, so they are symmetric
            return True
        if not left or not right: # one of them is None, so they are not symmetric
            return False
        if left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left):
            return True

    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)