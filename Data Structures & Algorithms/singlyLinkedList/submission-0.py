class Node:
    def __init__(self, val: int, next: Node | None = None):
        self.val = val
        self.next = next

    def setNext(self, next: Node):
        self.next = next


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.len: int = 0

    def get(self, index: int) -> int:
        if index < 0:
            return -1
        elif index >= self.len:
            return -1

        curr = self.head
        if curr == None:
            raise ValueError(f"LinkedList.get(index): no list")
        i = 0
        while i < index:
            if curr.next != None:
                curr = curr.next

        return curr.val

    def insertHead(self, val: int) -> None:
        new_node = Node(val, self.head)
        self.head = new_node

        if self.tail == None:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if self.tail != None:
            self.tail.next = new_node
        self.tail = new_node

        if self.head == None:
            self.head = new_node

    def remove(self, val: int) -> bool:
        if self.head == None:
            raise ValueError(f"LinkedList.remove(val): head is empty")
        elif self.tail == None:
            raise ValueError(f"LinkedList.remove(val): tail is empty")

        if self.head.val == val:
            self.head = self.head.next
            self.len -= 1
            return True

        curr = self.head
        while curr.next != None and curr.next.val != val:
            curr = curr.next

        if curr.next != None:
            if curr.next.val == val:
                curr.next = curr.next.next
                self.len -= 1
                return True
        return False

    def getValues(self) -> list[int]:
        if self.head == None:
            raise ValueError(f"LinkedList.remove(val): head is empty")
        elif self.tail == None:
            raise ValueError(f"LinkedList.remove(val): tail is empty")

        new_list = []

        curr = self.head
        while curr != None:
            new_list.append(curr.val)
            curr = curr.next

        return new_list


if __name__ == "__main__":
    arr = LinkedList()

    print(arr.insertHead(1))
    print(arr.getValues())

    print(arr.insertHead(2))
    print(arr.getValues())

    print(arr.get(5))
    print(arr.getValues())
