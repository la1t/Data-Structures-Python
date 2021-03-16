import pytest

from .dyn_array import DynArray


@pytest.fixture
def dyn_array():
    return DynArray()


def test_insert_if_there_is_no_buffer_overflow(dyn_array):
    dyn_array.append(0)
    dyn_array.append(1)
    dyn_array.append(2)

    dyn_array.insert(1, 1.5)

    assert dyn_array[0] == 0
    assert dyn_array[1] == 1.5
    assert dyn_array[2] == 1
    assert dyn_array[3] == 2
    assert len(dyn_array) == 4
    assert dyn_array.capacity == 16


def test_insert_if_there_is_buffer_overload(dyn_array):
    for i in range(16):
        dyn_array.append(i)
    
    dyn_array.insert(0, -1)

    assert dyn_array[0] == -1
    assert len(dyn_array) == 17
    assert dyn_array.capacity == 32


def test_insert_in_the_end_of_array(dyn_array):
    dyn_array.append(0)

    dyn_array.insert(1, 1)

    assert dyn_array[0] == 0
    assert dyn_array[1] == 1


def test_insert_raise_error_if_index_is_out_of_bounds(dyn_array):
    with pytest.raises(IndexError):
        dyn_array.insert(1, 1)


def test_delete_if_there_is_no_need_for_buffer_decrease(dyn_array):
    dyn_array.append(0)
    dyn_array.append(1)
    dyn_array.append(2)

    dyn_array.delete(1)

    assert len(dyn_array) == 2
    assert dyn_array[0] == 0
    assert dyn_array[1] == 2
    assert dyn_array.capacity == 16


def test_delete_if_there_is_need_for_buffer_decrease(dyn_array):
    for i in range(17):
        dyn_array.append(i)
    dyn_array.delete(0)

    dyn_array.delete(0)

    assert len(dyn_array) == 15
    assert dyn_array.capacity == 21


def test_delete_raise_error_if_index_is_out_of_bounds(dyn_array):
    with pytest.raises(IndexError):
        dyn_array.delete(0)
