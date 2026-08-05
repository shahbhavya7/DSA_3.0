class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Solution:
    def arrayToList(self, arr):
        if not arr:
            return None
        head = Node(arr[0])
        current_node = head
        n = len(arr)
        for data in range(1,n):
            current_node.next = Node(arr[data])
            current_node = current_node.next
        return head
    
# Example
arr = [1,2,3,4,5]
head = Solution().arrayToList(arr)
print(head)

