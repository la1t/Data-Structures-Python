from stack.head_first_stack.stack import Stack


def is_brackets_balanced(a_string):
    stack = Stack()
    for bracket in a_string:
        if bracket == '(':
            stack.push(True)
        else:
            if not stack.pop():
                return False
    return stack.size() == 0
