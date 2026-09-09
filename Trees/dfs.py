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
            self.inorder_traversal(node.left)
            print(node.val, end=' ')
            self.inorder_traversal(node.right)

class Solution:
    def dfs(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        print(f"Visiting node with value: {node.val}")  # Debug statement to trace the node being visited
        self.dfs(node.left)
        self.dfs(node.right)

# Example usage:
if __name__ == "__main__":
    bst = BST()
    values = [5, 3, 8, 1, 4, 7, 9] 
    # tree structure:
    #         5
    #        / \
    #       3   8
    #      / \  / \
    #     1  4 7   9
    for val in values:
        bst.insert(val)

    print("Inorder Traversal of the BST:") # output: 1 3 4 5 7 8 9
    bst.inorder_traversal(bst.root) 
    print("\nDFS Traversal of the BST:") # output order : 
    solution = Solution()
    solution.dfs(bst.root)
