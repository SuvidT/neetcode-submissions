class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []
        self.length = 0
        

    def push(self, val: int) -> None:
        self.stack.insert(0, val)
        self.length += 1
        if len(self.mins) == 0:
            self.mins.insert(0, (val, self.length))
        elif self.mins[0][0] > val:
            self.mins.insert(0, (val, self.length))

    def pop(self) -> None:
        if self.length == 0:
            return

        val = self.stack.pop(0)
        self.length -= 1

        if self.length < self.mins[0][1]:
            self.mins.pop(0)

    def top(self) -> int:
        return self.stack[0]
        

    def getMin(self) -> int:
        return self.mins[0][0]
        