class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def print_graph(self):
        for vertex, edges in self.adj_list.items():
            print(f"{vertex}: {edges}")

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False


# Example usage
my_graph = Graph()

# Adding vertices
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_vertex(4)
my_graph.add_vertex(5)
print("Graph after adding vertices:")
my_graph.print_graph()
print("--------------------------------------")

# Adding edges
my_graph.add_edge(1, 2)
my_graph.add_edge(1, 3)
my_graph.add_edge(2, 4)
my_graph.add_edge(3, 5)
print("Graph after adding edges:")
my_graph.print_graph()
print("--------------------------------------")

# Removing an edge
my_graph.remove_edge(1, 3)
print("Graph after removing the edge between 1 and 3:")
my_graph.print_graph()
print("--------------------------------------")

# Adding more edges
my_graph.add_edge(4, 5)
my_graph.add_edge(2, 3)
print("Graph after adding more edges:")
my_graph.remove_edge(1, 5)
my_graph.remove_edge(1, 5)
my_graph.print_graph()
print("--------------------------------------")
my_graph.remove_edge(1, 5)
my_graph.print_graph()
print("--------------------------------------")
my_graph.remove_edge(2, 4)
my_graph.print_graph()
print("--------------------------------------")
my_graph.remove_vertex(5)
my_graph.print_graph()
print("--------------------------------------")
