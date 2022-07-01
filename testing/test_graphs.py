from utility.graph_generator import RandomGraphFactory

class GraphTest():

    def __init__(self) -> None:
        self.factory = RandomGraphFactory()

    # generate some test data with which to check the characteristics the graphs have top obey (i.e simple having no loops and multiple edges...)
    def generate_test_graphs(self, number_graphs: int = 10):
        properties = ['simple', 'directed', 'weighted']
        graph_list = []
        for i in range(number_graphs):
            g = self.factory.generate_graph()
            graph_list.append(g)

    
    def test_graph_properties():
        pass



