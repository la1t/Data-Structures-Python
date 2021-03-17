from .deque import Deque


def is_palindrome(a_string):
    deque = Deque()
    for symb in a_string:
        deque.addTail(symb)
    
    while deque.size() > 1:
        if deque.removeFront() != deque.removeTail():
            return False
    return True
