from .solve import heuristic

def test_heuristic():
    assert heuristic((0, 0), (1, 1)) == 2

def test_heuristic_sort():
    nodes = [
        (0, 0),
        (10, 10),
    ]
    dest = (20, 20)
    sorted_nodes = sorted(nodes, key=lambda x: heuristic(x, dest))
    assert sorted_nodes[0] == (10, 10)
    assert sorted_nodes[1] == (0, 0)
    assert len(sorted_nodes) == 2
    assert sorted_nodes.pop(0) == (10, 10)
