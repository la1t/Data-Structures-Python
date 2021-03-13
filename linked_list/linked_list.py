class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
    
    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next
    
    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None
    
    def delete(self, val, all=False):
        node = self.head
        prev = None

        while node is not None:
            if node.value == val:
                if node == self.head:
                    self.head = node.next
                if node == self.tail:
                    self.tail = prev
                
                if prev is not None:
                    prev.next = node.next
                if not all:
                    return
                node = prev
            
            prev = node
            if node is not None:
                node = node.next
            else:
                node = self.head
    
    def clean(self):
        self.head = None
        self.tail = None
    
    def find_all(self, val):
        found_nodes = []
        
        node = self.head
        while node is not None:
            if node.value == val:
                found_nodes.append(node)
            node = node.next
        
        return found_nodes
    
    def len(self):
        result = 0

        node = self.head
        while node is not None:
            result += 1
            node = node.next
        
        return result
    
    def insert(self, afterNode, newNode):
        if afterNode == self.tail:
            self.tail = newNode

        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode
