from utility.graph_generator import RandomGraphFactory
from itertools import chain, combinations

class GraphTest():

    def __init__(self):
        pass

    # generate some test data with which to check the characteristics the graphs have top obey (i.e simple having no loops and multiple edges...)
    def generate_test_graphs(self, number_graphs: int = 10):
        properties = set(['simple', 'directed', 'weighted'])
        graph_types = self.powerset(properties)
        print(graph_types)

    def powerset(self, iterable):
        s = list(iterable)
        print(s)
        return chain.from_iterable(combinations(s, r) for r in range(len(s)+ 1))
    
    
    def test_graph_properties():
        pass



