class Deque:
    # оценки сложности даны, исходя из предположения, что список Python
    # реализован, как динамический массив. Иначе же сложность будет отличаться
    # в зависимости от выбранной реализации
    # так, для двунаправленных св.списков сложность на все четыре операции - O(1)
    # для однонаправленных - addFront/addTail/removeFront - O(1), у removeTail - O(n)
    def __init__(self):
        self.storage = []

    def addFront(self, item):
        # сложность - O(n)
        self.storage.insert(0, item)

    def addTail(self, item):
        # сложность - o(1)
        self.storage.append(item)

    def removeFront(self):
        # сложность - O(n)
        if len(self.storage) == 0:
            return None
        result = self.storage[0]
        self.storage.pop(0)
        return result

    def removeTail(self):
        # сложность - O(n)
        if len(self.storage) == 0:
            return None
        result = self.storage[len(self.storage) - 1]
        self.storage.pop(len(self.storage) - 1)
        return result

    def size(self):
        return len(self.storage)
