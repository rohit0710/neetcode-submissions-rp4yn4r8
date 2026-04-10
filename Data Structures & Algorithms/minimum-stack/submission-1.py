class MinStack:

    def __init__(self):
        self.stack = []
        self.min_v = float('inf')

    def push(self, val: int) -> None:
        if val <= self.min_v:
            self.stack.append(self.min_v)
            self.min_v = val
        self.stack.append(val)
        
    def pop(self) -> None:
        if self.stack.pop() == self.min_v:
            self.min_v = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.min_v