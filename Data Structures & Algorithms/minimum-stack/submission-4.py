class MinStack:

    def __init__(self):
        self.stack = []
        self.minv = float('inf')

    def push(self, val: int) -> None:
        if self.minv >= val:
            self.stack.append(self.minv)
            self.minv = val
        self.stack.append(val)

    def pop(self) -> None:
        if self.minv == self.stack.pop():
            self.minv = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minv
