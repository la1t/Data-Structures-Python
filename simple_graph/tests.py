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


def is_correct_route(graph, route):
    for i in range(len(route) - 1):
        origin = graph.get_index(route[i])
        dest = graph.get_index(route[i + 1])
        if not graph.IsEdge(origin, dest):
            return False
    return True


@pytest.fixture
def ds_graph():
    graph = SimpleGraph(9)
    graph.vertex = [Vertex(0) for _ in range(9)]
    graph.AddEdge(0, 1)
    graph.AddEdge(0, 2)
    graph.AddEdge(1, 5)
    graph.AddEdge(2, 3)
    graph.AddEdge(2, 5)
    graph.AddEdge(4, 5)
    graph.AddEdge(5, 7)
    graph.AddEdge(6, 7)
    graph.AddEdge(4, 6)
    return graph


@pytest.mark.parametrize(
    'route_indexes,is_correct',
    [
        ([0, 2, 5, 4], True),
        ([3, 2, 0, 1], True),
        ([3, 5, 4, 6], False),
    ]
)
def test_is_correct_route(ds_graph, route_indexes, is_correct):
    route = [ds_graph.vertex[i] for i in route_indexes]
    assert is_correct_route(ds_graph, route) == is_correct


@pytest.mark.parametrize(
    'vertex,edge_vertices', [
        (0, {1, 2}),
        (2, {0, 5, 3}),
    ]
)
def test_get_edges(ds_graph, vertex, edge_vertices):
    assert ds_graph.get_edges(vertex) == edge_vertices


@pytest.mark.parametrize(
    'v_from,v_to,route_exists',
    [
        (0, 7, True),
        (3, 1, True),
        (2, 6, True),
        (0, 8, False),
    ]
)
def test_depth_first_search(ds_graph, v_from, v_to, route_exists):
    route = ds_graph.DepthFirstSearch(v_from, v_to)

    if route_exists:
        assert route
        assert is_correct_route(ds_graph, route)
    else:
        assert not route


def test_depth_first_search_if_v_from_equals_v_to(ds_graph):
    route = ds_graph.DepthFirstSearch(0, 0)
    
    assert route != []
    assert is_correct_route(ds_graph, route)
    assert route != [0, 0]


@pytest.mark.parametrize(
    'v_from,v_to,route_exists',
    [
        (0, 7, True),
        (3, 1, True),
        (2, 6, True),
        (0, 8, False),
    ]
)
def test_breadth_first_search(ds_graph, v_from, v_to, route_exists):
    route = ds_graph.BreadthFirstSearch(v_from, v_to)

    if route_exists:
        assert route
        assert route[0] == ds_graph.vertex[v_from]
        assert route[-1] == ds_graph.vertex[v_to]
        assert is_correct_route(ds_graph, route)
    else:
        assert not route
