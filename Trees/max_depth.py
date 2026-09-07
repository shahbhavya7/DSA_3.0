from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert(node.left, val)
        elif val > node.val:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert(node.right, val)

    def inorder_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.val, end=' ')
            self.in_order_traversal(node.right)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        if root is None:
            return count

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        