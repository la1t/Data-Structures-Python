from stack.head_first_stack.stack import Stack


ARITHMETIC_OPS = ['+', '*']


def calculate_postfix(input_stack):
    calc_stack = Stack()
    current = input_stack.pop()
    while current is not None:
        if isinstance(current, int):
            calc_stack.push(current)
        elif current in ARITHMETIC_OPS:
            op1, op2 = calc_stack.pop(), calc_stack.pop()
            if op1 is None or op2 is None:
                raise ValueError('Operation before operands')
            calc_stack.push(execute_op(op1, op2, current))
        elif current == '=':
            return calc_stack.pop()
        else:
            raise ValueError(f'Incorrect item in input stack: {current}')
        current = input_stack.pop()


def execute_op(op1, op2, operation):
    if operation == '+':
        return op1 + op2
    elif operation == '*':
        return op1 * op2
    else:
        raise ValueError(f'Incorrect operation "{operation}')
