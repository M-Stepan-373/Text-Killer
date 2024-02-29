class INode:
    ... # Интерфейс класса Node

class Edge:
    def __init__(self, edge_data: list, end_nodes: list[INode]):
        self.edge_data = edge_data
        self.end_nodes = end_nodes

class Node(INode):
    def __init__(self, node_data: list, edges: list[Edge]):
        self.node_data = node_data
        self.edges = edges # TODO: editing of this variables can cause invlaid state
                           # TODO: we need to create methods like `get_node_data()` and
                           # TODO: `get_edges_data()` and make it private

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def create_node(self, node_data: list) -> Node:
        self.nodes.append(Node(node_data, [])) # TODO: node returning

    def create_edge(self, edge_data: list, end_nodes: list[Node]) -> Edge:
        edge = Edge(edge_data, end_nodes)
        self.edges.append(edge)
        for i in end_nodes:
            i.edges.append(edge) # TODO: edge returning

    def delete_node(self, node: Node):
        self.nodes.remove(node)
        for _ in range(len(node.edges)):
            self.edges.remove(node.edges[0])
            for j in node.edges[0].end_nodes:
                j.edges.remove(node.edges[0])

    def delete_edge(self, edge: Edge):
        self.edges.remove(edge)
        for i in edge.end_nodes:
            i.edges.remove(edge)

    def get_node(self, node_data: list) -> Node:
        for i in self.nodes:
            if i.node_data == node_data:
                return i

    def get_edge(self, edge_data: list) -> Edge:
        pass # TODO

