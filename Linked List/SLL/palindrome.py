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
            
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        # Find the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Reverse the second half of the linked list
        prev = None
        while slow:
            nnode = slow.next
            slow.next = prev
            prev = slow
            slow = nnode
            
        # Compare the first half and the reversed second half
        left = head
        right = prev
        
        while right:  # Only need to compare until the end of the reversed half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True
    
if __name__ == "__main__":
    # create a linked list and append some elements to it
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(2)
    linked_list.append(1)
    
    solution = Solution()
    is_palindrome = solution.isPalindrome(linked_list.head)
    
    print("Is the linked list a palindrome?", is_palindrome)  # Output: True