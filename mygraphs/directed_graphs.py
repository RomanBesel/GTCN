from standard_graphs import SimpleGraph, Graph
import base_graph
from base_graph import BaseGraph
import numpy as np


class DirectedGraph(Graph):

    # edges are arcs and have a direction (a, b) : a -> b

    def __init__(self, nod: list, edg: list):
        super().__init__(nod, edg)
        self.in_degree_matrix = self.get_in_degree_matrix()
        self.out_degree_matrix = self.get_out_degree_matrix()

    def construct_adjacency_matrix(self) -> np.array:
        array = np.zeros((len(self.nodes), len(self.nodes)))
        for edge in self.edges:
            array[edge] = 1 
        return array

    def construct_incidence_matrix(self) -> np.array:
        array = np.zeros((len(self.nodes), len(self.edges)))
        for edge, edge_pos in zip(self.edges, range(len(self.edges))):
            if edge[0] != edge[1]:
                array[edge[0], edge_pos] = -1
                array[edge[1], edge_pos] = 1 # (a, b) denotes arc a -> b, while (b, a) denotes  arc b -> a
            else: array[edge[0], edge_pos] = 2
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

