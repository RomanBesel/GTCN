import base_graph
from base_graph import BaseGraph
import numpy as np

class Graph(BaseGraph):

    # allows loops and multiple edges between nodes

    def __init__(self, nod: list, edg: list):
        super().__init__(nod, edg)
    
    def construct_adjacency_matrix(self) -> np.array:
        array = np.zeros((len(self.nodes), len(self.nodes)))
        for edge in self.edges:
            array[edge] += 1
            if edge[0] != edge[1]:
                array[tuple(reversed(edge))] += 1 # only in undirected graph due to symmetry
            else: pass
        return array

    def construct_incidence_matrix(self):
        edges = sorted(set(self.edges))
        array = np.zeros((len(self.nodes), len(edges)))
        for edge, edge_pos in zip(edges, range(len(edges))):
            array[edge[0], edge_pos] += self.edges.count(edge)
            if edge[0] != edge[1]:
                array[edge[1], edge_pos] += self.edges.count(edge)
            else: pass
        return array


class SimpleGraph(BaseGraph):

    # loops and multiple edges between two nodes are not allowed

    def __init__(self, nod: list, edg: list):
        super().__init__(nod, edg)
        self.laplacian_matrix = self.construct_laplacian_matrix()

    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, edges: list):
        edg = [e for e  in edges if e[0] != e[1]]
        edg = set(sorted(edg, key=lambda e:( e[0], e[1])))
        self._edges = edg

    def construct_adjacency_matrix(self) -> np.array:
        array = np.zeros((len(self.nodes), len(self.nodes)))
        for edge in self.edges:
            array[edge] = 1 
            array[tuple(reversed(edge))] = 1 # only in undirected graph due to symmetry
        return array

    def construct_incidence_matrix(self):
        array = np.zeros((len(self.nodes), len(self.edges)))
        for edge, edge_pos in zip(self.edges, range(len(self.edges))):
            array[edge[0], edge_pos] = 1
            array[edge[1], edge_pos] = 1
        return array

    def construct_laplacian_matrix(self):
        return np.subtract(self.adjacency_matrix, self.degree_matrix)

    