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
    def rotateRightBrute(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        previous = None
        current = head
        
        # reach the end of the list
        while current and current.next:
            previous = current
            current = current.next
        
        for _ in range(k):
            if not previous:
                return head  # If the list is empty or has only one node, no rotation needed
            
            # Move the last node to the front
            previous.next = None  # Detach the last node
            current.next = head   # Point the last node to the current head
            head = current        # Update head to the last node
            
            # Reset previous and current for the next iteration
            previous = None
            current = head
            while current and current.next:
                previous = current
                current = current.next
        return head
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        previous = None
        current = head
        
        # reach the end of the list
        while current and current.next:
            previous = current
            current = current.next
            
        # If the list is empty or has only one node, no rotation needed
        if not previous:
            return head
        
        for _ in range(k):
            
            temp = None
            current.next = head
            previous.next = None
            head = current
            
            
                
# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    for i in range(1, 6):  # Create a linked list with values 1 to 5
        ll.append(i)
    
    print("Original list:")
    ll.print_list()
    
    k = 2
    solution = Solution()
    new_head = solution.rotateRight(ll.head, k)
    
    print(f"List after rotating right by {k} positions:")
    current = new_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")