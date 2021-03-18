import pytest

from .native_dictionary import NativeDictionary


@pytest.mark.parametrize('value,result', [
    ('a', 12),
    ('b', 13),
    ('ab', 8)
])
def test_hash_fun(value, result):
    n_dict = NativeDictionary(17)
    
    assert n_dict.hash_fun(value) == result


def test_put_into_free_slot_create_slot_and_value_entries():
    n_dict = NativeDictionary(17)

    n_dict.put('a', 'b')
    
    assert n_dict.slots == [None] * 12 + ['a'] + [None] * 4
    assert n_dict.values == [None] * 12 + ['b'] + [None] * 4


def test_put_into_occupied_slot_replace_old_value():
    n_dict = NativeDictionary(17)
    n_dict.put('a', 'b')

    n_dict.put('a', 'c')

    assert n_dict.slots == [None] * 12 + ['a'] + [None] * 4
    assert n_dict.values == [None] * 12 + ['c'] + [None] * 4


def test_get_return_value_if_key_exists():
    n_dict = NativeDictionary(17)
    n_dict.put('a', 'b')

    assert n_dict.get('a') == 'b'


def test_get_return_None_if_key_does_not_exist():
    n_dict = NativeDictionary(17)
    
    assert n_dict.get('a') is None

def test_is_key_return_True_if_key_exists():
    n_dict = NativeDictionary(17)
    n_dict.put('a', 'b')

    assert n_dict.is_key('a')


def test_is_key_return_False_if_key_does_not_exist():
    n_dict = NativeDictionary(17)
    
    assert not n_dict.is_key('b')
