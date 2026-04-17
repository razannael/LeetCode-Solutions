class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        
        self.cap = capacity
        self.cache = {}

        self.right = Node(0,0)
        self.left = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]