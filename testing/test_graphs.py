from weighted_graphs import WeightedGraph
from directed_graphs import DirectedGraph
from standard_graphs import SimpleGraph
from base_graph import BaseGraph
from utility.graph_generator import RandomGraphFactory, GraphFactory
from itertools import chain, combinations
import numpy as np

class GraphTest():

    def __init__(self):
        self.factory = GraphFactory()
        self.test_data = {}

    # generate some test data with which to check the characteristics the graphs have top obey (i.e simple having no loops and multiple edges...)
    def generate_test_graphs(self, number_graphs: int = 10):
        for key in self.test_data:
            g = self.factory.generate_graph(self.test_data[key][0], self.test_data[1], key[0], key[1], key[2])
            self.test_graph_properties(g, self.test_data[1], key[0], key[1], key[2])

    def load_test_data():
        pass
    
    def test_graph_properties(self, g: BaseGraph, simple: str, directed: str, weighted: str):
        pass

    def test_base_property(g: BaseGraph):
        test_1 = True
        if g.adjacency_matrix.shape[0] != len(g.nodes):
            test_1 = False
        test_2 = True
        if g.incidence_matrix.shape[1] != len(g.edges):
            test_2 = False
        test_passed = test_1 & test_2
        return test_passed

    def test_simple_property(g: SimpleGraph):
        test_1 = True
        for i in range(g.adjacency_matrix.shape[0]):
            if g.adjacency_matrix[i, i] != 0:
                test_1 = False
        test_passed = test_1 
        return test_passed

    def test_directed_property(g: DirectedGraph):
        test_1 = True
        for i in range(g.incidence_matrix.shape[1]):
            if np.sum(g.incidence_matrix, 0) != 0:
                test_1 = False
        test_passed = test_1 
        return test_passed

    def test_weighted_property(g: WeightedGraph):
        pass

            


