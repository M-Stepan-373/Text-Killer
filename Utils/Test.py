import pytest
from Utils import graph_system

def test_graph_create():
    g = graph_system.Graph()

    for _ in range(99999):
        g.create_node(['1', '2'])

    node = g.create_node(['1', '2'])

    for i in range(100000):
        assert g.nodes[i - 1].node_data == ['1', '2']
        assert g.nodes[i - 1].edges == []
    node.node_data = ['11', '2']
    assert g.nodes[99999].node_data == ['11', '2']
