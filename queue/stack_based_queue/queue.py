from stack.head_first_stack.stack import Stack


class Queue:
    def __init__(self):
        self.write_stack = Stack()
        self.read_stack = Stack()

    def enqueue(self, item):
        self.write_stack.push(item)

    def dequeue(self):
        # сложность - O(n) для пустого буфера, o(1) для непустого
        if self.read_stack.size() == 0:
            while (item := self.write_stack.pop()) is not None:
                self.read_stack.push(item)
        
        return self.read_stack.pop()

    def size(self):
        # сложность - O(n)
        return self.read_stack.size() + self.write_stack.size()
