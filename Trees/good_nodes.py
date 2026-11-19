class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_val):
            if not node: # if the node is None, return 0 since there are no good nodes in a non-existent subtree
                return 0

            count = 1 if node.val >= max_val else 0 # if the current node's value is greater than or equal to the maximum value seen so far, it is a good node, so we increment the count by 1
            max_val = max(max_val, node.val) # update the maximum value seen so far to be the maximum of the current node's value and the previous maximum value
            count += dfs(node.left, max_val) # recursively get the count of good nodes in the left subtree and add it to the current count
            count += dfs(node.right, max_val) # recursively get the count of good nodes in the right subtree and add it to the current count
            return count

        return dfs(root, root.val) # start the DFS traversal from the root node, passing in the root's value as the initial maximum value seen so far

