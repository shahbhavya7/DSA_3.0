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
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while count < k: # check if there are at least k nodes left in the linked list, if not, return the head as is, no need to reverse the remaining nodes 
            if not temp:
                return head
            temp = temp.next
            count += 1
            
        new_head = self.reverseKGroup(temp, k) # reverse the next k nodes recursively and get the new head of the reversed list
        
        temp = head
        count = 0
        while count < k: # reverse the current k nodes
            next_node = temp.next
            temp.next = new_head
            new_head = temp # move the new head to the current node as for next iteration, the current node will become the new head of the reversed list
            # and so on until we reach the end of the k nodes
            temp = next_node # next current node is old current node's next node which is stored in next_node so it can preserved 
            count += 1
            
        return new_head # return the new head of the reversed list

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
    
