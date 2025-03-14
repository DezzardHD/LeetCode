class ListNode:
    
    def __init__(self, val = 0, key = 0, prev = None, next = None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.start = ListNode(-1)
        self.end = ListNode(-2)
        self.start.next = self.end # next of start holds RU
        self.end.prev = self.start # prev of end holds LRU

    def remove(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node: ListNode):
        node.prev = self.start
        node.next = self.start.next
        self.start.next = node
        node.next.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = self.cache[key] if key in self.cache else ListNode(value, key)
        self.cache[key].val = value
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            tbr = self.cache.pop(self.end.prev.key)
            self.remove(self.end.prev)
            tbr = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)