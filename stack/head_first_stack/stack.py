"""
При работе с головой, как с верхушкой стека, можно использовать однонаправленный св.сп.
"""

class StackNode:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.is_countable = True
        self.is_dummy = False


class DummyStackNode(StackNode):
    def __init__(self):
        self.value = None
        self.next = None
        self.is_countable = False
        self.is_dummy = True


class Stack:
    def __init__(self):
        self.head = DummyStackNode()
        self.tail = DummyStackNode()
        self.head.next = self.tail

    def size(self):
        node = self.head
        result = 0
        while node is not None:
            if node.is_countable:
                result += 1
            node = node.next
        return result

    def pop(self):
        # сложность - O(1)
        if self.head.next.is_dummy:
            return None
        popped = self.head.next
        self.head.next = popped.next
        return popped.value

    def push(self, value):
        # сложность - O(1)
        new_node = StackNode(value)
        new_node.next = self.head.next
        self.head.next = new_node

    def peek(self):
        return self.head.next.value
