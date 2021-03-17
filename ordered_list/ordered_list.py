class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 == v2:
            return 0
        else:
            return 1
    
    def asc_compare(self, v1, v2):
        return self.compare(v1, v2) if self.__ascending else -self.compare(v1, v2)

    def add(self, value):
        # сложность - O(n)
        # находим элемент, перед которым будет вставлять новый
        node = self.head
        while node is not None and self.asc_compare(node.value, value) == -1:
            node = node.next
        new_node = Node(value)
        # если node is None, значит вставлять мы должны после хвоста
        if node is None:
            new_node.prev = self.tail
            if self.tail is not None:
                self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.prev = node.prev
            if node.prev is not None:
                node.prev.next = new_node
            node.prev = new_node
        if self.head == node:
            self.head = new_node
        new_node.next = node

    def find(self, val):
        # сложность - O(n), она не изменяется, если мы останавливаем поиск раньше,
        # поскольку в худшем случае нам все равно придется пройти по всему списку
        node = self.head
        while node is not None:
            if self.asc_compare(node.value, val) == 0:
                return node
            elif self.asc_compare(node.value, val) == 1:
                return None
            node = node.next

    def delete(self, val):
        # сложность - O(n)
        node = self.find(val)
        if node is None:
            return

        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        # сложность - O(n)
        result = 0
        node = self.head
        while node is not None:
            result += 1
            node = node.next
        return result

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r
    
    def get_all_values(self):
        return [node.value for node in self.get_all()]

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        if v1.strip() < v2.strip():
            return -1
        elif v1.strip() == v2.strip():
            return 0
        else:
            return 1
