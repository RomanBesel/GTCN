import numpy as np

class BaseGraph():

    def __init__(self, nodes: list, edges: list):
        self.nodes = set(sorted(nodes))
        self.edges = edges
        self.adjacency_matrix = self.construct_adjacency_matrix()
        self.incidence_matrix = self.construct_incidence_matrix()
        self.degree_matrix = self.construct_degree_matrix()

    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, edges: list):
        edg = sorted(edges, key=lambda e:( e[0], e[1]))
        self._edges = edg
    
    def construct_adjacency_matrix(self) -> np.array:
        array = np.zeros((len(self.nodes), len(self.nodes)))
        return array

    def construct_incidence_matrix(self):
        array = np.zeros((len(self.nodes), len(self.edges)))
        return array

    def construct_degree_matrix(self):
        array = np.zeros((len(self.nodes), len(self.nodes)))
        sums_row = np.sum(self.adjacency_matrix, 1)
        for i in range(len(self.nodes)):
            array[(i, i)] = sums_row[i]
        return array

    

