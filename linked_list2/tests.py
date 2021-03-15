import pytest

from .linked_list2 import Node, LinkedList2


@pytest.fixture
def s_list():
    return LinkedList2()


def test_find_if_node_is_exist(s_list):
    expected_node = Node(2)
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(expected_node)

    found_node = s_list.find(2)

    assert found_node == expected_node


def test_find_if_node_is_not_exist(s_list):
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(2))
    
    assert s_list.find(3) is None


def test_find_if_list_is_empty(s_list):
    assert s_list.find(1) is None


def test_find_all_if_there_are_several_nodes(s_list):
    expected_nodes = [Node(2), Node(2)]
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(expected_nodes[0])
    s_list.add_in_tail(Node(3))
    s_list.add_in_tail(expected_nodes[1])

    found_nodes = s_list.find_all(2)

    assert found_nodes == expected_nodes


def test_find_all_if_there_are_no_right_nodes(s_list):
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(2))

    assert s_list.find_all(3) == []


def test_find_all_if_list_is_empty(s_list):
    assert s_list.find_all(1) == []


def test_delete_if_node_is_in_the_middle(s_list):
    prev_node = Node(1)
    deletable_node = Node(2)
    next_node = Node(3)
    s_list.add_in_tail(prev_node)
    s_list.add_in_tail(deletable_node)
    s_list.add_in_tail(next_node)

    s_list.delete(2)

    assert s_list.head == prev_node
    assert prev_node.prev is None
    assert prev_node.next == next_node
    assert s_list.tail == next_node
    assert next_node.next is None
    assert next_node.prev == prev_node


def test_delete_if_node_is_in_the_head(s_list):
    deletable_node = Node(1)
    next_node = Node(2)
    tail = Node(3)
    s_list.add_in_tail(deletable_node)
    s_list.add_in_tail(next_node)
    s_list.add_in_tail(tail)

    s_list.delete(1)
    
    assert s_list.head == next_node
    assert next_node.prev is None
    assert next_node.next == tail
    assert s_list.tail == tail


def test_delete_if_node_is_in_the_tail(s_list):
    head = Node(1)
    prev_node = Node(2)
    deletable_node = Node(3)
    s_list.add_in_tail(head)
    s_list.add_in_tail(prev_node)
    s_list.add_in_tail(deletable_node)

    s_list.delete(3)

    assert s_list.tail == prev_node
    assert prev_node.next is None
    assert prev_node.prev == head
    assert s_list.head == head


def test_delete_if_there_is_only_one_node(s_list):
    node = Node(1)
    s_list.add_in_tail(node)

    s_list.delete(1)

    assert s_list.head is None
    assert s_list.tail is None


def test_delete_only_one_if_there_are_several_right_nodes(s_list):
    right_nodes = [Node(1), Node(1)]
    s_list.add_in_tail(right_nodes[0])
    s_list.add_in_tail(right_nodes[1])

    s_list.delete(1)

    assert s_list.head == right_nodes[1]
    assert s_list.tail == right_nodes[1]


def test_delete_if_there_are_no_right_nodes(s_list):
    head = Node(1)
    tail = Node(2)
    s_list.add_in_tail(head)
    s_list.add_in_tail(tail)

    s_list.delete(3)

    assert s_list.head == head
    assert s_list.tail == tail


def test_delete_all(s_list):
    prev_node = Node(1)
    deletable_nodes = [Node(2), Node(2)]
    next_node = Node(3)
    s_list.add_in_tail(prev_node)
    s_list.add_in_tail(deletable_nodes[0])
    s_list.add_in_tail(deletable_nodes[1])
    s_list.add_in_tail(next_node)

    s_list.delete(2, all=True)

    assert prev_node.next == next_node
    assert next_node.prev == prev_node


def test_clean_if_list_has_some_nodes(s_list):
    head = Node(1)
    tail = Node(2)
    s_list.add_in_tail(head)
    s_list.add_in_tail(tail)

    s_list.clean()

    assert s_list.head is None
    assert s_list.tail is None


def test_clean_if_list_has_no_nodes(s_list):
    s_list.clean()

    assert s_list.head is None
    assert s_list.tail is None 


def test_len_if_list_has_some_nodes(s_list):
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(2))
    s_list.add_in_tail(Node(3))

    assert s_list.len() == 3


def test_len_if_list_has_only_one_node(s_list):
    s_list.add_in_tail(Node(1))

    assert s_list.len() == 1


def test_len_if_list_is_empty(s_list):
    assert s_list.len() == 0


def test_insert_if_after_node_is_None_and_list_is_empty(s_list):
    node = Node(1)

    s_list.insert(None, node)

    assert s_list.head == node
    assert s_list.tail == node
    assert node.prev is None
    assert node.next is None


def test_insert_if_after_node_is_None_and_list_is_not_empty(s_list):
    head = Node(1)
    tail = Node(2)
    s_list.add_in_tail(head)
    s_list.add_in_tail(tail)
    inserted = Node(3)

    s_list.insert(None, inserted)

    assert s_list.head == inserted
    assert s_list.tail == tail
    assert inserted.prev is None
    assert inserted.next == head
    assert head.prev == inserted


def test_insert_if_after_node_in_the_middle(s_list):
    head = Node(1)
    after_node = Node(2)
    tail = Node(4)
    s_list.add_in_tail(head)
    s_list.add_in_tail(after_node)
    s_list.add_in_tail(tail)
    inserted = Node(3)

    s_list.insert(after_node, inserted)
    
    assert s_list.head == head
    assert s_list.tail == tail
    assert after_node.next == inserted
    assert inserted.prev == after_node
    assert inserted.next == tail
    assert tail.prev == inserted


def test_insert_if_after_node_is_tail(s_list):
    head = Node(1)
    tail = Node(2)
    s_list.add_in_tail(head)
    s_list.add_in_tail(tail)
    inserted = Node(3)

    s_list.insert(tail, inserted)

    assert s_list.head == head
    assert s_list.tail == inserted
    assert tail.next == inserted
    assert inserted.prev == tail
    assert inserted.next is None


def test_add_in_head_if_list_is_not_empty(s_list):
    head = Node(1)
    s_list.add_in_tail(head)
    added = Node(2)

    s_list.add_in_head(added)

    assert s_list.head == added
    assert added.next == head
    assert head.prev == added


def test_add_in_head_if_list_is_empty(s_list):
    added = Node(1)

    s_list.add_in_head(added)

    assert s_list.head == added
    assert s_list.tail == added
    assert added.prev is None
    assert added.next is None
