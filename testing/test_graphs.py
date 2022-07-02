from msilib.schema import Error
from weighted_graphs import WeightedGraph
from directed_graphs import DirectedGraph
from standard_graphs import SimpleGraph
from base_graph import BaseGraph
from utility.graph_generator import RandomGraphFactory, GraphFactory
from itertools import chain, combinations
import pandas as pd
import numpy as np
import datetime as dt
import ast

class GraphTest():

    def __init__(self):
        self.factory = GraphFactory()
        self.test_data = self.load_test_data()

    # generate some test data with which to check the characteristics the graphs have top obey (i.e simple having no loops and multiple edges...)
    def test_graphs(self, suppress_output: bool = False):
        total_result = []
        for index, row in self.test_data.iterrows():
            nodes, edges = ast.literal_eval(row['nodes']), ast.literal_eval(row['edges'])
            g = self.factory.generate_graph(nodes, edges, row['simple'], row['directed'], row['weighted'])
            test_result = self.test_graph_properties(g, row['simple'], row['directed'], row['weighted'], suppress_output)
            total_result.append(test_result)
        if all(total_result) == True:
            print('Tests have been succesful for all graphs in the test dataset.')
        else: print('Graph test failed.')

    def load_test_data(self):
        test_data = pd.read_csv(r'C:\Users\roman\dev\git dev\GTCN\testing\test_data\test_data_graphs.csv', sep=';')
        return test_data
    
    def test_graph_properties(self, g: BaseGraph, simple: str, directed: str, weighted: str, suppress_output: bool) -> bool:
        passed_base, passed_simple, passed_directed, passed_weighted = True, True, True, True
        passed_base = self.test_base_property(g)
        if simple == True:
            passed_simple = self.test_simple_property(g)
        else: pass
        if directed == True:
            passed_directed = self.test_directed_property(g)
        else: pass
        if weighted == True:
            passed_weighted = self.test_weighted_property(g)
        else: pass
        passed = passed_base & passed_simple & passed_directed & passed_weighted
        if passed == True:
            if suppress_output == False:
                print('Graph' + str(g) + ' has passed property tests successful.')
            else: pass
        else: print('An error occured at graph object ' + str(g) + '. Please control the code or test data to resolve the error.')
        return passed

    def test_base_property(self, g: BaseGraph) -> bool:
        test_1 = True
        if (g.adjacency_matrix.shape[0] != len(g.nodes)) & (g.adjacency_matrix.shape[1] != len(g.nodes)):
            test_1 = False
            print('Failed adjacency dimension test.')
        test_2 = True
        if (g.incidence_matrix.shape[0] != len(g.nodes)) & (g.incidence_matrix.shape[1] != len(g.edges)):
            test_2 = False
            print('Failed incidence dimension test.')
        test_passed = test_1 & test_2
        return test_passed

    def test_simple_property(self, g: SimpleGraph) -> bool:
        test_1 = True
        for i in range(g.adjacency_matrix.shape[0]):
            if g.adjacency_matrix[i, i] != 0:
                test_1 = False
                print('Failed loop existence test.')
        test_passed = test_1 
        test_2 = True
        if np.unique(g.incidence_matrix, axis=1).shape[1] != len(g.edges):
            test_2 = False
            print('Failed mutiple edges existent test.')
        test_passed = test_1 & test_2
        return test_passed

    def test_directed_property(self, g: DirectedGraph) -> bool:
        test_1 = True
        if all((v is 0) or (v is 2) for v in set(np.sum(g.incidence_matrix, 0))):
            test_1 = False
            print('Failed directed property test.')
        test_passed = test_1 
        return test_passed

    def test_weighted_property(self, g: WeightedGraph) -> bool:
        test_1 = True
        weights = [2 * e[1] for e in g.edges]
        if np.array_equal(np.sum(g.incidence_matrix, 0), weights) != True:
            test_1 = False
            print('Failed consistent weight test.')
        test_passed = test_1
        return test_passed


            


