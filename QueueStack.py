class MyQueue:
    
    def __init__(self):
        self.Stack = []

    def push(self, x: int) -> None:
        return self.Stack.append(x) 
    def pop(self) -> int:
        print(self.Stack)
        x = self.Stack[0]
        print(self.Stack)
        self.Stack = self.Stack[1:]
        print(self.Stack)
        return x

    def peek(self) -> int:
        return self.Stack[0]

    def empty(self) -> bool:
        if len(self.Stack) == 0:
            return True
        else:
            return False
