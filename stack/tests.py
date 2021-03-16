import pytest

from .stack import Stack


@pytest.fixture
def stack():
    return Stack()


def test_push_if_stack_is_empty(stack):
    stack.push(1)

    assert not stack.head.next.is_dummy
    assert stack.head.next.value == 1
    assert stack.head.next == stack.tail.prev


def test_push_if_stack_is_not_empty(stack):
    stack.push(0)

    stack.push(1)

    assert stack.head.next.value == 0
    assert stack.tail.prev.value == 1
    assert stack.tail.prev.prev == stack.head.next
    assert stack.head.next.next == stack.tail.prev


def test_size_if_stack_is_not_empty(stack):
    stack.push(0)

    assert stack.size() == 1


def test_size_if_stack_is_empty(stack):
    assert stack.size() == 0


def test_pop_if_stack_is_empty(stack):
    assert stack.pop() is None


def test_pop_if_after_this_stack_will_be_empty(stack):
    stack.push(0)

    item = stack.pop()

    assert item == 0
    assert stack.size() == 0
    assert stack.head.next.is_dummy
    assert stack.tail.prev.is_dummy


def test_pop_if_stack_has_several_items(stack):
    stack.push(0)
    stack.push(1)

    item = stack.pop()

    assert item == 1
    assert stack.tail.prev.value == 0
    assert stack.tail.prev.next.is_dummy


def test_peek_if_stack_is_empty(stack):
    assert stack.peek() is None


def test_peek_if_stack_is_empty(stack):
    stack.push(0)

    item = stack.peek()

    assert item == 0
    assert not stack.tail.prev.is_dummy
