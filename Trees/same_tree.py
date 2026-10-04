class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True
        
        if p and q and p.val == q.val: 
            # if both nodes are not None and have the same value, check their children else return False as they are not the same tree
            # in every rec call we check if roots of the child trees are the same and then check their children recursively
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return False
    