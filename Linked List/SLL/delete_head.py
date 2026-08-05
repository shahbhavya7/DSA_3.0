class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        nnode = ListNode(val)
        if not self.head:
            self.head = nnode
            return
        temp_node = self.head
        while temp_node.next:
            temp_node = temp_node.next
        temp_node.next = nnode

    def print_list(self):
        temp_node = self.head
        while temp_node.next:
            print(temp_node.val, end=" -> ")
            temp_node = temp_node.next
        print(temp_node.val)

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
        
# driver code 
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()

s = Solution()
s.deleteNode(ll.head) # deletes the head node
ll.print_list()
