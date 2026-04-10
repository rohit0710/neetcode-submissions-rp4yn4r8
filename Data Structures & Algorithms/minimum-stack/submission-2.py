class MinStack:

    def __init__(self):
        self.stack = []
        self.minV = float('inf')

    def push(self, val: int) -> None:
        if val <= self.minV:
            self.stack.append(self.minV)
            self.minV = val
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.minV:
            self.minV = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minV
        
