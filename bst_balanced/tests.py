import pytest

from .generate_bbst_array import GenerateBBSTArray
from .balanced_bst import BalancedBST, BSTNode


@pytest.mark.parametrize(
    'orig_list,expected_list',
    [
        (
            [1, 3, 2],
            [2, 1, 3],
        ),
        (
            [3, 1, 9, 6, 4, 12, 7, 2, 11],
            [6, 3, 11, 2, 4, 9, 12, 1, None, None, None, 7, None, None, None]
        ),
        (
            [],
            []
        )
    ]
)
def test_generate_bbst_array(orig_list, expected_list):
    assert GenerateBBSTArray(orig_list) == expected_list


@pytest.fixture(scope='function')
def root():
    root = BSTNode(6, None)
    root.Level = 1
    return root


@pytest.fixture(scope='function')
def level_1(root):
    level_1 = [BSTNode(3, root), BSTNode(11, root)]
    level_1[0].Level = 2
    level_1[1].Level = 2
    root.add_childs(*level_1)
    return level_1


@pytest.fixture(scope='function')
def level_2(level_1):
    level_2 = [BSTNode(2, level_1[0]), BSTNode(4, level_1[0]), BSTNode(9, level_1[1]), BSTNode(12, level_1[1])]
    level_2[0].Level = 3
    level_2[1].Level = 3
    level_2[2].Level = 3
    level_2[3].Level = 3
    level_1[0].add_childs(*level_2[:2])
    level_1[1].add_childs(*level_2[2:])
    return level_2


def test_balanced_bst_is_balanced_ret_true_if_tree_is_without_diff(root, level_1, level_2):
    bst = BalancedBST()

    assert bst.IsBalanced(root)


def test_balanced_bst_is_balanced_ret_true_if_tree_is_with_diff_is_1(root, level_1):
    level_1[0].add_childs(BSTNode(2, level_1[0]), None)
    bst = BalancedBST()

    assert bst.IsBalanced(root)


def test_balanced_bst_is_balanced_ret_false_if_tree_is_with_diff_more_than_1(root, level_1):
    level_1[0].add_childs(BSTNode(2, level_1[0]), BSTNode(4, level_1[0]))
    bst = BalancedBST()

    assert not bst.IsBalanced(root) 


def assert_tree_is_valid(tree, node=None):
    if not tree.Root:
        return
    if node is None:
        node = tree.Root
    
    if node.LeftChild:
        assert node.LeftChild.Parent == node
        assert node.LeftChild.Level == node.Level + 1
        assert node.LeftChild.NodeKey < node.NodeKey
        assert_tree_is_valid(tree, node.LeftChild)
    
    if node.RightChild:
        assert node.RightChild.Parent == node
        assert node.RightChild.Level == node.Level + 1
        assert node.RightChild.NodeKey >= node.NodeKey
        assert_tree_is_valid(tree, node.RightChild)


def test_assert_tree_is_valid_does_not_assert_if_tree_is_valid(root, level_1, level_2):
    tree = BalancedBST()
    tree.Root = root

    assert_tree_is_valid(tree)


def test_assert_tree_is_valid_asserts_if_tree_is_invalid(root):
    root.add_childs(BSTNode(7, root), None)
    tree = BalancedBST()
    tree.Root = root

    with pytest.raises(AssertionError):
        assert_tree_is_valid(tree)


def assert_tree_is_balanced(tree):
    if not tree.Root:
        return
    assert tree.IsBalanced(tree.Root)


@pytest.mark.parametrize(
    'orig_list',
    [
        [1, 3, 2],
        [3, 1, 9, 6, 4, 12, 7, 2, 11],
        [],
    ]
)
def test_fill_tree(orig_list):
    tree = BalancedBST()
    tree.GenerateTree(orig_list)

    assert_tree_is_valid(tree)
    assert_tree_is_balanced(tree)
