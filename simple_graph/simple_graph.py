class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False
  
class SimpleGraph:
	
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        
    def AddVertex(self, v):
        free_index = self.vertex.index(None)
        self.vertex[free_index] = Vertex(v)
	
    # здесь и далее, параметры v -- индекс вершины
    # в списке  vertex
    def RemoveVertex(self, v):
        self.vertex[v] = None
        for i in range(0, self.max_vertex):
            self.m_adjacency[i][v] = 0
            self.m_adjacency[v][i] = 0
	
    def IsEdge(self, v1, v2):
        return self.m_adjacency[v1][v2] == 1
	
    def AddEdge(self, v1, v2):
        # добавление ребра между вершинами v1 и v2
        self.m_adjacency[v1][v2] = self.m_adjacency[v2][v1] = 1
	
    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        self.m_adjacency[v1][v2] = self.m_adjacency[v2][v1] = 0
    
    def DepthFirstSearch(self, VFrom, VTo):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
        self.clear_vertices()
        stack = []
        current_vertex = VFrom
        while True:
            self.visit(current_vertex)
            stack.append(current_vertex)
            if self.IsEdge(current_vertex, VTo):
                self.visit(VTo)
                stack.append(VTo)
                return [self.vertex[v] for v in stack]
            unvisitted_vertices = self.get_unvisited_edges(current_vertex)
            if unvisitted_vertices:
                current_vertex = unvisitted_vertices[0]
                continue
            stack.pop()
            if stack:
                current_vertex = stack.pop()
                continue
            else:
                return []
    
    def BreadthFirstSearch(self, VFrom, VTo):
        # сохранение пути:
        # - сохранять вместо вершин полный путь до этой вершины
        # - держать отдельно словарь со всеми возможными путями
        # я выберу второй вариант, потому что он более дешевый по памяти (не придется по нескольку
        # раз хранить путь до одной вершины)
        self.clear_vertices()
        queue = []

        # словарь, где ключ - вершина, в которую надо попасть, а значение —
        # вершина, из которой нужно выдвигаться
        routing = {}

        current_vertex = VFrom
        self.visit(VFrom)
        while True:
            for vertex in self.get_unvisited_edges(current_vertex):
                self.visit(vertex)
                routing[vertex] = current_vertex
                if vertex == VTo:
                    return self.build_route(routing, VFrom, VTo)
                queue.append(vertex)
            if queue:
                current_vertex = queue.pop(0)
                continue
            return []
    
    def get_edges(self, v):
        return {v2 for v2 in range(self.max_vertex) if self.m_adjacency[v][v2] == 1}
    
    def get_unvisited_edges(self, v):
        return [v for v in self.get_edges(v) if not self.is_visited(v)]
    
    def visit(self, v):
        self.vertex[v].Hit = True
    
    def is_visited(self, v):
        return self.vertex[v].Hit
    
    def clear_vertices(self):
        for vertex in self.vertex:
            if vertex is not None:
                vertex.Hit = False
    
    def build_route(self, routing, v_from, v_to):
        current_vertex = v_to
        route_indexes = [current_vertex]
        while current_vertex != v_from:
            current_vertex = routing[current_vertex]
            route_indexes.append(current_vertex)
        return [self.vertex[i] for i in reversed(route_indexes)]
    
    def get_index(self, vertex):
        return self.vertex.index(vertex)
