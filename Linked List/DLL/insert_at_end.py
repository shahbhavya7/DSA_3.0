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


class Solution:
    def insert_at_end(self, head, data):
        new_node = Node(data)

        if not head:
            return new_node

        temp_node = head
        while temp_node.next:
            temp_node = temp_node.next

        temp_node.next = new_node
        new_node.prev = temp_node

        return head

# Example usage
dll = Solution()
dll.head = dll.insert_at_end(dll.head, 10)
dll.head = dll.insert_at_end(dll.head, 20)
dll.head = dll.insert_at_end(dll.head, 30)

# Print the list forward
dll.print_forward()  # Output: 10 <-> 20 <-> 30

# Print the list backward
dll.print_backward()  # Output: 30 <-> 20 <-> 10