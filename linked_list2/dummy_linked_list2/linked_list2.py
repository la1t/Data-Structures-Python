class Node:

    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None
        self.is_countable = True
    
    def has_value(self, v):
        return self.value == v


class DummyNode(Node):    
    def __init__(self):
        self.prev = None
        self.next = None
        self.is_countable = False

    def has_value(self, v):
        return False


class LinkedListWithDummy:  
    def __init__(self):
        self.head = DummyNode()
        self.tail = DummyNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, afterNode, newNode):
        if afterNode is None:
            afterNode = self.tail.prev

        newNode.prev = afterNode
        newNode.next = afterNode.next
        afterNode.next = newNode
        newNode.next.prev = newNode

    def add_in_head(self, newNode):
        self.insert(self.head, newNode)
    
    def add_in_tail(self, item):
        self.insert(self.tail.prev, item)
    
    def find(self, val):
        node = self.head
        while node is not None:
            if node.has_value(val):
                return node
            node = node.next

    def find_all(self, val):
        found_nodes = []
        node = self.head
        while node is not None:
            if node.has_value(val):
                found_nodes.append(node)
            node = node.next
        return found_nodes

    def delete(self, val, all=False):
        if all:
            for node in self.find_all(val):
                node.prev.next = node.next
                node.next.prev = node.prev
        else:
            node = self.find(val)
            if node is not None:
                node.prev.next = node.next
                node.next.prev = node.prev
        node = self.head

    def clean(self):
        self.head.next = self.tail
        self.tail.prev = self.head

    def len(self):
        result = 0
        node = self.head
        while node is not None:
            if node.is_countable:
                result += 1
            node = node.next
        return result
