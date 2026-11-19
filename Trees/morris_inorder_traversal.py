class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        curr = root
        while curr:
            if not curr.left:
                res.append(curr.val)
                curr = curr.right
            else:
                IP = curr.left
                while IP.right and IP.right != curr:
                    IP = IP.right
                if not IP.right: # create a temp thread to the current node to traverse back after finishing the left subtree
                    IP.right = curr
                    curr = curr.left
                else: # remove the temp thread and traverse back to the current node after finishing the left subtree
                    IP.right = None
                    res.append(curr.val)
                    curr = curr.right

        return res