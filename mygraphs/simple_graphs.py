import base_graph
from base_graph import BaseGraph
import numpy as np


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
        self_loops = [e for e  in edges if e[0] == e[1]]
        unique_edges = set(edges) # get unique edges in edge list
        if (len(edges) != len(unique_edges)) or (len(self_loops) != 0): # look if conditions (no self loops and no multiple edges) of simple graph are fulfilled
            raise ValueError('One or both of the conditions for a simple graph are violated in the data passed. Please remove edges until you meet the criterion for a Simple Graph.')
        else: 
            edg = set(sorted(edg, key=lambda e:(e[0], e[1])))
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


class SimpleDirectedGraph(SimpleGraph):

    # edges are arcs and have a direction (a, b) : a -> b
    # loops and mutiple edges with the same direction between the same nodes are not allowed

    def __init__(self, nod: list, edg: list):
        super().__init__(nod, edg)
        self.in_degree_matrix = self.get_in_degree_matrix()
        self.out_degree_matrix = self.get_out_degree_matrix()
        self.in_degree_laplacian = self.get_in_degree_laplacian()
        self.out_degree_laplacian = self.get_out_degree_laplacian()
        
    def construct_adjacency_matrix(self) -> np.array:
        array = np.zeros((len(self.nodes), len(self.nodes)))
        for edge in self.edges:
            array[edge] = 1 
        return array

    def construct_incidence_matrix(self) -> np.array:
        array = np.zeros((len(self.nodes), len(self.edges)))
        for edge, edge_pos in zip(self.edges, range(len(self.edges))):
            array[edge[0], edge_pos] = -1 # (a, b) denotes arc a -> b, while (b, a) denotes  arc b -> a
            array[edge[1], edge_pos] = 1 # a : -1 -> b: 1
        return array
    
    def construct_degree_matrix(self) -> dict:
        degree_dict = {}
        degree_dict['in'] = self.get_in_degree_matrix()
        degree_dict['out'] = self.get_out_degree_matrix()
        return degree_dict

    def get_in_degree_matrix(self) -> np.array:
        array = np.zeros((len(self.nodes), len(self.nodes)))
        sums_col = np.sum(self.adjacency_matrix, 0)
        for i in range(len(self.nodes)):
            array[(i, i)] = sums_col[i]
        return array

    def get_out_degree_matrix(self) -> np.array:
        array = np.zeros((len(self.nodes), len(self.nodes)))
        sums_row = np.sum(self.adjacency_matrix, 1)
        for i in range(len(self.nodes)):
            array[(i, i)] = sums_row[i]
        return array

    def construct_laplacian_matrix(self) -> dict:
        laplacian_dict = {}
        laplacian_dict['in'] = self.get_in_degree_laplacian()
        laplacian_dict['out'] = self.get_out_degree_laplacian()
        return laplacian_dict

    def get_in_degree_laplacian(self) -> np.array:
        return np.subtract(self.degree_matrix['in'], self.adjacency_matrix)

    def get_out_degree_laplacian(self) -> np.array:
        return np.subtract(self.degree_matrix['out'], self.adjacency_matrix)

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
        self_loops = [e for e  in edges if e[0][0] == e[0][1]]
        edge_tuple = [e[0] for e in edges] 
        unique_edges = set(edge_tuple) # get unique edges in edge list
        if (len(edge_tuple) != len(unique_edges)) or (len(self_loops) != 0): # look if conditions (no self loops and no multiple edges) of simple graph are fulfilled
            raise ValueError('One or both of the conditions for a simple graph are violated in the data passed. Please remove edges until you meet the criterion for a Simple Graph.')
        else: 
            edg = sorted(edges, key=lambda e: e[0])
            self._edges = edg

    def construct_adjacency_matrix(self) -> np.array:
        array = np.zeros((len(self.nodes), len(self.nodes)))
        for edge in self.edges:
            array[edge[0]] = edge[1] # instead of 1 here the weight is set as value
            array[tuple(reversed(edge[0]))] = edge[1] # same as above
        return array

    # The incidence matrix must be built differently compared to the other graphs:
    # instead of 1 the weights of the edges are set in the matrix

    def construct_incidence_matrix(self):
        array = np.zeros((len(self.nodes), len(self.edges)))
        for edge, edge_pos in zip(self.edges, range(len(self.edges))):
            array[edge[0][0], edge_pos] = edge[1]
            array[edge[0][1], edge_pos] = edge[1]
        return array
    
class SimpleDirectedWeightedGraph(SimpleGraph):

    # edges are arcs and have a direction (a, b) : a -> b
    # edges have weights i.e. for all e in E: e -> R^n 
    # loops and mutiple edges with the same direction between the same nodes are not allowed

    def __init__(self, nod: list, edg: list):
        super().__init__(nod, edg)
        self.in_degree_matrix = self.get_in_degree_matrix()
        self.out_degree_matrix = self.get_out_degree_matrix()
        self.in_degree_laplacian = self.get_in_degree_laplacian()
        self.out_degree_laplacian = self.get_out_degree_laplacian()

    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, edges: list):
        self_loops = [e for e  in edges if e[0][0] == e[0][1]]
        edge_tuple = [e[0] for e in edges] 
        unique_edges = set(edge_tuple) # get unique edges in edge list
        if (len(edge_tuple) != len(unique_edges)) or (len(self_loops) != 0): # look if conditions (no self loops and no multiple edges) of simple graph are fulfilled
            raise ValueError('One or both of the conditions for a simple graph are violated in the data passed. Please remove edges until you meet the criterion for a Simple Graph.')
        else: 
            edg = sorted(edges, key=lambda e: e[0])
            self._edges = edg
        
    def construct_adjacency_matrix(self) -> np.array:
        array = np.zeros((len(self.nodes), len(self.nodes)))
        for edge in self.edges:
            array[edge[0]] = edge[1] 
        return array

    def construct_incidence_matrix(self) -> np.array:
        array = np.zeros((len(self.nodes), len(self.edges)))
        for edge, edge_pos in zip(self.edges, range(len(self.edges))):
            array[edge[0][0], edge_pos] = -1 * edge[1] # (a, b) denotes arc a -> b, while (b, a) denotes  arc b -> a
            array[edge[0][1], edge_pos] = 1 * edge[1] # a : -1 -> b: 1
        return array
    
    def construct_degree_matrix(self) -> dict:
        degree_dict = {}
        degree_dict['in'] = self.get_in_degree_matrix()
        degree_dict['out'] = self.get_out_degree_matrix()
        return degree_dict

    def get_in_degree_matrix(self) -> np.array:
        array = np.zeros((len(self.nodes), len(self.nodes)))
        sums_col = np.sum(self.adjacency_matrix, 0)
        for i in range(len(self.nodes)):
            array[(i, i)] = sums_col[i]
        return array

    def get_out_degree_matrix(self) -> np.array:
        array = np.zeros((len(self.nodes), len(self.nodes)))
        sums_row = np.sum(self.adjacency_matrix, 1)
        for i in range(len(self.nodes)):
            array[(i, i)] = sums_row[i]
        return array

    def construct_laplacian_matrix(self) -> dict:
        laplacian_dict = {}
        laplacian_dict['in'] = self.get_in_degree_laplacian()
        laplacian_dict['out'] = self.get_out_degree_laplacian()
        return laplacian_dict

    def get_in_degree_laplacian(self) -> np.array:
        return np.subtract(self.degree_matrix['in'], self.adjacency_matrix)

    def get_out_degree_laplacian(self) -> np.array:
        return np.subtract(self.degree_matrix['out'], self.adjacency_matrix)