import pytest

from .simple_tree import SimpleTree, SimpleTreeNode
from .enrich_levels import enrich_levels


@pytest.fixture(scope="function")
def root():
    return SimpleTreeNode(1, None)


@pytest.fixture(scope="function")
def tree(root):
    return SimpleTree(root)


@pytest.fixture(scope='function')
def nodes_lvl_1(tree, root):
    nodes_lvl_1 = [
        SimpleTreeNode(0, None),
        SimpleTreeNode(1, None),
    ]
    tree.AddChild(root, nodes_lvl_1[0])
    tree.AddChild(root, nodes_lvl_1[1])
    return nodes_lvl_1


@pytest.fixture(scope="function")
def nodes_lvl_2_1(tree, nodes_lvl_1):
    nodes_lvl_2_1 = [
        SimpleTreeNode(0, None),
        SimpleTreeNode(1, None)
    ]
    tree.AddChild(nodes_lvl_1[0], nodes_lvl_2_1[0])
    tree.AddChild(nodes_lvl_1[0], nodes_lvl_2_1[1])
    return nodes_lvl_2_1


@pytest.fixture(scope="function")
def nodes_lvl_2_2(tree, nodes_lvl_1):
    nodes_lvl_2_2 = [
        SimpleTreeNode(0, None),
        SimpleTreeNode(1, None)
    ]
    tree.AddChild(nodes_lvl_1[1], nodes_lvl_2_2[0])
    tree.AddChild(nodes_lvl_1[1], nodes_lvl_2_2[1])
    return nodes_lvl_2_2


def test_add_child():
    root = SimpleTreeNode(0, None)
    tree = SimpleTree(root)
    new_node = SimpleTreeNode(1, None)

    tree.AddChild(root, new_node)

    assert root.Children == [new_node]
    assert new_node.Parent == root


def test_delete_node():
    root = SimpleTreeNode(0, None)
    tree = SimpleTree(root)
    subroot_node = SimpleTreeNode(0, None)
    tree.AddChild(root, subroot_node)
    deletable_node = SimpleTreeNode(1, None)
    tree.AddChild(root, deletable_node)
    sub_nodes = [
        SimpleTreeNode(2, None),
        SimpleTreeNode(3, None),
    ]
    tree.AddChild(deletable_node, sub_nodes[0])
    tree.AddChild(deletable_node, sub_nodes[1])

    tree.DeleteNode(deletable_node)

    assert root.Children == [subroot_node]
    assert deletable_node.Parent is None


def test_get_all_nodes_if_tree_is_empty():
    tree = SimpleTree(None)
    
    assert tree.GetAllNodes() == []


def test_get_all_nodes_if_there_are_some_nodes(tree, root, nodes_lvl_1, nodes_lvl_2_1):
    expected_nodes = [root, *nodes_lvl_1, *nodes_lvl_2_1]

    all_nodes = tree.GetAllNodes()

    assert len(expected_nodes) == len(all_nodes)
    for node in expected_nodes:
        assert node in all_nodes


def test_find_nodes_by_value(tree, root, nodes_lvl_1, nodes_lvl_2_1):
    expected_nodes = [root, nodes_lvl_1[1], nodes_lvl_2_1[1]]
    found_nodes = tree.FindNodesByValue(1)

    assert len(expected_nodes) == len(found_nodes)
    for node in expected_nodes:
        assert node in found_nodes


def test_find_nodes_by_value_if_tree_is_empty():
    tree = SimpleTree(None)

    assert tree.FindNodesByValue(1) == []


def test_move_node(tree, root, nodes_lvl_1, nodes_lvl_2_1):
    tree.MoveNode(nodes_lvl_1[1], nodes_lvl_2_1[1])

    assert root.Children == [nodes_lvl_1[0]]
    assert nodes_lvl_2_1[1].Children == [nodes_lvl_1[1]]
    assert nodes_lvl_1[1].Parent == nodes_lvl_2_1[1]


def test_count(tree, root, nodes_lvl_1, nodes_lvl_2_1, nodes_lvl_2_2):
    assert tree.Count() == 7


def test_count_if_tree_is_empty():
    tree = SimpleTree(None)

    return tree.Count() == 0


def test_leaf_count(tree, root, nodes_lvl_1, nodes_lvl_2_1):
    assert tree.LeafCount() == 3


def test_leaf_count_if_tree_is_empty():
    tree = SimpleTree(None)

    assert tree.LeafCount() == 0


def test_enrich_levels(tree, root, nodes_lvl_1, nodes_lvl_2_1):
    enrich_levels(tree)
    
    assert root.Level == 0
    assert all(node.Level == 1 for node in nodes_lvl_1)
    assert all(node.Level == 2 for node in nodes_lvl_2_1)
