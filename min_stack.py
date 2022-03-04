class MinStack:

    def __init__(self):
        self.memory = []
        self.min = []

    def push(self, val: int) -> None:
        self.memory.append(val)
        self.min.append(val if len(self.min) == 0 or val < self.min[-1] else self.min[-1])

    def pop(self) -> None:
        self.min.pop()
        return self.memory.pop()

        
    def top(self) -> int:
        return self.memory[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()