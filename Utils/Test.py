import pytest
from Utils import graph_system

def test_graph_create():
    g = graph_system.Graph()

    node = g.create_node(['1', '2'])
    assert node.node_data == ['1', '2']
    assert node.edges == []



