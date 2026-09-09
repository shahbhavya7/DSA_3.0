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
        if root is None: # this is the base case, if the root is None i.e we have reached end of branch, we return 0 as the maximum depth
            # and then going back up the recursion stack, we will add 1 for each node we encounter, which will give us the maximum depth of the tree
            return 0 # if the root is None, return 0 as the maximum depth

        left_depth = self.maxDepth(root.left) # left depth stores has the maximum depth of the left subtree
        right_depth = self.maxDepth(root.right) # right depth stores has the maximum depth of the right subtree

        return max(left_depth, right_depth) + 1 # return the maximum depth of the left and right subtree + 1 for the current node while going back up the recursion stack

        