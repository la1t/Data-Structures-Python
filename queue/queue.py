class QueueNode:
    def __init__(self, v):
        self.value = v
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        # сложность - O(1)
        new_node = QueueNode(item)
        if self.head is None:
            self.head = new_node
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        # сложность - O(1)
        if self.head is None:
            return None
        result = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return result

    def size(self):
        node = self.head
        result = 0
        while node is not None:
            result += 1
            node = node.next
        return result
