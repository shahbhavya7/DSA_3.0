from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 0)])  # Store nodes along with their index
        max_width = 0
        
        while queue:
            current_level_size = len(queue)
            start_index = queue[0][1]  # Index of the first node at the current level
            end_index = queue[-1][1]    # Index of the last node at the current level
            max_width = max(max_width, end_index - start_index + 1)
            
            for _ in range(current_level_size):
                current_node, index = queue.popleft()
                if current_node.left:
                    queue.append((current_node.left, 2 * index + 1))  # Left child index
                if current_node.right:
                    queue.append((current_node.right, 2 * index + 2))  # Right child index
            
        return max_width