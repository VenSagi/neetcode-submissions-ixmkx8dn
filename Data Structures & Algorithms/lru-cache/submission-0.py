class Node:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.cache = {}

        self.left.next = self.right
        self.right.prev = self.left
        
    def add(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
