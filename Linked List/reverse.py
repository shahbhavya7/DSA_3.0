from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current  = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current  = next_node
        return prev 

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
        
    def print_list(self):
        current_node = self.head
        while current_node:
            if current_node.next:
                print(current_node.val, end=' -> ')
            else:
                print(current_node.val)
            current_node = current_node.next

# create a linked list and append some elements to it
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
# print the elements of the linked list
linked_list.print_list()
# reverse the linked list
sol = Solution()
linked_list.head = sol.reverseList(linked_list.head)
# print the elements of the reversed linked list
linked_list.print_list()