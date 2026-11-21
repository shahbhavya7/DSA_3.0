from typing import Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        
        if node.right:
            successor = node.right
            while successor.left:
                successor = successor.left
            return successor
        
        else:
            successor = node.parent
            while successor and node == successor.right: # till we reach the root or find a node that is the left child of its parent, we keep moving up the tree
                node = successor
                successor = successor.parent
            return successor
        