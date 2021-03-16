import pytest

from .queue import Queue


@pytest.fixture
def queue():
    return Queue()


def test_enqueue_if_queue_is_empty(queue):
    queue.enqueue(1)

    assert queue.head is not None
    assert queue.head.value == 1
    assert queue.head.next is None
    assert queue.tail == queue.head


def test_enqueue_if_queue_is_not_empty(queue):
    queue.enqueue(1)

    queue.enqueue(2)

    assert queue.head.value == 1
    assert queue.head.next == queue.tail
    assert queue.tail.value == 2
    assert queue.tail.next is None


def test_dequeue_if_queue_is_empty(queue):
    assert queue.dequeue() is None


def test_dequeue_if_queue_is_not_empty(queue):
    queue.enqueue(1)
    queue.enqueue(2)

    result = queue.dequeue()

    assert result == 1
    assert queue.head.value == 2
    assert queue.tail == queue.head
    assert queue.tail.next is None


def test_dequeue_last_item(queue):
    queue.enqueue(1)

    result = queue.dequeue()
    
    assert result == 1
    assert queue.head is None
    assert queue.tail is None


def test_size_if_queue_is_empty(queue):
    assert queue.size() == 0


def test_size_if_queue_is_not_empty(queue):
    queue.enqueue(1)
    queue.enqueue(2)

    assert queue.size() == 2
