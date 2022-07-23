from lib2to3.pytree import Base
from msilib.schema import Error
import numpy as np

class NewBaseGraph():

    def __init__(self, nodes: list, edges: list):
        self.nodes: set = nodes
        self.node_objects_map: dict = self.map_node_objects(self.nodes)

        self.edges: list = edges
        self.edge_objects_map: list = self.map_edge_objects(self.edges)

        self.adjacency_matrix: np.array = self.construct_adjacency_matrix()
        self.incidence_matrix: np.array = self.construct_incidence_matrix()
        self.degree_matrix: np.array = self.construct_degree_matrix()

    ''' ********************************** Getter and Setter **********************************'''

    @property
    def nodes(self):
        return self._nodes

    @nodes.setter
    def nodes(self, nodes: list):
        nodes = set([Node(node, self, number) for node, number in zip(nodes, range(len(nodes)))])
        self._nodes = nodes

    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, edges: list):
        edges = [Edge(edge, self) for edge in edges]
        self._edges = edges

    ''' ********************************** Mapping **********************************'''

    def map_node_objects(self, nodes) -> None:
        nodes_map = dict()
        for n in self.nodes:
            nodes_map[n.node] = n.number
        return nodes_map

    def map_edge_objects(self, edges) -> None:
        edges_map = dict()
        for e in self.edges:
            edges_map[e.edge] = e.number_tuple
        return edges_map

    ''' ********************************** Matrix Methods **********************************'''
    
    def construct_adjacency_matrix(self) -> np.array:
        adjacency_matrix = np.zeros((len(self.nodes), len(self.nodes)))
        return adjacency_matrix

    def construct_incidence_matrix(self) -> np.array:
        incidence_matrix = np.zeros((len(self.nodes), len(self.edges)))
        return incidence_matrix

    def construct_degree_matrix(self) -> np.array:
        degree_matrix = np.zeros((len(self.nodes), len(self.nodes)))
        sums_row = np.sum(self.adjacency_matrix, 1)
        for i in range(len(self.nodes)):
            degree_matrix[(i, i)] = sums_row[i]
        return degree_matrix

    ''' ********************************** Add and Delete methods **********************************'''

    def update_matrizes(self) -> None:
        self.adjacency_matrix = self.construct_adjacency_matrix()
        self.incidence_matrix = self.construct_incidence_matrix()
        self.degree_matrix = self.construct_degree_matrix()

    def add_node(self, node):
        node = Node(node, self)
        self.nodes.add(node)
        self.update_matrizes()
        
    def delete_node(self, node):
        if isinstance(node, Node):
            self.nodes.remove(node)
        else: raise ValueError('Passed argument is not of type {class Node}.')
        self.update_matrizes()

    def add_edge(self, edge):
        edge = Edge(edge, self)
        self.edges.append(edge)
        self.update_matrizes()
        
    def delete_edge(self, edge):
        if isinstance(edge, Edge):
            self.edges.remove(edge)
        else: raise ValueError('Passed argument is not of type {class Edge}.')
        self.update_matrizes()

''' ++++++++++++++++++++++++++++++++++++++++ Node and Edge Class ++++++++++++++++++++++++++++++++++++++++ '''

class Node(object):

    def __init__(self, node: object, graph: NewBaseGraph, number: int = None) -> None:
        self.node = node
        self.graph = graph
        self.number = self.map_to_int(number)

    def map_to_int(self, number) -> int:
        if (number == None) and (len(self.graph.nodes) != 0):
            node_number = max(self.graph.nodes_number) + 1
        elif number != None:
            node_number = number
        else: raise Error('Couldnt map the passed object to an integer.')
        return node_number

class Edge(object):

    def __init__(self, edge: tuple, graph: NewBaseGraph) -> None:
        self.edge = edge
        self.graph = graph
        self.number_tuple = self.map_to_int(self.edge)

    def map_to_int(self, edge: tuple) -> tuple:
        if (edge[0] in self.graph.node_objects_map.keys()) and (edge[0] in self.graph.node_objects_map.keys()):
            first_node_int = self.graph.node_objects_map[edge[0]]
            second_node_int = self.graph.node_objects_map[edge[1]]
        else: raise ValueError('One or both of the nodes in the passed edge dont exist in the graphs node set.') 
        return tuple([first_node_int, second_node_int])





    

