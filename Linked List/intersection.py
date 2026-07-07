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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d1,d2 = headA, headB

        while d1 != d2:
            if d1:
                d1 = d1.next
            else:
                d1 = headB
            if d2:
                d2 = d2.next
            else:
                d2 = headA
        return d1
    
# if the two do not intersect, both d1 and d2 will eventually become None, and the loop will terminate, returning None. 
# If they do intersect, d1 and d2 will eventually point to the same node, which is the intersection node.


# Example usage:
ll1 = LinkedList()
ll1.append(4)
ll1.append(1)
ll1.append(8)
ll1.append(4)
ll1.append(5)

ll2 = LinkedList()
ll2.append(5)
ll2.append(6)
ll2.append(1)
ll2.append(8)
ll2.append(4)
ll2.append(5)

# Creating intersection
# Let's say the intersection starts at node with value 8 in ll1
intersection_node = ll1.head.next.next  # Node with value 8
ll2.head.next.next.next = intersection_node  # Linking ll2 to the intersection node

solution = Solution()
intersection = solution.getIntersectionNode(ll1.head, ll2.head)
if intersection:
    print(f"Intersection at node with value: {intersection.val}")  # Output: Intersection at node with value: 8
elif intersection is None:
    print("No intersection found.")

