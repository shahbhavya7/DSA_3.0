from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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
    
if __name__ == "__main__":
    # create a linked list and append some elements to it
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    
    # create a cycle in the linked list for testing
    linked_list.head.next.next.next.next = linked_list.head.next  # creating a cycle
    
    solution = Solution()
    has_cycle = solution.hasCycle(linked_list.head)
    
    print("Does the linked list have a cycle?", has_cycle)  # Output: True