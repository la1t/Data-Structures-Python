import pytest

from .bst import BST, BSTNode, BSTFind


@pytest.fixture(scope="function")
def root():
    return BSTNode(50, '50', None)



@pytest.fixture(scope='function')
def empty_tree():
    return BST(None)


@pytest.fixture(scope="function")
def tree(root):
    return BST(root)


@pytest.fixture(scope='function')
def nodes_lvl_1(root):
    nodes_lvl_1 = [
        BSTNode(25, '25', root),
        BSTNode(75, '75', root),
    ]
    root.LeftChild = nodes_lvl_1[0]
    root.RightChild = nodes_lvl_1[1]
    return nodes_lvl_1


@pytest.fixture(scope="function")
def nodes_lvl_2_1(nodes_lvl_1):
    nodes_lvl_2_1 = [
        BSTNode(20, '20', nodes_lvl_1[0]),
        BSTNode(30, '30',  nodes_lvl_1[0])
    ]
    nodes_lvl_1[0].LeftChild = nodes_lvl_2_1[0]
    nodes_lvl_1[0].RightChild = nodes_lvl_2_1[1]
    return nodes_lvl_2_1


@pytest.fixture(scope="function")
def nodes_lvl_2_2(nodes_lvl_1):
    nodes_lvl_2_2 = [
        BSTNode(70, '70', nodes_lvl_1[1]),
        BSTNode(80, '80', nodes_lvl_1[1])
    ]
    nodes_lvl_1[1].LeftChild = nodes_lvl_2_2[0]
    nodes_lvl_1[1].RightChild = nodes_lvl_2_2[1]
    return nodes_lvl_2_2


@pytest.fixture(scope="function")
def nodes_lvl_3(nodes_lvl_2_2):
    nodes_lvl_3 = [
        BSTNode(79, '79', nodes_lvl_2_2[1]),
        BSTNode(81, '81', nodes_lvl_2_2[1]),
    ]
    nodes_lvl_2_2[1].LeftChild = nodes_lvl_3[0]
    nodes_lvl_2_2[1].RightChild = nodes_lvl_3[1]
    return nodes_lvl_3


def test_find_if_there_is_no_item_to_find_and_this_item_must_be_left(tree, nodes_lvl_2_1, nodes_lvl_2_2):
    find_result = tree.FindNodeByKey(60)

    assert find_result.Node == nodes_lvl_2_2[0]
    assert not find_result.NodeHasKey
    assert find_result.ToLeft


def test_find_if_there_is_no_item_to_find_and_this_item_must_be_right(tree, nodes_lvl_2_1, nodes_lvl_2_2):
    find_result = tree.FindNodeByKey(90)

    assert find_result.Node == nodes_lvl_2_2[1]
    assert not find_result.NodeHasKey
    assert not find_result.ToLeft


def test_find_if_there_is_item_to_find(tree, nodes_lvl_2_1, nodes_lvl_2_2):
    find_result = tree.FindNodeByKey(30)

    assert find_result.Node == nodes_lvl_2_1[1]
    assert find_result.NodeHasKey


def test_find_if_tree_is_empty():
    tree = BST(None)

    find_result = tree.FindNodeByKey(10)

    assert find_result.Node is None
    assert not find_result.NodeHasKey


def test_add_if_new_item_must_be_left(tree, nodes_lvl_2_1):
    tree.AddKeyValue(19, '19')
    
    assert nodes_lvl_2_1[0].LeftChild is not None
    new_node = nodes_lvl_2_1[0].LeftChild
    assert new_node.Parent == nodes_lvl_2_1[0]
    assert new_node.NodeKey == 19
    assert new_node.NodeValue == '19'
    assert new_node.LeftChild is None
    assert new_node.RightChild is None


def test_add_if_new_item_must_be_right(tree, nodes_lvl_2_1):
    tree.AddKeyValue(21, '21')

    assert nodes_lvl_2_1[0].RightChild is not None
    new_node = nodes_lvl_2_1[0].RightChild
    assert new_node.Parent == nodes_lvl_2_1[0]
    assert new_node.NodeKey == 21
    assert new_node.NodeValue == '21'
    assert new_node.LeftChild is None
    assert new_node.RightChild is None


def test_add_if_item_already_exists(tree, nodes_lvl_2_1):
    tree.AddKeyValue(20, 'new value')

    assert nodes_lvl_2_1[0].LeftChild is None
    assert nodes_lvl_2_1[0].RightChild is None
    assert nodes_lvl_2_1[0].NodeValue == '20'


def test_add_if_tree_is_empty(empty_tree):
    empty_tree.AddKeyValue(20, '20')

    assert empty_tree.Root is not None
    new_node = empty_tree.Root
    assert new_node.NodeKey == 20
    assert new_node.NodeValue == '20'


def test_find_min_from_root(tree, root, nodes_lvl_2_1, nodes_lvl_2_2):
    assert tree.FinMinMax(root, False) == nodes_lvl_2_1[0]


def test_find_min_from_any_node(tree, root, nodes_lvl_1, nodes_lvl_2_1, nodes_lvl_2_2):
    assert tree.FinMinMax(nodes_lvl_1[1], nodes_lvl_2_2[0])


def test_find_max_from_root(tree, root, nodes_lvl_2_1, nodes_lvl_2_2):
    assert tree.FinMinMax(root, True) == nodes_lvl_2_2[1]


def test_find_max_from_any_node(tree, root, nodes_lvl_1, nodes_lvl_2_1, nodes_lvl_2_2):
    assert tree.FinMinMax(nodes_lvl_1[0], nodes_lvl_2_1[1])


def test_delete_node_if_min_node_from_right_subtree_does_not_have_descendans(tree, root, nodes_lvl_1, nodes_lvl_2_1, nodes_lvl_2_2, nodes_lvl_3):
    is_deleted = tree.DeleteNodeByKey(75)

    assert is_deleted
    assert root.RightChild == nodes_lvl_3[0]
    assert nodes_lvl_3[0].Parent == root
    assert nodes_lvl_3[0].LeftChild == nodes_lvl_2_2[0]
    assert nodes_lvl_3[0].RightChild == nodes_lvl_2_2[1]
    assert nodes_lvl_2_2[0].Parent == nodes_lvl_3[0]
    assert nodes_lvl_2_2[1].Parent == nodes_lvl_3[0]
    assert nodes_lvl_2_2[0].LeftChild is None


def test_delete_node_if_min_node_from_right_subtree_has_descendans(tree, root, nodes_lvl_1, nodes_lvl_2_1, nodes_lvl_2_2, nodes_lvl_3):
    node_lvl_4 = BSTNode(79.5, '79.5', nodes_lvl_3[0])
    nodes_lvl_3[0].RightChild = node_lvl_4

    is_deleted = tree.DeleteNodeByKey(75)

    assert is_deleted
    assert root.RightChild == nodes_lvl_3[0]
    assert nodes_lvl_3[0].Parent == root
    assert nodes_lvl_3[0].LeftChild == nodes_lvl_2_2[0]
    assert nodes_lvl_3[0].RightChild == nodes_lvl_2_2[1]
    assert nodes_lvl_2_2[0].Parent == nodes_lvl_3[0]
    assert nodes_lvl_2_2[1].Parent == nodes_lvl_3[0]
    assert nodes_lvl_2_2[1].LeftChild == node_lvl_4
    assert node_lvl_4.Parent == nodes_lvl_2_2[1]


def test_delete_node_if_min_node_node_to_delete_is_from_left_side(tree, root, nodes_lvl_1, nodes_lvl_2_1):
    is_deleted = tree.DeleteNodeByKey(25)

    assert is_deleted
    assert root.LeftChild == nodes_lvl_2_1[1]
    assert nodes_lvl_2_1[1].Parent == root
    assert nodes_lvl_2_1[1].LeftChild == nodes_lvl_2_1[0]
    assert nodes_lvl_2_1[0].Parent == nodes_lvl_2_1[1]
    assert nodes_lvl_2_1[1].RightChild is None


def test_delete_node_by_key_if_there_is_not_node_to_found(tree, nodes_lvl_2_1, nodes_lvl_2_2):
    is_deleted = tree.DeleteNodeByKey(123)

    assert not is_deleted


def test_delete_leaf_from_left_side(tree, root, nodes_lvl_1):
    is_deleted = tree.DeleteNodeByKey(25)

    assert is_deleted
    assert root.LeftChild is None


def test_delete_leaf_from_right_side(tree, root, nodes_lvl_1):
    is_deleted = tree.DeleteNodeByKey(75)

    assert is_deleted
    assert root.RightChild is None


def test_delete_root(tree, root, nodes_lvl_1):
    is_deleted = tree.DeleteNodeByKey(50)
    
    assert is_deleted
    assert tree.Root == nodes_lvl_1[1]
    assert nodes_lvl_1[1].Parent is None
    assert nodes_lvl_1[1].LeftChild == nodes_lvl_1[0]
    assert nodes_lvl_1[0].Parent == nodes_lvl_1[1]
    assert nodes_lvl_1[1].RightChild is None


def test_delete_root_if_this_is_leaf(tree, root):
    is_deleted = tree.DeleteNodeByKey(50)

    assert is_deleted
    assert tree.Root is None


def test_count(tree, root, nodes_lvl_1, nodes_lvl_2_1, nodes_lvl_2_2):
    assert tree.Count() == 7


def test_count_if_tree_is_empty(empty_tree):
    return empty_tree.Count() == 0
