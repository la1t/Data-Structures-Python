from .deque import Deque


def is_palindrome(a_string):
    deque = Deque()
    for symb in a_string:
        deque.addTail(symb)
    for symb in a_string:
        if symb != deque.removeTail():
            return False
    return True
