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
    assert new_node.Level == 1


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


@pytest.fixture
def even_example():
    node_1 = SimpleTreeNode(1, None)
    tree = SimpleTree(node_1)
    node_2 = SimpleTreeNode(2, None)
    tree.AddChild(node_1, node_2)
    node_3 = SimpleTreeNode(3, None)
    tree.AddChild(node_1, node_3)
    node_6 = SimpleTreeNode(6, None)
    tree.AddChild(node_1, node_6)
    node_5 = SimpleTreeNode(5, None)
    tree.AddChild(node_2, node_5)
    node_7 = SimpleTreeNode(7, None)
    tree.AddChild(node_2, node_7)
    node_4 = SimpleTreeNode(4, None)
    tree.AddChild(node_3, node_4)
    node_8 = SimpleTreeNode(8, None)
    tree.AddChild(node_6, node_8)
    node_9 = SimpleTreeNode(9, None)
    tree.AddChild(node_8, node_9)
    node_10 = SimpleTreeNode(10, None)
    tree.AddChild(node_8, node_10)
    nodes = [node_1, node_2, node_3, node_4, node_5, node_6, node_7, node_8, node_9, node_10]
    return tree, nodes


def assert_link_in(result, n1, n2):
    for i in range(len(result) - 1):
        if result[i] == n1 and result[i + 1] == n2:
            return
    raise AssertionError('Link is not in result')


def test_even_trees(even_example):
    tree, nodes = even_example

    result = tree.EvenTrees()

    assert_link_in(result, nodes[0], nodes[2])
    assert_link_in(result, nodes[0], nodes[5])


def test_even_tree_another(even_example):
    tree, nodes = even_example
    nodes.append(SimpleTreeNode(11, None))
    tree.AddChild(nodes[3], nodes[10])
    nodes.append(SimpleTreeNode(12, None))
    tree.AddChild(nodes[2], nodes[11])

    result = tree.EvenTrees()

    assert_link_in(result, nodes[0], nodes[2])
    assert_link_in(result, nodes[0], nodes[5])
    assert_link_in(result, nodes[2], nodes[3])
