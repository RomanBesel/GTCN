import numpy as np
from base_graph import BaseGraph
import base_graph
from standard_graphs import Graph, SimpleGraph

class WeightedGraph(Graph):

    # edges have weights i.e. for all e in E: e -> R^n 
    # undirected; edges have format ((a, b), [x]) with edge e incident to nodes a, b and where [x] represents an n-dimensional list of weights (here n=1)
    # subclass with negative weights not allowed should be implemented

    def __init__(self, nod: list, edg: list):
        super().__init__(nod, edg)

    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, edges: list):
        edg = sorted(edges, key=lambda e: e[0])
        self._edges = edg

    def construct_adjacency_matrix(self) -> np.array:
        array = np.zeros((len(self.nodes), len(self.nodes)))
        for edge in self.edges:
            array[edge[0]] = edge[1] # instead of 1 here the weight is set as value
            array[tuple(reversed(edge[0]))] = edge[1] # same as above
        return array

    # The incidence matrix must be built differently compared to the other graphs:
    # for multiple edges (a, b) -> each gets their own column
    # instead of 1 the weights of the edges are set in the matrix

    def construct_incidence_matrix(self):
        array = np.zeros((len(self.nodes), len(self.edges)))
        for edge, edge_pos in zip(self.edges, range(len(self.edges))):
            array[edge[0][0], edge_pos] = edge[1]
            array[edge[0][1], edge_pos] = edge[1]
        return array

    def construct_degree_matrix(self):
        adj_array, array = np.zeros((len(self.nodes), len(self.nodes))), np.zeros((len(self.nodes), len(self.nodes)))
        for edge in self.edges:
            adj_array[edge[0]] = 1 # instead of 1 here the weight is set as value
            adj_array[tuple(reversed(edge[0]))] = 1 # same as above
        sums_row = np.sum(adj_array, 1)
        for i in range(len(self.nodes)):
            array[(i, i)] = sums_row[i]
        return array

class SimpleWeightedGraph(SimpleGraph):

    # edges have weights i.e. for all e in E: e -> R^n 
    # undirected; edges have format ((a, b), [x]) with edge e incident to nodes a, b and where [x] represents an n-dimensional list of weights (here n=1)
    # subclass with negative weights not allowed should be implemented

    def __init__(self, nod: list, edg: list):
        super().__init__(nod, edg)

    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, edges: list):
        edges_loops_removed = [e for e  in edges if e[0][0] != e[0][1]]
        edges_tuple = [e[0] for e in edges_loops_removed] 
        unique_edges = set(edges_tuple) # get unique edges in edge list
        multiple_edges = [e for e in edges_tuple if edges_tuple.count(e) >= 2]
        if multiple_edges != []:
            raise ValueError('There exist multiple edges incident to the same nodes in the data you provided. Please remove edges until you meet the criterion for a Simple Graph.')
        else: 
            edg = sorted(edges_loops_removed, key=lambda e: e[0])
            self._edges = edg

    def construct_adjacency_matrix(self) -> np.array:
        array = np.zeros((len(self.nodes), len(self.nodes)))
        for edge in self.edges:
            array[edge[0]] = edge[1] # instead of 1 here the weight is set as value
            array[tuple(reversed(edge[0]))] = edge[1] # same as above
        return array

    # The incidence matrix must be built differently compared to the other graphs:
    # for multiple edges (a, b) -> each gets their own column
    # instead of 1 the weights of the edges are set in the matrix

    def construct_incidence_matrix(self):
        array = np.zeros((len(self.nodes), len(self.edges)))
        for edge, edge_pos in zip(self.edges, range(len(self.edges))):
            array[edge[0][0], edge_pos] = edge[1]
            array[edge[0][1], edge_pos] = edge[1]
        return array

    def construct_degree_matrix(self):
        adj_array, array = np.zeros((len(self.nodes), len(self.nodes))), np.zeros((len(self.nodes), len(self.nodes)))
        for edge in self.edges:
            adj_array[edge[0]] = 1 # instead of 1 here the weight is set as value
            adj_array[tuple(reversed(edge[0]))] = 1 # same as above
        sums_row = np.sum(adj_array, 1)
        for i in range(len(self.nodes)):
            array[(i, i)] = sums_row[i]
        return array

    def construct_laplacian_matrix(self):
        adj_array, array = np.zeros((len(self.nodes), len(self.nodes))), np.zeros((len(self.nodes), len(self.nodes)))
        for edge in self.edges:
            adj_array[edge[0]] = 1 # instead of 1 here the weight is set as value
            adj_array[tuple(reversed(edge[0]))] = 1 # same as above
        array = np.subtract(adj_array, self.degree_matrix)
        return array
        