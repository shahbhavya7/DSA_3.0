from typing import List, Optional

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        temp_node = self.head
        while temp_node.next:
            temp_node = temp_node.next
        temp_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            if current_node.next:
                print(current_node.val, end=' -> ')
            else:
                print(current_node.val)
            current_node = current_node.next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None 
        current_node = head
        q_node = None
        while current_node and current_node.next:
            if current_node.val == current_node.next.val:
                q = current_node.next
                current_node.next = q.next
                q.next = None
                del q
            else:
                current_node = current_node.next
        return head
    
# Example usage:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(3)
print("Original list:")
linked_list.print_list()
solution = Solution()
solution.deleteDuplicates(linked_list.head)
print("List after removing duplicates:")
linked_list.print_list()