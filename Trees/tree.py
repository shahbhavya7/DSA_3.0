class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorder(self, root: TreeNode) -> None:
        if root is None:
            return

        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root: TreeNode) -> None:
        if root is None:
            return

        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)

    def postorder(self, root: TreeNode) -> None:
        if root is None:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val)

# Example usage:
if __name__ == "__main__":
    # Constructing a binary tree:
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()
    
    print("Preorder Traversal:")
    solution.preorder(root)

    print("\nInorder Traversal:")
    solution.inorder(root)

    print("\nPostorder Traversal:")
    solution.postorder(root)