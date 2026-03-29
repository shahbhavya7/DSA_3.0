# we will implement a linked list in this file and print the elements of the linked list
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
        current_node = self.head
        while current_node:
            if current_node.next:
                print(current_node.data, end=' -> ')
            else:
                print(current_node.data)
            current_node = current_node.next

# create a linked list and append some elements to it
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
# print the elements of the linked list
linked_list.print_list()