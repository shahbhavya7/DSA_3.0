from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class BinaryTree:
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
            
class SolutionBrute:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        current_height = left_height + right_height
        
        return max(current_height, left_diameter, right_diameter)
    
    def height(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        
        right_height = self.height(node.right)
        left_height = self.height(node.left)
        
        return max(left_height, right_height) + 1
    

class Solution:   
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameterOfBinaryTree = 0
        
        def height(node: Optional[TreeNode]) -> int: 
            # just calculate the current diameter inside the height function as height already has length of left and right subtree, 
            # so we can calculate the diameter at that node
            if node is None:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)
            
            self.diameterOfBinaryTree = max(self.diameterOfBinaryTree, left_height + right_height)
            
            return max(left_height, right_height) + 1
        height(root)
        
        return self.diameterOfBinaryTree