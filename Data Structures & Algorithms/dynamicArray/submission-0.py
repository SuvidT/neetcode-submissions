class DynamicArray:
    def __init__(self, capacity: int):
        self.arr: list[int | None] = [None for _ in range(capacity)]
        self.len = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
        if i < 0:
            raise ValueError(f"DynamicArray.get(i): index {i} too low")
        elif i >= self.len:
            raise ValueError(f"DynamicArray.get(i): index {i} too high")

        val = self.arr[i]
        if val:
            return val
        else:
            raise ValueError(f"DynamicArray.get(i): no value at {i}")

    def set(self, i: int, n: int) -> None:
        if i < 0:
            raise ValueError(f"DynamicArray.set(i): index {i} too low")
        elif i >= self.len:
            raise ValueError(f"DynamicArray.set(i): index {i} too high")

        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.len == self.capacity:
            self.resize()

        self.arr[self.len] = n
        self.len += 1

    def popback(self) -> int:
        if self.len == 0:
            raise ValueError(f"DynamicArray.popback(): no value left to pop")

        val = self.arr[self.len - 1]

        self.arr[self.len - 1] = None

        self.len -= 1

        if val:
            return val
        else:
            raise ValueError(f"DynamicArray.popback(): no value left to pop")

    def resize(self) -> None:
        new_list: list[int | None] = [None for _ in range(self.capacity * 2)]
        for i, num in enumerate(self.arr):
            new_list[i] = num
        self.arr = new_list
        self.capacity = len(self.arr)

    def getSize(self) -> int:
        return self.len

    def getCapacity(self) -> int:
        return self.capacity
