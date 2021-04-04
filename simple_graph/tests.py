import pytest

from .simple_graph import SimpleGraph, Vertex


@pytest.fixture
def graph_2():
    graph = SimpleGraph(2)
    graph.vertex = [Vertex(1), Vertex(2)]
    return graph


@pytest.fixture
def graph():
    graph = SimpleGraph(10)
    graph.vertex[0] = Vertex(1)
    graph.vertex[1] = Vertex(2)
    graph.vertex[2] = Vertex(3)
    return graph


def test_is_edge_return_true_if_this_is_edge(graph_2):
    graph_2.m_adjacency = [
        [0, 1],
        [1, 0],
    ]
    
    assert graph_2.IsEdge(0, 1)


def test_is_edge_return_false_if_this_is_not_the_edge(graph_2):
    assert not graph_2.IsEdge(0, 1)


def graph_values(graph):
    return [vertex.Value for vertex in graph.vertex if vertex is not None]


def assert_no_edges(graph, vertex):
    i = graph.vertex.index(vertex)
    
    assert all(edge == 0 for edge in graph.m_adjacency[i])
    assert all(edge == 0 for edge in [v[i] for v in graph.m_adjacency])


def get_vertex_by_val(graph, v):
    for vertex in graph.vertex:
        if vertex.Value == v:
            return vertex


def test_add_vertex(graph):
    new_value = 4
    graph.AddVertex(new_value)

    assert new_value in graph_values(graph)
    assert_no_edges(graph, get_vertex_by_val(graph, new_value))


def test_add_edge(graph):
    assert not graph.IsEdge(0, 1)
    assert not graph.IsEdge(1, 0)

    graph.AddEdge(0, 1)

    assert graph.IsEdge(0, 1)
    assert graph.IsEdge(1, 0)


def test_remove_edge(graph_2):
    graph_2.m_adjacency = [
        [0, 1],
        [1, 0],
    ]

    assert graph_2.IsEdge(0, 1)
    assert graph_2.IsEdge(1, 0)

    graph_2.RemoveEdge(0, 1)

    assert not graph_2.IsEdge(0, 1)
    assert not graph_2.IsEdge(1, 0)


def test_remove_vertex(graph_2):
    graph_2.m_adjacency = [
        [0, 1],
        [1, 0],
    ]

    assert 2 in graph_values(graph_2)
    assert graph_2.IsEdge(0, 1)
    assert graph_2.IsEdge(1, 0)

    graph_2.RemoveVertex(1)

    assert 2 not in graph_values(graph_2)
    assert not graph_2.IsEdge(0, 1)
    assert not graph_2.IsEdge(1, 0)
