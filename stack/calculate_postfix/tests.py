import pytest

from stack.head_first_stack.stack import Stack

from .calculate_postfix import calculate_postfix


def get_postfix_stack_from_list(a_list):
    stack = Stack()
    for item in reversed(a_list):
        stack.push(item)
    return stack


def test_return_result_if_expression_is_correct():
    input_stack = get_postfix_stack_from_list([8, 2, '+', 5, '*', 9, '+', '='])

    assert calculate_postfix(input_stack) == 59


def test_return_none_if_there_is_no_return_operation():
    input_stack = get_postfix_stack_from_list([8, 2, '+', 5, '*', 9, '+'])

    assert calculate_postfix(input_stack) is None


def test_raise_error_if_operation_before_operands():
    input_stack = get_postfix_stack_from_list(['+', 1, 2])

    with pytest.raises(ValueError):
        calculate_postfix(input_stack)


def test_raise_error_if_there_is_incorrect_item():
    input_stack = get_postfix_stack_from_list([1, 2, 'q'])

    with pytest.raises(ValueError):
        calculate_postfix(input_stack)


def test_return_result_with_deep_nesting():
    input_stack = get_postfix_stack_from_list([10, 8, 2, '+', '*', '='])

    assert calculate_postfix(input_stack) == 100


def test_return_last_value_after_return_operation():
    # странное поведение, но исходя из описания логики оператора возврата - логичное
    input_stack = get_postfix_stack_from_list([1, 1, '+', 10, '=', '*'])

    assert calculate_postfix(input_stack) == 10
