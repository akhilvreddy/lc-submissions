class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            self.min = min(val, self.min)

        
    def pop(self) -> None:
        old = self.stack.pop()
        if old < 0:
            self.min -= old
        

    def top(self) -> int:
        return self.stack[-1] + self.min if self.stack[-1] > 0 else self.min
        

    def getMin(self) -> int:
        return self.min
        
