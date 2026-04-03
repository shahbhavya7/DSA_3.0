class LRUCache:
    class Node: # class inside class to represent each node in the doubly linked list
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None
            
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = self.Node(-1, -1) # dummy head
        self.tail = self.Node(-1, -1) # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {} # hashmap to store key and node reference
        
    def _add_node(self, node):
        temp = self.head.next
        node.next = temp # this will be the new first node, so its next will be the old first node
        temp.prev = node # old first node's prev will be the new node
        self.head.next = node # head's next will be the new node
        node.prev = self.head # new node's prev will be head
    
    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node # bypass the node to be removed
        next_node.prev = prev_node # bypass the node to be removed
        
    def get(self, key: int) -> int:
        if key in self.cache:
            resNode = self.cache[key] # get the node reference from the hashmap
            ans = resNode.value # get the value to return
            del self.cache[key] # remove the key from hashmap as we will re-add it to the front, key and node both are deleted and re-added to mark it as most recently used
            self._remove_node(resNode) # remove the node from its current position
            self._add_node(resNode) # add the node to the front (most recently used
            self.cache[key] = resNode # re-add the key and node reference to the hashmap
            return ans
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            curr = self.cache[key] # get the node reference from the hashmap
            del self.cache[key] # remove the key from hashmap as we will re-add it to the front
            self._remove_node(curr) # remove the node from its current position
        
        if len(self.cache) == self.capacity: # if cache is full, remove the least recently used node (node before tail)
            del self.cache[self.tail.prev.key] # remove the key of the least recently used node from hashmap
            self._remove_node(self.tail.prev) # remove the least recently used node from the linked

        self._add_node(self.Node(key, value)) # add the new node to the front (most recently used)
        self.cache[key] = self.head.next # add the key and node reference i.e head.next (new node) to the hashmap
        
# after adding nodes tail reaches end of linkedlist and as tail is dummy node, tail.prev will be the least recently used node which we can remove when cache 
# is full. When we get a key, we remove the node from its current position and add it to the front to mark it as most recently used.

# Example usage
lru_cache = LRUCache(2)
lru_cache.put(1, 1) # cache is {1=1}
lru_cache.put(2, 2) # cache is {1=1, 2=2}
print(lru_cache.get(1)) # returns 1, cache is {2=2, 1=1}
lru_cache.put(3, 3) # evicts key 2, cache is {1=1, 3=3}
print(lru_cache.get(2)) # returns -1 (not found)
lru_cache.put(4, 4) # evicts key 1, cache is {3=3, 4=4}
print(lru_cache.get(1)) # returns -1 (not found)    
print(lru_cache.get(3)) # returns 3, cache is {4=4, 3=3}
print(lru_cache.get(4)) # returns 4, cache is {3=3, 4=4}

            
        
        
        
        