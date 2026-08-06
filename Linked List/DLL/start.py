# We will implement a Doubly Linked List (DLL) in this file
# and print the elements of the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head: # If the list is empty, set the new node as the head
            self.head = new_node
            return

        temp_node = self.head
        while temp_node.next:
            temp_node = temp_node.next

        temp_node.next = new_node
        new_node.prev = temp_node

    def print_forward(self):
        current_node = self.head

        while current_node:
            if current_node.next:
                print(current_node.data, end=" <-> ")
            else:
                print(current_node.data)
            current_node = current_node.next

    def print_backward(self):
        if not self.head:
            return

        temp_node = self.head
        while temp_node.next:
            temp_node = temp_node.next

        while temp_node:
            if temp_node.prev:
                print(temp_node.data, end=" <-> ")
            else:
                print(temp_node.data)
            temp_node = temp_node.prev


# Example usage
dll = DoublyLinkedList()

dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

print("Forward:")
dll.print_forward()

print("Backward:")
dll.print_backward()