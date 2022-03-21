class MinStack:

    def __init__(self):
        self.minStack  = []

    def push(self, val: int) -> None:
        self.minStack.append(val)

    def pop(self) -> None:
        self.minStack.pop()

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        return min(self.minStack)
