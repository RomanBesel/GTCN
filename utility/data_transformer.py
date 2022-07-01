

class DataTransformer(object):

    def __init__(self) -> None:
        pass

    def transform_input(self, nodes: list, edges: list, weighted: bool):
        int_to_nodes, nodes_to_int, nodes = self.transform_nodes(nodes)
        if weighted == True:
            edges = self.transform_weighted_edges(nodes_to_int, edges)
        else: edges = self.transform_edges(nodes_to_int, edges)
        return nodes, edges
            
    def transform_nodes(self, nodes: list):
        nodes_to_int, int_to_nodes, nodes_list = {},{}, [] # nodes_to_int is a mapping of nodes to an integer number for better processing
        if all([isinstance(item, int) for item in nodes]) == False:
            for index, n in zip(range(len(nodes)), nodes):
                int_to_nodes[index] = n
                nodes_to_int[n] = index
            nodes_list = [x for x in int_to_nodes.keys()]
        else: nodes_list = nodes
        return int_to_nodes, nodes_to_int, nodes_list

    def transform_edges(self, nodes_to_int: dict, edges: list) -> list:
        is_tuple = all([isinstance(item, tuple) for item in edges])
        if is_tuple == False:   ## check if all items in the list are tuples
            raise ValueError('Edges provided for the graph must come in tuple form (a, b)')
        else: pass

        node_one = [e[0] for e in edges]  # nodes a in (a, b)
        node_two = [e[1] for e in edges]   # nodes b in (a, b)
        only_int = (all([isinstance(item, int) for item in node_one]) | all([isinstance(item, int) for item in node_two]))

        if  only_int == False:
            edges = [(nodes_to_int[e[0]], nodes_to_int[e[1]]) for e in edges]
        else: pass
        return edges

    def transform_weighted_edges(self, nodes_to_int: dict, edges: list) -> list:
        is_tuple = all([isinstance(item[0], tuple) for item in edges])
        is_number = all([isinstance(item[1], (int, float)) for item in edges])

        if  is_tuple == False:   ## check if all items in the list are tuples
            raise ValueError('Edges provided for the graph must come in tuple form (a, b)')
        else: pass

        if  is_number == False:   ## check if all items in the list are tuples
            raise ValueError('Weights can only be numeric.')
        else: pass

        node_one = [e[0][0] for e in edges]  # nodes a in (a, b)
        node_two = [e[0][1] for e in edges]   # nodes b in (a, b)
        only_int = (all([isinstance(item, int) for item in node_one]) | all([isinstance(item, int) for item in node_two]))

        if  only_int == False:
            edges = [(nodes_to_int[e[0][0]], nodes_to_int[e[0][1]]) for e in edges]
        else: pass
        return edges