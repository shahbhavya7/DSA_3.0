class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next

class Solution:

    def reverse(self, head):
        prev = None
        current = head
        while current:
            nnode = current.next
            current.next = prev
            prev = current
            current = nnode

        return prev

    def addOne(self,head):
        head = self.reverse(head)
        current = head
        last = None # initially, last will be None, it will keep track of the last node processed
        carry = 1

        while current:
            sum_val = current.data + carry
            carry = 1 if sum_val >= 10 else 0
            current.data = sum_val % 10

            last = current
            current = current.next
        
        if carry > 0:
            last.next = Node(carry)

        return self.reverse(head)
    
# Example usage:
ll = LinkedList()

ll.push(9)
ll.push(9)
ll.push(9)

solution = Solution()
ll.head = solution.addOne(ll.head)
ll.printList()  # Output: 1 0 0 0




        