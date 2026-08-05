from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool: 
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
            return
        temp_node = self.head
        while temp_node.next:
            temp_node = temp_node.next
        temp_node.next = new_node
    
# create a linked list and append some elements to it
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
# create a cycle in the linked list
linked_list.head.next.next.next = linked_list.head
# check if the linked list has a cycle
sol = Solution()
print(sol.hasCycle(linked_list.head))