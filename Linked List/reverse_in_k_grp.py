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
    def length(self, head: ListNode) -> int:
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1:
            return head
        
        length = self.length(head)
        cnt = length // k
        
        while cnt > 0:
            prev = None
            current = head
            next_node = None
            
            for _ in range(k): 
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            
            if head:
                head.next = current
            
            head = prev
            cnt -= 1
            
        return head
    
# create a linked list and append some elements to it
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)


# create an instance of the Solution class
solution = Solution()

# reverse the linked list in groups of k
k = 2

# reverse the linked list in groups of k
new_head = solution.reverseKGroup(linked_list.head, k)

# print the elements of the reversed linked list
current_node = new_head
while current_node:
    if current_node.next:
        print(current_node.val, end=' -> ')
    else:
        print(current_node.val)
    current_node = current_node.next
    
