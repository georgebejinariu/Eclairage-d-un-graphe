class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object 
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex, light):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]
            
    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges
    
    
g = { ("a",1) : ["d"],
          ('b',1) : ["c"],
          ('c',1) : ["b", "c", "d", "e"],
          ("d",1) : ["a", "c"],
          ("e",1) : ["c"],
          ("f",1) : ["d"]
          }

graph = Graph(g)

print("Vertices of graph:")
print(graph.vertices())


print("Edges of graph:")
print(graph.edges())




