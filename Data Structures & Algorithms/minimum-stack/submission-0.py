class MinStack:

    def __init__(self):
        self.mainStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if len(self.mainStack) == 0:
            self.mainStack.insert(0, val)
            self.minStack.insert(0, val)
        else:
            self.mainStack.insert(0, val)
            if val < self.minStack[0]:
                self.minStack.insert(0, val)
            else:
                self.minStack.insert(0, self.minStack[0])

    def pop(self) -> None:
        if len(self.mainStack) == 0:
            pass
        else:
            self.mainStack.pop(0)
            self.minStack.pop(0)

    def top(self) -> int:
        if len(self.mainStack) == 0:
            return None
        else:
            return self.mainStack[0]

    def getMin(self) -> int:
        if len(self.minStack) == 0:
            return None
        else:
            return self.minStack[0]