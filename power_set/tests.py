import pytest
import time
import random
import contextlib

from .power_set import PowerSet


def gen_big_set():
    set_ = PowerSet()
    for _ in range(20000):
        set_.put(str(random.randint(0, 100000)))
    return set_


@contextlib.contextmanager
def assert_exec_time(timeout):
    start = time.time()
    yield
    end = time.time()
    diff = end - start
    assert diff < timeout


@pytest.fixture
def ab_set():
    res = PowerSet()
    res.put('a')
    res.put('b')
    return res


@pytest.fixture
def a_set():
    res = PowerSet()
    res.put('a')
    return res


@pytest.fixture
def b_set():
    res = PowerSet()
    res.put('b')
    return res


@pytest.fixture
def c_set():
    res = PowerSet()
    res.put('c')
    return res


@pytest.fixture
def ac_set():
    res = PowerSet()
    res.put('a')
    res.put('c')
    return res


@pytest.fixture
def abc_set():
    res = PowerSet()
    res.put('a')
    res.put('b')
    res.put('c')
    return res


@pytest.fixture
def ce_set():
    res = PowerSet()
    res.put('c')
    res.put('e')
    return res


@pytest.fixture
def empty_set():
    return PowerSet()


def test_put_if_item_does_not_exist():
    p_set = PowerSet()

    p_set.put('a')

    assert p_set.get_all_items() == ['a']


def test_put_if_item_exists():
    p_set = PowerSet()
    p_set.put('a')

    p_set.put('a')

    assert p_set.get_all_items() == ['a']


def test_size_return_len_hash_table_values():
    p_set = PowerSet()
    p_set.put('a')
    p_set.put('a')
    p_set.put('b')

    assert p_set.size() == 2


def test_get_return_True_if_item_exists():
    p_set = PowerSet()
    p_set.put('a')

    assert p_set.get('a')


def test_get_return_False_if_item_does_not_exist():
    p_set = PowerSet()
    
    assert not p_set.get('a')


def test_remove_delete_existing_item_and_return_True():
    p_set = PowerSet()
    p_set.put('a')
    p_set.put('b')

    result = p_set.remove('a')

    assert result
    assert p_set.get_all_items() == ['b']


def test_remove_return_False_if_item_does_not_exist():
    p_set = PowerSet()
    p_set.put('a')
    p_set.put('b')

    result = p_set.remove('c')

    assert not result
    assert p_set.get_all_items() == ['a', 'b']


def test_intersection_returns_items_that_exists_in_both_of_the_sets(ab_set, ac_set, a_set, empty_set):
    assert ab_set.intersection(ac_set) == a_set
    assert ac_set.intersection(ab_set) == a_set
    assert ab_set.intersection(empty_set) == empty_set
    assert empty_set.intersection(ab_set) == empty_set


def test_load_intersection():
    set1 = gen_big_set()
    set2 = gen_big_set()

    with assert_exec_time(timeout=1):
        set1.intersection(set2)


def test_union_returns_items_that_exist_in_at_least_one_of_the_sets(ab_set, ac_set, abc_set, empty_set):
    assert ab_set.union(ac_set) == abc_set
    assert ac_set.union(ab_set) == abc_set

    assert ab_set.union(empty_set) == ab_set
    assert empty_set.union(ab_set) == ab_set


def test_load_union():
    set1 = gen_big_set()
    set2 = gen_big_set()

    with assert_exec_time(timeout=.1):
        set1.union(set2)


def test_difference_return_items_that_exist_in_first_one_and_do_not_exist_in_second_one(ab_set, ac_set, a_set, b_set, c_set, ce_set, empty_set):
    assert ab_set.difference(ac_set) == b_set
    assert ac_set.difference(ab_set) == c_set

    assert ab_set.difference(ce_set) == ab_set
    assert ce_set.difference(ab_set) == ce_set
    
    assert b_set.difference(ab_set) == empty_set
    assert ab_set.difference(b_set) == a_set


def test_difference_load():
    set1 = gen_big_set()
    set2 = gen_big_set()

    with assert_exec_time(timeout=1):
        set1.difference(set2)


def test_is_subset_return_True_if_second_set_is_subset_of_the_first_one(ab_set, a_set):
    assert ab_set.issubset(a_set)


def test_is_subset_return_False_if_second_set_is_not_subset_of_the_first_one(ab_set, ac_set):
    assert not ab_set.issubset(ac_set)
