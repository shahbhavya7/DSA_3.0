from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        count = self.countNodes(head)
        if n > count:
            return head
        node_to_remove = count - n + 1 
        if node_to_remove == 1: # if we need to remove the head node then we just return the next node as the new head
            return head.next
        current = head
        current_position = 1
        while current_position < node_to_remove - 1: # we need to stop at the node before the node to remove
            current = current.next
            current_position += 1
        current.next = current.next.next
        return head
   
    def countNodes(self, head: Optional[ListNode]) -> int:
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count 

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
# remove the 2nd node from the end of the linked list
sol = Solution()
linked_list.head = sol.removeNthFromEnd(linked_list.head, 2)
# print the elements of the linked list after removing the node
linked_list.print_list()