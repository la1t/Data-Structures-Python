from .deque import Deque


def is_palindrome(a_string):
    deque = Deque()
    for symb in a_string:
        deque.addTail(symb)
    
    first_symb = deque.removeFront()
    last_symb = deque.removeTail()
    while last_symb is not None:
        if first_symb != last_symb:
            return False
        first_symb = deque.removeFront()
        last_symb = deque.removeTail()
    return True
