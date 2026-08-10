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

class Solution(DoublyLinkedList):
    def removeDuplicates(self):
        if not self.head:
            return None

        current = self.head

        while current and current.next:
            nxt_distinct = current.next
            while nxt_distinct and nxt_distinct.data == current.data: # move nxt_distinct to the next distinct node
                nxt_distinct = nxt_distinct.next

            current.next = nxt_distinct # link current node to the next distinct node
            if nxt_distinct: # if nxt_distinct is not None, set its prev to current
                nxt_distinct.prev = current

            current = nxt_distinct
        return self.head

# Example usage
dll = Solution()
# Create a doubly linked list with some nodes
dll.head = Node(1)
dll.head.next = Node(2)
dll.head.next.prev = dll.head
dll.head.next.next = Node(2)
dll.head.next.next.prev = dll.head.next
dll.head.next.next.next = Node(3)
dll.head.next.next.next.prev = dll.head.next.next

# Print the original list
print("Original list:")
dll.print_forward()  # Output: 1 <-> 2 <-> 2 <-> 3

# Remove duplicates
dll.removeDuplicates()
# Print the modified list
print("List after removing duplicates:")
dll.print_forward()  # Output: 1 <-> 2 <-> 3

