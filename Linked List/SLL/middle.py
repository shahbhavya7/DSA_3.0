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
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    for i in range(1, 6):  # Create a linked list with values 1 to 5
        linked_list.append(i)
    
    linked_list.print_list()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None
    
    solution = Solution()
    middle_node = solution.middleNode(linked_list.head)
    
    if middle_node:
        print(f"The middle node value is: {middle_node.val}")  # Output: The middle node value is: 3
    else:
        print("The linked list is empty.")