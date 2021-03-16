import pytest

from .deque import Deque
from .is_palindrome import is_palindrome


@pytest.fixture
def deque():
    return Deque()


def test_add_front_if_deque_is_empty(deque):
    deque.addFront(0)

    assert deque.storage == [0]


def test_add_front_if_deque_is_not_empty(deque):
    deque.addFront(0)

    deque.addFront(1)

    assert deque.storage == [1, 0]


def test_add_tail_if_deque_is_empty(deque):
    deque.addTail(0)

    assert deque.storage == [0]


def test_add_tail_if_deque_is_not_empty(deque):
    deque.addTail(0)

    deque.addTail(1)

    assert deque.storage == [0, 1]


def test_remove_front_if_deque_is_empty(deque):
    assert deque.removeFront() is None


def test_remove_front_if_deque_is_not_empty(deque):
    deque.addFront(0)
    deque.addFront(1)

    result = deque.removeFront()

    assert result == 1
    assert deque.storage == [0]


def test_remove_tail_if_deque_is_empty(deque):
    assert deque.removeTail() is None


def test_remove_tail_if_deque_is_not_empty(deque):
    deque.addTail(0)
    deque.addTail(1)

    result = deque.removeTail()

    assert result == 1
    assert deque.storage == [0]


def test_size(deque):
    deque.addTail(1)

    assert deque.size() == 1


def test_is_palindrome_return_true_if_string_is_palindrome():
    assert is_palindrome('топот')


def test_is_palindrome_return_true_for_empty_string():
    assert is_palindrome('')


def test_is_palindrome_return_false_if_string_is_not_palindrome():
    assert not is_palindrome('палиндром')
