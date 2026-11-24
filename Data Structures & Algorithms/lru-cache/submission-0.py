class Node:
    def __init__(self, key = 0, val = 0, prev = None, nxt = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = Node(), Node()
        self.head.nxt = self.tail
        self.tail.prev = self.head
    
    def remove_node(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev

    def insert_node(self, node):
        node.prev, node.nxt = self.tail.prev, self.tail
        self.tail.prev.nxt = node
        self.tail.prev = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove_node(node)
        self.insert_node(node)
        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert_node(self.cache[key])

        while len(self.cache) > self.capacity:
            evict = self.head.nxt
            self.remove_node(evict)
            del self.cache[evict.key]


