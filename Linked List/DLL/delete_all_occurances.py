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
    def delete_target_nodes(self, head, target):
        curr = head
        while curr:
            if curr.data == target:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    head = curr.next  # Update head if the first node is deleted
                if curr.next:
                    curr.next.prev = curr.prev
            curr = curr.next
        return head


# Example usage
dll = Solution()
# Create a doubly linked list with some nodes
dll.head = Node(1)
dll.head.next = Node(2)
dll.head.next.prev = dll.head
dll.head.next.next = Node(3)
dll.head.next.next.prev = dll.head.next

# Print the original list
print("Original list:")
current_node = dll.head
while current_node:
    if current_node.next:
        print(current_node.data, end=" <-> ")
    else:
        print(current_node.data)
    current_node = current_node.next

# Delete nodes with target value 2
dll.head = dll.delete_target_nodes(dll.head, 2)

# Print the modified list
print("Modified list after deleting target nodes:")
current_node = dll.head
while current_node:
    if current_node.next:
        print(current_node.data, end=" <-> ")
    else:
        print(current_node.data)
    current_node = current_node.next

    