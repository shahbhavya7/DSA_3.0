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
            
class SolutionBrute:

    def countNodes(self, head: Optional[ListNode]) -> int:
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count
    
    def deleteMiddleBrute(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None  # If the list is empty or has only one node, return None
        
        count = self.countNodes(head)
        # Find the position of the middle node (0 based index), for even number of nodes, we will delete the second middle node
        middle_position = count // 2
        
        current = head
        current_position = 0
        while current_position < middle_position - 1:  # Stop at the node before the middle node
            current = current.next
            current_position += 1
        current.next = current.next.next  # Remove the middle node by skipping it
        return head
    

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return None  # If the list is empty or has only one node, return None
        
        slow = head
        fast = head.next.next  # Start fast pointer two steps ahead as we want to delete the second middle node in case of even number of nodes
        # for odd nodes it handles it as well because slow will be at one node before the middle node when fast reaches the end of the list
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        slow.next = slow.next.next  # Remove the middle node by skipping it
        return head
        
        
# create a linked list and append some elements to it
linked_list = LinkedList()

linked_list.append(2)
linked_list.append(1)
# linked_list.append(3)
# linked_list.append(4)

# print the elements of the linked list
linked_list.print_list()

# create an instance of the Solution class
solution = Solution()

# delete the middle node
linked_list.head = solution.deleteMiddle(linked_list.head)

# print the elements of the linked list after deleting the middle node
linked_list.print_list()