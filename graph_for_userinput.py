#Creating a Graph class for the graph data structure
class Graph():
    def __init__(self):
        # Initialize an empty adjacency list
        self._adj_list = dict()
        self._h_value = dict()
    def add_edge(self, node1, node2):
        # Add edges to the adjacency list
        if node1 in self._adj_list:
            self._adj_list[node1].append(node2)
        else:
            self._adj_list[node1] = [node2]
        # Since this is an undirected graph, add the edge in both directions
        if node2 in self._adj_list:
            self._adj_list[node2].append(node1)
        else:
            self._adj_list[node2] = [node1]
    #Setting the Heuristic value
    def add_value(self, node, value):
        if node not in self._h_value.keys():
            raise ValueError(f'Node not found in the graph object to heuristic value')
        self._h_value[node] = value
    #Getting the Heuristic value
    def get_value(self, node):
        if node in self._h_value.keys():
            return self._h_value[node]
        raise ValueError('Hurestic Fucntion is not set')
    #Getting the Heuristic value list
    def get_value_list(self):
        return list(self._h_value.items())
    #Returning the child
    def child(self, node):
        return list(self._adj_list[node])
    #Sorting the list of child
    def sort(self):
        for k,v in self._adj_list.items():
            self._adj_list[k] = v.sort(key = lambda x : self._h_value[x])
    #Fucntion printing the graph Object
    def __str__(self):
        return str(self._adj_list)

# Example usage:
if __name__ == "__main__":
    my_graph = Graph()
    my_graph.add_edge(1, 2)
    my_graph.add_edge(2, 3)
    my_graph.add_edge(1, 3)

    my_graph.add_value(1, 45)
    my_graph.add_value(2, 54)
    my_graph.add_value(5, 54)

    print(my_graph)

    print(my_graph.get_value_list())