from data_transformer import DataTransformer
import numpy as np
from base_graph import BaseGraph
from simple_graphs import SimpleGraph, SimpleDirectedGraph, SimpleWeightedGraph
from graphs import Graph, DirectedGraph, WeightedGraph
from utility import *


class RandomGraphFactory(object):

    def __init__(self):
        pass

    def generate_graph(self, n: int, e: int = None, simple: bool = True, directed: bool = False, weighted: bool = False, complete: str = False) -> object:
        nodes = [x for x in range(0, n-1)]
        edges = self.generate_edge_set(n, e, simple, directed, weighted, complete)
        return self.graph(nodes, edges, simple, directed, weighted)

    def graph(self, nodes, edges, simple: bool, directed: bool, weighted: bool):
        if simple == True:
            if (directed == False) & (weighted == False):
                return SimpleGraph(nodes, edges)
            elif (directed == True) & (weighted == False):
                return SimpleDirectedGraph(nodes, edges)
            elif (directed == False) & (weighted == True):
                return SimpleWeightedGraph(nodes, edges)
            else: raise ValueError('Error in graph construction. Property case doesnt exist.')
        elif simple == False:                                   #
            if (directed == False) & (weighted == False):
                return Graph(nodes, edges)
            elif (directed == True) & (weighted == False):
                return DirectedGraph(nodes, edges)
            elif (directed == False) & (weighted == True):
                return WeightedGraph(nodes, edges)
            else: raise ValueError('Error in graph construction. Property case doesnt exist.')

    def generate_edge_set(self, n, e, simple, directed, weighted, complete):

            if directed == True:
                max_number_edges = int(n * (n - 1))
            else: max_number_edges = int(n * (n - 1) / 2) 

            if (complete == False) & (e == None):
                number_edges = np.random.randint(max_number_edges)
            elif (complete == True) & (e == None): 
                number_edges = max_number_edges
            elif e != None: number_edges = e
            else: print('Error in max_number assignment.')

            if weighted == True:
                edges = [((np.random.randint(n-1), np.random.randint(n-1)), np.random.randint(100)) for _ in range(number_edges)]
            else: edges = [(np.random.randint(n-1), np.random.randint(n-1)) for _ in range(number_edges)]
            return edges


class GraphFactory(object):

    def __init__(self):
        self.data_transformer = DataTransformer()

    def generate_graph(self, n: list, e: list, simple: bool = False, directed: bool = False, weighted: bool = False) -> object:
        n, e = self.data_transformer.transform_input(n, e, weighted)
        return self.graph(n, e, simple, directed, weighted)

    def graph(self, nodes, edges, simple: bool, directed: bool, weighted: bool):
        if simple == True:
            if (directed == False) & (weighted == False):
                return SimpleGraph(nodes, edges)
            elif (directed == True) & (weighted == False):
                return SimpleDirectedGraph(nodes, edges)
            elif (directed == False) & (weighted == True):
                return SimpleWeightedGraph(nodes, edges)
            else: raise ValueError('Error in graph construction. Property case doesnt exist.')
        elif simple == False:                                   #
            if (directed == False) & (weighted == False):
                return Graph(nodes, edges)
            elif (directed == True) & (weighted == False):
                return DirectedGraph(nodes, edges)
            elif (directed == False) & (weighted == True):
                return WeightedGraph(nodes, edges)
            else: raise ValueError('Error in graph construction. Property case doesnt exist.')

    


