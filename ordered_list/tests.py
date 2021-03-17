import pytest

from .ordered_list import OrderedList, OrderedStringList


@pytest.fixture
def o_list():
    return OrderedList(True)


@pytest.mark.parametrize('v1,v2,result', [(0, 1, -1), (1, 1, 0), (1, 0, 1)])
def test_compare(o_list, v1, v2, result):
    assert o_list.compare(v1, v2) == result


def test_add_if_o_list_is_empty(o_list):
    o_list.add(1)

    assert o_list.get_all_values() == [1]
    assert o_list.head == o_list.tail


def test_add_in_the_head(o_list):
    o_list.add(2)

    o_list.add(1)

    assert o_list.get_all_values() == [1, 2]
    assert o_list.tail.prev == o_list.head


def test_add_in_the_tail(o_list):
    o_list.add(1)

    o_list.add(2)

    assert o_list.get_all_values() == [1, 2]
    assert o_list.tail.prev == o_list.head


def test_add_in_the_middle(o_list):
    o_list.add(1)
    o_list.add(3)
    
    o_list.add(2)

    assert o_list.get_all_values() == [1, 2, 3]
    assert o_list.head.next == o_list.tail.prev


def test_add_if_asc_is_False():
    o_list = OrderedList(False)
    o_list.add(1)
    o_list.add(3)
    o_list.add(2)

    assert o_list.get_all_values() == [3, 2, 1]


def test_find_if_item_exists_and_asc_is_True(o_list):
    o_list.add(1)
    o_list.add(2)
    o_list.add(3)

    assert o_list.find(2).value == 2


def test_find_if_item_exists_and_asc_is_False(o_list):
    o_list = OrderedList(False)
    o_list.add(1)
    o_list.add(2)
    o_list.add(3)

    assert o_list.find(2).value == 2


def test_find_if_item_does_not_exist_and_asc_is_True(o_list):
    o_list.add(1)

    assert o_list.find(2) is None


def test_find_if_item_does_not_exist_and_is_False():
    o_list = OrderedList(False)
    o_list.add(1)

    assert o_list.find(2) is None


def test_delete_if_item_does_not_exist(o_list):
    o_list.add(1)
    o_list.add(2)

    o_list.delete(3)

    assert o_list.get_all_values() == [1, 2]


def test_delete_if_item_exists(o_list):
    o_list.add(1)
    o_list.add(2)
    o_list.add(3)

    o_list.delete(2)

    assert o_list.get_all_values() == [1, 3]
    assert o_list.head.next == o_list.tail
    assert o_list.tail.prev == o_list.head


def test_delete_if_need_to_delete_head(o_list):
    o_list.add(1)
    o_list.add(2)

    o_list.delete(1)

    assert o_list.get_all_values() == [2]
    assert o_list.head.value == 2
    assert o_list.head == o_list.tail


def test_delete_if_need_to_delete_tail(o_list):
    o_list.add(1)
    o_list.add(2)

    o_list.delete(2)

    assert o_list.get_all_values() == [1]
    assert o_list.head.value == 1
    assert o_list.head == o_list.tail


def test_clean(o_list):
    o_list.add(1)
    o_list.add(2)

    o_list.clean(True)

    assert o_list.get_all_values() == []


def test_len_if_list_is_empty(o_list):
    assert o_list.len() == 0


def test_len_if_list_is_not_empty(o_list):
    o_list.add(1)
    o_list.add(2)

    assert o_list.len() == 2


@pytest.mark.parametrize('v1,v2,result', [
    ('  a', 'b  ', -1),
    (' a ', '    a', 0),
    ('b     ', 'a', 1),
])
def test_compare_for_ordered_string_list(v1, v2, result):
    o_list = OrderedStringList(True)

    assert o_list.compare(v1, v2) == result
