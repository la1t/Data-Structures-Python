import pytest

from .queue import Queue


@pytest.fixture
def queue():
    return Queue()


def test_enqueue_if_queue_is_empty(queue):
    queue.enqueue(1)

    assert queue.write_stack.pop() == 1


def test_enqueue_if_queue_is_not_empty(queue):
    queue.enqueue(1)

    queue.enqueue(2)

    assert queue.write_stack.pop() == 2
    assert queue.write_stack.pop() == 1


def test_dequeue_if_queue_is_empty(queue):
    assert queue.dequeue() is None


def test_dequeue_if_queue_is_not_empty(queue):
    queue.enqueue(1)
    queue.enqueue(2)

    result = queue.dequeue()

    assert result == 1


def test_size_if_queue_is_empty(queue):
    assert queue.size() == 0


def test_size_if_queue_is_not_empty(queue):
    queue.enqueue(1)
    queue.enqueue(2)

    assert queue.size() == 2
