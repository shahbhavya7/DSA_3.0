from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy  = ListNode(0) # dummy ptr to keep track of the head of the merged list
        cur = dummy # cur ptr to keep track of the current node in the merged list
        
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2
        return dummy.next

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
            
# create two linked lists and append some elements to them
linked_list1 = LinkedList()
linked_list1.append(1)
linked_list1.append(2)
linked_list1.append(4)
linked_list2 = LinkedList()
linked_list2.append(1)
linked_list2.append(3)
linked_list2.append(4)
# merge the two linked lists
sol = Solution()
merged_head = sol.mergeTwoLists(linked_list1.head, linked_list2.head)
# print the elements of the merged linked list
current_node = merged_head
while current_node:
    if current_node.next:
        print(current_node.val, end=' -> ')
    else:
        print(current_node.val)
    current_node = current_node.next