"""
Для реализации стека использую двунаправленный связный список
Обычный связный список не будет оптимальным решением, если работать с хвостом, как с верхушкой стека
(из-за того, что удаление элемента из конца у однонаправленного св.сп. будет стоить О(n)
против О(1) у двунаправленного)
"""

class StackNode:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None
        self.is_countable = True
        self.is_dummy = False


class DummyStackNode(StackNode):
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None
        self.is_countable = False
        self.is_dummy = True


class Stack:
    def __init__(self):
        self.head = DummyStackNode()
        self.tail = DummyStackNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def size(self):
        node = self.head
        result = 0
        while node is not None:
            if node.is_countable:
                result += 1
            node = node.next
        return result

    def pop(self):
        if self.tail.prev.is_dummy:
            return None
        popped = self.tail.prev
        popped.prev.next = self.tail
        self.tail.prev = popped.prev
        return popped.value

    def push(self, value):
        new_node = StackNode(value)
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def peek(self):
        return self.tail.prev.value
