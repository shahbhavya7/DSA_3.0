from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)  # Dummy node to help with the addition
        current = temp

        carry = 0

        while l1 or l2 or carry:

            sum_val = 0

            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            sum_val += carry

            carry = sum_val // 10
            node = ListNode(sum_val % 10)
            current.next = node
            current = current.next

        return temp.next
    

# Example usage:
ll1 = LinkedList()
ll1.append(2)
ll1.append(4)
ll1.append(3)

ll2 = LinkedList()
ll2.append(5)
ll2.append(6)
ll2.append(4)

solution = Solution()
result = solution.addTwoNumbers(ll1.head, ll2.head)
# Print the result
current_node = result
while current_node:
    if current_node.next:
        print(current_node.val, end=' -> ')
    else:
        print(current_node.val)
    current_node = current_node.next

