class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def solve(self, node, ans):
        if not node:
            return 0

        left = max(0, self.solve(node.left, ans))
        right = max(0, self.solve(node.right, ans))
        ans = max(ans, left + right + node.val)
        return node.val + max(left, right)

    def maxPathSum(self, root: TreeNode | None) -> int:
        self.ans = float("-inf")
        self.solve(root)
        return self.ans
        
