class Node:
    def __init__(self, key: int, value: int):
        self.key, self.value = key, value
        self.previous = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # Initialize with capacity size
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.previous = self.right, self.left
    
    def add(self, node):
        prev, nxt = self.right.previous, self.right
        node.previous, prev.next = prev, node
        node.next, nxt.previous = nxt, node 

    def remove(self, node):
        prev, nxt = node.previous, node.next
        prev.next, nxt.previous = nxt, prev
        

    def get(self, key: int) -> int:
        # Return Value w/ Key
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].value
        return -1
        # return -1 otherwise 
        

    def put(self, key: int, value: int) -> None:
        # Update/add key value to cache
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])

        # Remove LRU key if exceeds capacity
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
