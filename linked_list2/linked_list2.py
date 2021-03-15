class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next

    def find_all(self, val):
        found_nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                found_nodes.append(node)
            node = node.next
        return found_nodes

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node.value == val:
                if node == self.head:
                    self.head = node.next
                else:
                    node.prev.next = node.next
                if node == self.tail:
                    self.tail = node.prev
                else:
                    node.next.prev = node.prev
                if not all:
                    return
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        result = 0
        node = self.head
        while node is not None:
            result += 1
            node = node.next
        return result

    def insert(self, afterNode, newNode):
        if afterNode is None and self.len() == 0:
            self.head = newNode
            self.tail = newNode
            return

        if afterNode is None:
            afterNode = self.tail
        
        newNode.prev = afterNode
        newNode.next = afterNode.next
        afterNode.next = newNode
        if newNode.next is not None:
            newNode.next.prev = newNode
        if afterNode == self.tail:
            self.tail = newNode

    def add_in_head(self, newNode):
        if self.head is not None:
            self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode
        if self.tail is None:
            self.tail = newNode
