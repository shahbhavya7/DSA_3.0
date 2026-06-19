class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def insertAtFirst(list: Node, newValue: int) -> Node:
        nnode = Node(newValue)
        nnode.next = list
        return nnode
        
