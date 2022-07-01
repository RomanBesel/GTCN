from utility.graph_generator import RandomGraphFactory, GraphFactory
from itertools import chain, combinations

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

    def graph_types(self):
        properties = set(['simple', 'directed', 'weighted'])
        graph_types = list(self.powerset(properties))
        return graph_types

    def powerset(self, iterable):
        s = list(iterable)
        powerset = chain.from_iterable(combinations(s, r) for r in range(len(s)+ 1))
        return powerset
    
    def test_graph_properties():
        pass



