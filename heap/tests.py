import pytest

from .heap import Heap


@pytest.fixture
def heap():
    result = Heap()
    result.HeapArray = [11, 9, 4, 7, 8, 3, 1, 2, 5, 6, None, None, None, None, None]
    return result


def assert_heap_is_valid(heap, i=None):
    if not heap.HeapArray:
        return
    if not i:
        i = 0

    left_child = heap.get_left_child(i)
    if heap.exists(left_child):
        assert heap.HeapArray[left_child] < heap.HeapArray[i]
        assert_heap_is_valid(heap, left_child)
    
    right_child = heap.get_right_child(i)
    if heap.exists(right_child):
        assert heap.HeapArray[right_child] < heap.HeapArray[i]
        assert_heap_is_valid(heap, right_child)


def test_assert_heap_is_valid_if_heap_is_valid(heap):
    assert_heap_is_valid(heap)


def test_assert_heap_is_valid_if_heap_is_invalid(heap):
    heap.HeapArray[0] = 1
    with pytest.raises(AssertionError):
        assert_heap_is_valid(heap)


@pytest.mark.parametrize(
    'key', [12, 0]
)
def test_sift_up(heap, key):
    heap.HeapArray[10] = key

    heap.sift_up(10)

    assert_heap_is_valid(heap)


@pytest.mark.parametrize(
    'key', [12, 0]
)
def test_sift_down(heap, key):
    heap.HeapArray[0] = key

    heap.sift_down(0)

    assert_heap_is_valid(heap)


@pytest.mark.parametrize(
    'key_to_add', [10, 0],
)
def test_add(heap, key_to_add):
    result = heap.Add(key_to_add)

    assert result
    assert key_to_add in heap.HeapArray
    assert_heap_is_valid(heap)


def test_add_if_heap_is_packed(heap):
    heap.HeapArray[-5:] = [0, -1, -2, -3, -4]

    result = heap.Add(-5)

    assert not result
    assert -5 not in heap.HeapArray
    assert_heap_is_valid(heap)


def test_add_if_heap_is_empty_with_zero_len():
    heap = Heap()

    result = heap.Add(1)
    
    assert not result
    assert heap.HeapArray == []


def test_add_if_heap_is_empty_with_non_zero_len():
    heap = Heap()
    heap.HeapArray = [None] * 15

    result = heap.Add(10)

    assert result
    assert heap.HeapArray == [10] + [None] * 14


def test_get_max(heap):
    result = heap.GetMax()

    assert result == 11
    assert 11 not in heap.HeapArray
    assert_heap_is_valid(heap)


def test_get_max_if_heap_is_empty_with_zero_len():
    heap = Heap()

    result = heap.GetMax()

    assert result == -1
    assert heap.HeapArray == []


def test_get_max_if_heap_is_empty_with_non_zero_len():
    heap = Heap()
    heap.HeapArray = [None] * 15

    result = heap.GetMax()

    assert result == -1
    assert heap.HeapArray == [None] * 15


def test_get_max_if_heap_after_deletion_will_be_empty():
    heap = Heap()
    heap.HeapArray = [1] + [None] * 14

    result = heap.GetMax()

    assert result == 1
    assert heap.HeapArray == [None] * 15


def test_make_heap_creates_correct_heap():
    heap = Heap()
    a = [9, 4, 1, 3, 2, 10]
    heap.MakeHeap(a, 3)

    assert len(heap.HeapArray) == 15
    assert all([key in heap.HeapArray for key in a])
    assert_heap_is_valid(heap)
