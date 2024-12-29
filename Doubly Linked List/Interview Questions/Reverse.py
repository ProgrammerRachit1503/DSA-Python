class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value = None) -> None:
        if value is None:
            self.head = None
            self.tail = None
        else:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        self.length = 1 if value is not None else 0

    def print_list(self) -> None:
        temp: Node = self.head

        while temp.next is not None:
            print(temp.value, end=" <-> ")
            temp = temp.next
        print(temp.value)
        # print(None)

    def append(self, value) -> bool:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def reverse(self) -> bool:
        if self.length == 0:
            return False

        if self.length == 1:
            return True

        else:
            temp: Node = self.head

            while temp is not None:
                temp.next, temp.prev = temp.prev, temp.next
                temp = temp.prev

            self.head, self.tail = self.tail, self.head
            return True


def main() -> None:
    pass


if __name__ == "__main__":
    main()
