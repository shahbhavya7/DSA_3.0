from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        # Dummy node helps handle edge cases (e.g., when left = 1)
        dummy = ListNode(0)
        dummy.next = head
        node_before_sublist = dummy
        
        # 1. Move `node_before_sublist` to the node right before the `left` position
        for _ in range(left - 1):
            node_before_sublist = node_before_sublist.next
            
        # 2. Reverse the sublist between `left` and `right`
        # `current` begins at `left`
        current = node_before_sublist.next
        prev = None
        
        for _ in range(right - left + 1):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        # 3. Reconnect the reversed sublist back to the main list
        # `node_before_sublist.next` currently points to the original start of the sublist, 
        # which is now the end of the reversed sublist. It should point to `current` (node after `right`)
        node_before_sublist.next.next = current
        
        # Connect the node before the sublist to the new start of the reversed sublist (`prev`)
        node_before_sublist.next = prev
        
        return dummy.next
    
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
linked_list.append(4)
linked_list.append(5)
# print the elements of the linked list
linked_list.print_list()
# reverse the linked list between position 2 and 4
sol = Solution()
linked_list.head = sol.reverseBetween(linked_list.head, 2, 4)
# print the elements of the reversed linked list
linked_list.print_list()    
