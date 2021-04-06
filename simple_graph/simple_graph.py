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
        stack = []
        current_item = VFrom
        self.visit(current_item)
        stack.append(current_item)
        while stack:
            if self.IsEdge(current_item, VTo):
                self.visit(VTo)
                stack.append(VTo)
                return stack
            unvisitted_vertices = [v for v in self.get_edges(current_item) if not self.is_visited(v)]
            if unvisitted_vertices:
                current_item = unvisitted_vertices[0]
                self.visit(current_item)
                stack.append(current_item)
                continue
            stack.pop()
        return stack
    
    def get_edges(self, v):
        return {v2 for v2 in range(self.max_vertex) if self.m_adjacency[v][v2] == 1}
    
    def visit(self, v):
        self.vertex[v].Hit = True
    
    def is_visited(self, v):
        return self.vertex[v].Hit
