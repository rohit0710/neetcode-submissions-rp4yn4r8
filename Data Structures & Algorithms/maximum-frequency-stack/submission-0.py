class FreqStack:

    def __init__(self):
        self.counter = defaultdict(int)
        self.stack = [[]]

    def push(self, val: int) -> None:
        self.counter[val] += 1
        if self.counter[val] == len(self.stack):
            self.stack.append([])
        self.stack[self.counter[val]].append(val)

    def pop(self) -> int:
        val = self.stack[-1].pop()
        self.counter[val] -= 1
        if not self.stack[-1]:
            del self.stack[-1]
        return val
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()