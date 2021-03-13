import pytest

from .linked_list import LinkedList, Node


@pytest.fixture
def s_list():
    return LinkedList()

def test_delete_one_node_if_found_node_is_in_middle(s_list):
    head = Node(1)
    before_delete = Node(2)
    deletable_node = Node(3)
    after_delete = Node(4)
    tail = Node(5)
    s_list.add_in_tail(head)
    s_list.add_in_tail(before_delete)
    s_list.add_in_tail(deletable_node)
    s_list.add_in_tail(after_delete)
    s_list.add_in_tail(tail)

    s_list.delete(3)

    assert before_delete.next == after_delete
    assert s_list.head == head
    assert s_list.tail == tail


def test_delete_one_node_if_found_node_is_head(s_list):
    after_delete = Node(2)
    deletable_node = Node(1)
    tail = Node(3)
    s_list.add_in_tail(deletable_node)
    s_list.add_in_tail(after_delete)
    s_list.add_in_tail(tail)
    
    s_list.delete(1)

    assert s_list.head == after_delete
    assert s_list.tail == tail


def test_delete_one_node_if_found_node_is_tail(s_list):
    before_delete = Node(2)
    deletable_node = Node(3)
    head = Node(1)
    s_list.add_in_tail(head)
    s_list.add_in_tail(before_delete)
    s_list.add_in_tail(deletable_node)

    s_list.delete(3)

    assert before_delete.next is None
    assert s_list.tail == before_delete
    assert s_list.head == head


def test_delete_one_node_if_s_list_has_only_one_node(s_list):
    deletable_node = Node(1)
    s_list.add_in_tail(deletable_node)

    s_list.delete(1)

    assert s_list.tail is None
    assert s_list.head is None


def test_delete_one_node_if_node_is_not_found(s_list):
    the_one_node = Node(1)
    s_list.add_in_tail(the_one_node)

    s_list.delete(1000000)

    assert s_list.head == the_one_node
    assert s_list.tail == the_one_node

def test_delete_only_one_if_these_are_several_found_nodes(s_list):
    head = Node(1)
    before_deletable = Node(2)
    deletable = Node(3)
    after_deletable = Node(3)
    tail = Node(4)
    s_list.add_in_tail(head)
    s_list.add_in_tail(before_deletable)
    s_list.add_in_tail(deletable)
    s_list.add_in_tail(after_deletable)
    s_list.add_in_tail(tail)

    s_list.delete(3)

    assert before_deletable.next == after_deletable
    assert s_list.head == head
    assert s_list.tail == tail


def test_delete_all_if_all_of_these_in_the_middle(s_list):
    head = Node(1)
    before_deletables = Node(2)
    deletables = (Node(3), Node(3))
    after_deletables = Node(4)
    tail = Node(5)
    s_list.add_in_tail(head)
    s_list.add_in_tail(before_deletables)
    s_list.add_in_tail(deletables[0])
    s_list.add_in_tail(deletables[1])
    s_list.add_in_tail(after_deletables)
    s_list.add_in_tail(tail)

    s_list.delete(3, all=True)

    assert before_deletables.next == after_deletables
    assert s_list.head == head
    assert s_list.tail == tail

def test_delete_all_if_all_nodes_are_found(s_list):
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(1))

    s_list.delete(1, all=True)

    assert s_list.head is None
    assert s_list.tail is None


def test_clean_if_list_is_not_empty(s_list):
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(2))
    s_list.add_in_tail(Node(3))

    s_list.clean()

    assert s_list.head is None
    assert s_list.tail is None


def test_clean_if_list_is_not_empty(s_list):
    s_list.clean()

    assert s_list.head is None
    assert s_list.tail is None


def test_find_all_if_several_nodes_are_found(s_list):
    expected_nodes = [Node(1), Node(1)]
    
    s_list.add_in_tail(Node(2))
    s_list.add_in_tail(expected_nodes[0])
    s_list.add_in_tail(Node(2))
    s_list.add_in_tail(expected_nodes[1])

    found_nodes = s_list.find_all(1)

    assert found_nodes == expected_nodes


def test_find_all_if_one_node_is_found(s_list):
    expected_nodes = [Node(1)]

    s_list.add_in_tail(expected_nodes[0])

    found_nodes = s_list.find_all(1)

    assert found_nodes == expected_nodes


def test_find_all_if_nodes_are_not_found(s_list):
    assert s_list.find_all(1) == []


def test_len_if_list_has_several_nodes(s_list):
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(2))
    s_list.add_in_tail(Node(3))

    assert s_list.len() == 3


def test_len_if_list_has_only_one_node(s_list):
    s_list.add_in_tail(Node(1))

    assert s_list.len() == 1


def test_len_if_list_has_no_nodes(s_list):
    assert s_list.len() == 0


def test_insert_in_the_middle(s_list):
    head = Node(1)
    after_node = Node(2)
    before_node = Node(4)
    tail = Node(5)
    s_list.add_in_tail(head)
    s_list.add_in_tail(after_node)
    s_list.add_in_tail(before_node)
    s_list.add_in_tail(tail)
    new_node = Node(3)

    s_list.insert(after_node, new_node)

    assert after_node.next == new_node
    assert new_node.next == before_node
    assert s_list.head == head
    assert s_list.tail == tail


def test_insert_after_tail(s_list):
    head = Node(1)
    after_node = Node(2)
    s_list.add_in_tail(head)
    s_list.add_in_tail(after_node)
    new_node = Node(3)

    s_list.insert(after_node, new_node)

    assert after_node.next == new_node
    assert new_node.next is None
    assert s_list.tail == new_node
    assert s_list.head == head


def test_insert_as_a_head_if_list_is_not_empty(s_list):
    head = Node(2)
    s_list.add_in_tail(head)
    new_node = Node(1)

    s_list.insert(None, new_node)

    assert new_node.next == head
    assert head.next is None
    assert s_list.head == new_node
    assert s_list.tail == head


def test_insert_as_a_head_if_list_is_empty(s_list):
    new_node = Node(1)

    s_list.insert(None, new_node)

    assert new_node.next is None
    assert s_list.head == new_node
    assert s_list.tail == new_node
