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
            i += 1

        return curr.val

    def insertHead(self, val: int) -> None:
        new_node = Node(val, self.head)
        self.head = new_node

        if self.tail == None:
            self.tail = new_node

        self.len += 1

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if self.tail != None:
            self.tail.next = new_node
        self.tail = new_node

        if self.head == None:
            self.head = new_node

        self.len += 1

    def remove(self, index: int) -> bool:
        if (index < 0) or (index >= self.len):
            return False

        if self.head == None:
            return False

        if index == 0:
            self.head = self.head.next
            self.len -= 1
            return True

        curr = self.head
        i = 0
        while i < (index - 1):
            curr = curr.next
            i += 1

        curr.next = curr.next.next
        if index == (self.len - 1):
            self.tail = curr
        self.len -= 1

        return True

    def getValues(self) -> list[int]:
        new_list = []

        curr = self.head
        while curr != None:
            new_list.append(curr.val)
            curr = curr.next

        return new_list
