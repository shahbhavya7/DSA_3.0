from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = [[]]
        queue = deque([root])

        while queue:
            same_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                same_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(same_level)
        return result[1:]  # Exclude the first empty list

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

    print("\nLevel Order Traversal of the BST:") # output order :
    solution = Solution()
    level_order_result = solution.levelOrder(bst.root)
    for level in level_order_result:
        print(level)  # Output: [[5], [3, 8], [1, 4, 7, 9]]