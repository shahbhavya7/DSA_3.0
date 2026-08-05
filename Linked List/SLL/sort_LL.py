from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        
    def print_list(self):
        current_node = self.head
        while current_node:
            if current_node.next:
                print(current_node.val, end=' -> ')
            else:
                print(current_node.val)
            current_node = current_node.next
            
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Split the list into two halves
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next   
            
        mid = slow.next
        slow.next = None  # Split the list into two halves

        
        # Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # Merge the sorted halves
        return self.merge(left, right)
    
    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)  # Dummy node to help with merging
        current = temp
        
        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
            
        if left:
            current.next = left
            
        if right:
            current.next = right
            
        return temp.next
    

# Example usage:
list = LinkedList()
list.append(4)
list.append(2)
list.append(1)
list.append(3)
list.print_list()  # Output: 4 -> 2 -> 1 -> 3

solution = Solution()
sorted_head = solution.sortList(list.head)

# Print the sorted linked list
current_node = sorted_head
while current_node:
    if current_node.next:
        print(current_node.val, end=' -> ')
    else:
        print(current_node.val)
    current_node = current_node.next
