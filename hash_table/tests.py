import pytest

from .hash_table import HashTable


@pytest.mark.parametrize('value,result', [
    ('a', 12),
    ('b', 13),
    ('ab', 8)
])
def test_hash_fun(value, result):
    hash_table = HashTable(17, 3)
    
    assert hash_table.hash_fun(value) == result


def test_seek_slot_if_hash_slot_is_free():
    hash_table = HashTable(17, 3)

    assert hash_table.seek_slot('a') == 12


def test_seek_slot_if_hash_slot_is_not_free():
    hash_table = HashTable(17, 3)
    hash_table.slots[12] = 'a'

    assert hash_table.seek_slot('a') == 15


def test_seek_slot_make_cycle_if_free_slot_is_not_found():
    hash_table = HashTable(17, 3)
    hash_table.slots[12] = hash_table.slots[15] = 'a'

    assert hash_table.seek_slot('a') == 1


def test_seek_slot_return_None_if_there_are_no_free_slots():
    hash_table = HashTable(17, 3)
    hash_table.slots = ['a'] * 17

    assert hash_table.seek_slot('a') is None


def test_put_if_there_is_free_slot():
    hash_table = HashTable(17, 3)

    result = hash_table.put('a')

    assert result == 12
    assert hash_table.slots == [None] * 12 + ['a'] + [None] * 4


def test_put_if_there_are_no_free_slots():
    hash_table = HashTable(17, 3)
    hash_table.slots = ['a'] * 17

    assert hash_table.put('a') is None


def test_find_if_item_exists():
    hash_table = HashTable(17, 3)
    hash_table.put('a')

    assert hash_table.find('a') == 12


def test_find_if_item_does_not_exist():
    hash_table = HashTable(17, 3)

    assert hash_table.find('a') is None
