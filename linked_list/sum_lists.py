from .linked_list import LinkedList, Node


class LengthsAreNotEqual(Exception):
    pass


def sum_lists(s_list1, s_list2):
    if s_list1.len() != s_list2.len():
        raise LengthsAreNotEqual

    result = LinkedList()

    node1 = s_list1.head
    node2 = s_list2.head
    while node1 is not None:
        result.add_in_tail(Node(node1.value + node2.value))
        node1 = node1.next
        node2 = node2.next
    
    return result
