class MinStack:

    def __init__(self):
        self.stack = []
        self.extraStack = [] # stack with prefix min attached afterwards
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        minimum = val
        if self.extraStack:
            minimum = min(self.extraStack[-1], val)

        self.extraStack.append(val)
        self.extraStack.append(minimum)

    def pop(self) -> None:
        
        self.stack.pop()

        self.extraStack.pop()
        self.extraStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.extraStack[-1]
        
