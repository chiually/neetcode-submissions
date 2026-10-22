class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:

        if self.stack:
            minimum = min(self.stack[-1], val)
        else:
            minimum = val

        self.stack.append(val)
        self.stack.append(minimum)
        

    def pop(self) -> None:
        self.stack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-2]
    

    def getMin(self) -> int:
        return self.stack[-1]
        
