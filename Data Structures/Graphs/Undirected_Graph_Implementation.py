# Edge List

# Adjacent List

#Adjacent Matrix
class Graph:
    def __init__(self):
        self.number_of_nodes =0
        self.adjacent_list = {}
    def inset_node(self,data):
        if data not in self.adjacent_list:
            self.adjacent_list[data]
            self.number_of_nodes+=1
    def insert_edge(self, vertex1, vertex2):
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return
        return "Edge already exists"
    def show_connections(self):
        for node in self.adjacency_list:
            print(f'{node} -->> {" ".join(map(str, self.adjacency_list[node]))}')
        
