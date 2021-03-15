import pytest

from .linked_list2 import DummyNode, Node, LinkedListWithDummy


@pytest.fixture
def s_list():
    return LinkedListWithDummy()


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

    assert s_list.head.next == prev_node
    assert isinstance(prev_node.prev, DummyNode)
    assert prev_node.next == next_node
    assert s_list.tail.prev == next_node
    assert isinstance(next_node.next, DummyNode)
    assert next_node.prev == prev_node


def test_delete_if_node_is_in_the_head(s_list):
    deletable_node = Node(1)
    next_node = Node(2)
    tail = Node(3)
    s_list.add_in_tail(deletable_node)
    s_list.add_in_tail(next_node)
    s_list.add_in_tail(tail)

    s_list.delete(1)
    
    assert s_list.head.next == next_node
    assert isinstance(next_node.prev, DummyNode)
    assert next_node.next == tail
    assert s_list.tail.prev == tail


def test_delete_if_node_is_in_the_tail(s_list):
    head = Node(1)
    prev_node = Node(2)
    deletable_node = Node(3)
    s_list.add_in_tail(head)
    s_list.add_in_tail(prev_node)
    s_list.add_in_tail(deletable_node)

    s_list.delete(3)

    assert s_list.tail.prev == prev_node
    assert isinstance(prev_node.next, DummyNode)
    assert prev_node.prev == head
    assert s_list.head.next == head


def test_delete_if_there_is_only_one_node(s_list):
    node = Node(1)
    s_list.add_in_tail(node)

    s_list.delete(1)

    assert isinstance(s_list.head.next, DummyNode)
    assert isinstance(s_list.tail.prev, DummyNode)


def test_delete_only_one_if_there_are_several_right_nodes(s_list):
    right_nodes = [Node(1), Node(1)]
    s_list.add_in_tail(right_nodes[0])
    s_list.add_in_tail(right_nodes[1])

    s_list.delete(1)

    assert s_list.head.next == right_nodes[1]
    assert s_list.tail.prev == right_nodes[1]


def test_delete_if_there_are_no_right_nodes(s_list):
    head = Node(1)
    tail = Node(2)
    s_list.add_in_tail(head)
    s_list.add_in_tail(tail)

    s_list.delete(3)

    assert s_list.head.next == head
    assert s_list.tail.prev == tail


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

    assert isinstance(s_list.head, DummyNode)
    assert isinstance(s_list.tail, DummyNode)


def test_clean_if_list_has_no_nodes(s_list):
    s_list.clean()

    assert isinstance(s_list.head, DummyNode)
    assert isinstance(s_list.tail, DummyNode)


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

    assert s_list.head.next == node
    assert s_list.tail.prev == node
    assert isinstance(node.prev, DummyNode)
    assert isinstance(node.next, DummyNode)


def test_insert_if_after_node_is_None_and_list_is_not_empty(s_list):
    node = Node(1)
    s_list.insert(None, node)
    inserted = Node(2)

    s_list.insert(None, inserted)

    assert s_list.head.next == node
    assert s_list.tail.prev == inserted
    assert inserted.prev == node
    assert isinstance(inserted.next, DummyNode)
    assert node.next == inserted


def test_insert_if_after_node_in_the_middle(s_list):
    head = Node(1)
    after_node = Node(2)
    tail = Node(4)
    s_list.insert(None, head)
    s_list.insert(None, after_node)
    s_list.insert(None, tail)
    inserted = Node(3)

    s_list.insert(after_node, inserted)
    
    assert s_list.head.next == head
    assert s_list.tail.prev == tail
    assert after_node.next == inserted
    assert inserted.prev == after_node
    assert inserted.next == tail
    assert tail.prev == inserted


def test_insert_if_after_node_is_tail(s_list):
    head = Node(1)
    tail = Node(2)
    s_list.insert(None, head)
    s_list.insert(None, tail)
    inserted = Node(3)

    s_list.insert(tail, inserted)

    assert s_list.head.next == head
    assert s_list.tail.prev == inserted
    assert tail.next == inserted
    assert inserted.prev == tail
    assert isinstance(inserted.next, DummyNode)


def test_add_in_tail_if_list_is_empty(s_list):
    added = Node(1)

    s_list.add_in_tail(added)

    assert s_list.head.next == added
    assert s_list.tail.prev == added
    assert isinstance(added.next, DummyNode)
    assert isinstance(added.prev, DummyNode)


def test_add_in_tail_if_list_is_not_empty(s_list):
    head = Node(1)
    added = Node(2)
    s_list.insert(None, head)

    s_list.add_in_tail(added)

    assert s_list.head.next == head
    assert s_list.tail.prev == added
    assert added.prev == s_list.head.next
    assert isinstance(added.next, DummyNode)


def test_add_in_head_if_list_is_not_empty(s_list):
    head = Node(1)
    s_list.add_in_tail(head)
    added = Node(2)

    s_list.add_in_head(added)

    assert s_list.head.next == added
    assert added.next == head
    assert head.prev == added


def test_add_in_head_if_list_is_empty(s_list):
    added = Node(1)

    s_list.add_in_head(added)

    assert s_list.head.next == added
    assert s_list.tail.prev == added
    assert isinstance(added.prev, DummyNode)
    assert isinstance(added.next, DummyNode)
