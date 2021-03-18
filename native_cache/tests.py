import pytest

from .native_cache import NativeCache


@pytest.mark.parametrize('value,result', [
    ('a', 12),
    ('b', 13),
    ('ab', 8)
])
def test_hash_fun(value, result):
    n_cache = NativeCache(17)
    
    assert n_cache.hash_fun(value) == result


def test_put_into_free_slot_creates_slot_and_value_entries():
    n_cache = NativeCache(17)

    n_cache.put('a', 'b')
    
    assert n_cache.slots == [None] * 12 + ['a'] + [None] * 4
    assert n_cache.values == [None] * 12 + ['b'] + [None] * 4
    assert n_cache.hits == [0] * 17


def test_put_into_occupied_slot_replaces_old_value_does_not_change_hits():
    n_cache = NativeCache(17)
    n_cache.put('a', 'b')
    n_cache.get('a')

    n_cache.put('a', 'c')

    assert n_cache.slots == [None] * 12 + ['a'] + [None] * 4
    assert n_cache.values == [None] * 12 + ['c'] + [None] * 4
    assert n_cache.hits == [0] * 12 + [1] + [0] * 4


def test_put_into_packed_cache_replaces_min_hit_value():
    n_cache = NativeCache(17)
    for i in range(17):
        n_cache.put(chr(i), i)
        n_cache.get(chr(i))
        n_cache.get(chr(i))
        # ко всем ключам, кроме 14, обращаемся трижды, к 14 - дважды
        if i != 14:
            n_cache.get(chr(i))

    n_cache.put(chr(100), 100)

    assert n_cache.get(chr(100)) == 100
    assert n_cache.get(chr(14)) is None
    assert n_cache.hits[n_cache.find_key_slot(chr(100))] == 1


def test_get_returns_value_and_increment_hits_if_key_exists():
    n_cache = NativeCache(17)
    n_cache.put('a', 'b')

    assert n_cache.get('a') == 'b'
    assert n_cache.hits == [0] * 12 + [1] + [0] * 4


def test_get_returns_None_and_does_not_touch_hits_if_key_does_not_exist():
    n_cache = NativeCache(17)
    
    assert n_cache.get('a') is None
    assert n_cache.hits == [0] * 17

def test_is_key_returns_True_and_increment_hits_if_key_exists():
    n_cache = NativeCache(17)
    n_cache.put('a', 'b')

    assert n_cache.is_key('a')
    assert n_cache.hits == [0] * 12 + [1] + [0] * 4


def test_is_key_returns_False_and_does_not_touch_hits_if_key_does_not_exist():
    n_cache = NativeCache(17)
    
    assert not n_cache.is_key('b')
    assert n_cache.hits == [0] * 17
