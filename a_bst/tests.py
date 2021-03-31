import pytest

from .a_bst import aBST


@pytest.fixture
def a_bst():
    a_bst = aBST(3)
    a_bst.Tree = [
        50,
        25, 75,
        20, 30, None, 80,
    ]
    return a_bst



@pytest.fixture
def empty_a_bst():
    return aBST(3)


@pytest.mark.parametrize(
    'depth,expected_tree_size', [
        (1, 1),
        (2, 3),
        (4, 15),
    ]
)
def test_calc_tree_size(depth, expected_tree_size):
    assert aBST.calc_tree_size(depth) == expected_tree_size


@pytest.mark.parametrize(
    'key,expected_index', [
        (50, 0),
        (25, 1),
        (70, None),
        (80, 6),
        (90, None)
    ]
)
def test_find_key_index(key, expected_index, a_bst):
    # a_bst = aBST(3)
    # a_bst.Tree = [
    #     50,
    #     25, 75,
    #     20, 30, 70, 80,
    # ]

    assert a_bst.FindKeyIndex(key) == expected_index


def test_find_key_index_if_bst_is_empty(empty_a_bst):
    assert empty_a_bst.FindKeyIndex(50) is None


def test_add_key_into_empty_a_bst(empty_a_bst):
    index = empty_a_bst.AddKey(50)

    assert index == 0
    assert empty_a_bst.Tree == [50] + [None] * 6


@pytest.mark.parametrize(
    'key,expected_index', [
        (20, 3),
        (51, 5),
        (76, 6),
    ]
)
def test_add_key_to_last_lvl(key, expected_index):
    a_bst = aBST(3)
    a_bst.Tree = [
        50,
        25, 75,
        None, None, None, None
    ]

    index = a_bst.AddKey(key)

    assert index == expected_index
    assert a_bst.Tree[index] == key


def test_add_key_does_nothing_if_key_already_exists(a_bst):
    orig_tree = a_bst.Tree.copy()

    index = a_bst.AddKey(25)

    assert index == 1
    assert orig_tree == a_bst.Tree


def test_add_key_returns_special_value_if_adding_is_impossible(a_bst):
    orig_tree = a_bst.Tree.copy()

    index = a_bst.AddKey(19)

    assert index == -1
    assert orig_tree == a_bst.Tree
