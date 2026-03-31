from typing import List, Optional

class ListNode:
    def __init__(self, data):
        self.val = data
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None 
        while len(lists) > 1: # loop until we have only one list left
            temp = []
            for i in range(0, len(lists), 2): # 0 to len(lists) with step of 2 means we take two lists at a time, specifying step helps us to avoid index out of range error
                list1 = lists[i]
                list2  = lists[i + 1] if (i + 1) < len(lists) else None # python allows to check conditions for list in one line
                temp.append(self.mergeTwoLists(list1, list2)) # merge two lists and append the merged list to temp
            lists = temp # this will update the lists with the merged lists, we will repeat this process after every iteration of the while loop until we have only one list left which will be our final merged list
        return lists[0] # return the merged list
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy  = ListNode(0) 
        cur = dummy 
        
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
    
# create two linked lists and append some elements to them
linked_list1 = LinkedList()
linked_list1.append(1)
linked_list1.append(4)
linked_list1.append(5)
linked_list2 = LinkedList()
linked_list2.append(1)
linked_list2.append(3)
linked_list2.append(4)
linked_list3 = LinkedList()
linked_list3.append(2)
linked_list3.append(6)
# merge the three linked lists
solution = Solution()
merged_head = solution.mergeKLists([linked_list1.head, linked_list2.head, linked_list3.head])
# print the merged linked list
merged_list = LinkedList()
merged_list.head = merged_head
merged_list.print_list()

# like we have list = [L1,L2,L3,L4], first we will merge L1 L2 to get M1, store M1 in temp, then we will merge L3 L4 to get M2, store M2 in temp, 
# now we have temp = [M1,M2], now for ends temp is updated to list = [M1,M2], now while loop will run again, we will merge M1 M2 to get M3, store M3 in temp, 
# now we have temp = [M3], now for ends temp is updated to list = [M3], now while loop will run again, but this time it will not run because we have only one 
# list left in the list which is our final merged list M3, so we will return M3 as the final merged list.
# in list = [L1,L2,L3,L4], during for with help of step we take L1 L2 then loop pointer i directly jumps to L3 and we take L3,L4