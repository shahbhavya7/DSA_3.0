
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
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self): 
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

class Solution:
    def lengthOfLoop(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
            if slow == fast:
                loop_length = 1
                current = slow
                while current.next != slow:
                    loop_length += 1
                    current = current.next
                return loop_length
            
        return 0

if __name__ == "__main__":
    # create a linked list and append some elements to it
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    
    # create a cycle in the linked list for testing
    linked_list.head.next.next.next.next = linked_list.head.next  # creating a cycle
    
    solution = Solution()
    loop_length = solution.lengthOfLoop(linked_list.head)
    
    print("Length of the loop in the linked list:", loop_length)  # Output: 3
        