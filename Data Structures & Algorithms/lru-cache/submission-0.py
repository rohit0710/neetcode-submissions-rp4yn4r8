
class DoublyLinkedList:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_value = dict()
        self.start = DoublyLinkedList()
        self.end = DoublyLinkedList()
        self.start.next = self.end
        self.end.prev = self.start

    def add_to_ll(self, head):
        temp = self.start.next
        head.prev = self.start
        head.next = temp
        temp.prev = head
        self.start.next = head

    def delete_from_ll(self, head):
        head.prev.next = head.next
        head.next.prev = head.prev

    def get(self, key: int) -> int:
        if key in self.key_value:
            head = self.key_value[key]
            self.delete_from_ll(head)
            self.add_to_ll(head)
            return head.val
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.key_value:
            self.delete_from_ll(self.key_value[key])
        head = DoublyLinkedList(key = key, val=value)
        self.key_value[key] = head
        self.add_to_ll(head)
        if len(self.key_value) > self.capacity:
            evicted = self.end.prev
            del self.key_value[evicted.key]
            self.delete_from_ll(evicted)