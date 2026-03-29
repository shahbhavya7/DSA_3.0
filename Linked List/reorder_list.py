from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second_half = self.reverseList(slow.next) # seconf half has head of the reversed second half of the list
        slow.next = None # now as list is reversed slow's next will be the last node of the list so we need to set it to None
        first_half = head # first half has head of the first half of the list

        while second_half:
            temp1,temp2 = first_half.next, second_half.next # we need to store the next nodes of first half and second half before changing the next pointers
            first_half.next = second_half # we need to point the next of first half to the current node of second half
            second_half.next = temp1 # we need to point the next of current node of second half to the next node of first half
            first_half = temp1 # we need to move the first half pointer to the next node of first half
            second_half = temp2 # we need to move the second half pointer to the next node of second half
   
    def countNodes(self, head: Optional[ListNode]) -> int:
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count 
    
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
linked_list.append(4)
linked_list.append(5)
# print the elements of the linked list
linked_list.print_list()
# reorder the linked list
sol = Solution()
sol.reorderList(linked_list.head)
# print the elements of the reordered linked list
linked_list.print_list()