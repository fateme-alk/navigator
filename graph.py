from vertex import Vertex
from edge import Edge


class Graph:
    def __init__(self):
        self._adj_list = {} 


    @property
    def adj_list(self):
        return self._adj_list


    def add_vertex(self, name, coordinate):
        v = Vertex(name, coordinate)
        self.adj_list[v] = []
        return v

    
    def add_edge(self, end_p1, end_p2):
        e = Edge(end_p1, end_p2)
        self.adj_list[end_p1].append({
            'adjacent_vertex': end_p2,
            'weight': e.weight
        })
        self.adj_list[end_p2].append({
            'adjacent_vertex': end_p1,
            'weight': e.weight
        })


    def vertex_exists(self, vertex):
        if vertex in self.adj_list:
            return True
        else:
            return False
        
