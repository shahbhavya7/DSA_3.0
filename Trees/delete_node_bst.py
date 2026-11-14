class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    def findMin(self, node: TreeNode) -> TreeNode:
        while node and node.left: # we traverse the left in right subtree to find the minimum value in the right subtree, until we reach a node with no left child, which is the minimum value in the right subtree
            node = node.left
        return node
    
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key) # after recursive call returns the new left subtree, we assign it to root.left to update the tree structure
        elif key > root.val:
            root.right = self.deleteNode(root.right, key) # after recursive call returns the new right subtree, we assign it to root.right to update the tree structure
            
        else: # if key == root.val, we found the node to delete
            if not root.left: # we combine the cases where the node has no children or only a right child
                temp = root.right
                del root
                return temp
            elif not root.right: # if the node has only a left child or no children, we return the left child (or None if no children)
                temp = root.left
                del root
                return temp
            else: # if the node has two children, we find the minimum value in the right subtree to replace the node's value i.e. inorder sucessor
                InorderSuccessor = self.findMin(root.right)
                root.val = InorderSuccessor.val
                root.right = self.deleteNode(root.right, InorderSuccessor.val) # we delete the inorder successor from the right subtree
        
        return root
    
    