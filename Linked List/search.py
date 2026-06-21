class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp_node = self.head
        while temp_node.next:
            temp_node = temp_node.next
        temp_node.next = new_node
    
    def print_list(self):
        temp_node = self.head
        while temp_node.next:
            print(temp_node.data, end=" -> ")
            temp_node = temp_node.next
        print(temp_node.data)

class Solution:
    def searchKey(self, head, key):
        temp = head
        while temp:
            if temp.data == key:
                return True
            temp  = temp.next
        return False


# driver code 
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.print_list()

s = Solution()
print(s.searchKey(ll.head, 4))
print(s.searchKey(ll.head, 10))