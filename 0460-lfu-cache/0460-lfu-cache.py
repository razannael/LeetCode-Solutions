class Node:
    def __init__(self, key=None, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next
        

class LRU:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, key) -> Node:
        prev_head = self.head.next
        new_head = Node(key, self.head, prev_head)
        self.head.next = new_head
        prev_head.prev = new_head
        return new_head

    def remove(self, node: Node):
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_val = dict()
        self.key_to_node = dict()
        self.key_to_freq = dict()
        self.freq_to_lru = defaultdict(LRU)
        self.min_freq = inf

    def remove_from_lru(self, old_freq, key):
        prev_lru = self.freq_to_lru[old_freq]
        node = self.key_to_node[key]
        prev_lru.remove(node)
        del self.key_to_node[key]


    def add_to_lru(self, new_freq, key):
        lru = self.freq_to_lru[new_freq]
        new_node = lru.add(key)
        self.key_to_node[key] = new_node
    
        
    def increase_freq(self, key):
        old_freq = self.key_to_freq[key]
        new_freq = old_freq + 1

        self.remove_from_lru(old_freq, key)
        self.add_to_lru(new_freq, key)
        new_lru = self.freq_to_lru[new_freq]

        self.key_to_freq[key] = new_freq
        if old_freq == self.min_freq:
            old_lru = self.freq_to_lru[old_freq]
            if old_lru.head.next == old_lru.tail:
                self.min_freq = new_freq

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1

        self.increase_freq(key)
        return self.key_to_val[key]

    def remove_oldest(self):
        lru = self.freq_to_lru[self.min_freq]
        oldest = lru.tail.prev
        lru.remove(oldest)

        key = oldest.key
        del self.key_to_val[key]
        del self.key_to_node[key]
        del self.key_to_freq[key]

    def init_freq(self, key):
        self.key_to_freq[key] = 1
        self.min_freq = 1
        self.add_to_lru(1, key)


    def put(self, key: int, value: int) -> None:
        if key in self.key_to_val:
            self.key_to_val[key] = value
            self.increase_freq(key)
            return
        else:
            self.capacity -= 1

            if self.capacity < 0:
                self.remove_oldest()
            
            self.key_to_val[key] = value
            self.key_to_node[key] = None
            self.init_freq(key)
    