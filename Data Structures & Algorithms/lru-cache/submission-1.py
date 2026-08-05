class ListNode:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def add_to_ll(self, node):
        node.next = self.start.next 
        node.prev = self.start
        self.start.next.prev = node
        self.start.next = node

    def remove_from_ll(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def __init__(self, capacity: int):
        self.start = ListNode()
        self.end = ListNode()
        self.start.next = self.end
        self.end.prev = self.start
        self.cap = capacity
        self.map = dict()

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.remove_from_ll(node)
        self.add_to_ll(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self.remove_from_ll(node)
        node = ListNode(key, value)
        self.add_to_ll(node)
        self.map[key] = node
        if len(self.map) > self.cap:
            last_node = self.end.prev
            self.remove_from_ll(last_node)
            del self.map[last_node.key]


