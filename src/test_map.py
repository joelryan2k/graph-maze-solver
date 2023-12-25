from .map import is_passable, read_map

def test_is_passable():
    data = [
        '  ',
        '  B'
    ]
    assert is_passable(data, 0, 0) == True
    assert is_passable(data, 2, 1) == False
    assert is_passable(data, -1, -1) == False

def test_read_map():
    maze = read_map(['S E'], col_width=1)
    assert len(maze.graph.adj) == 3
    assert (1, 0) in maze.graph.adj[(0, 0)]
    assert (0, 0) in maze.graph.adj[(1, 0)]
    assert (2, 0) in maze.graph.adj[(1, 0)]
    assert (1, 0) in maze.graph.adj[(2, 0)]
    assert maze.beginning == (0, 0)
    assert maze.end == (2, 0)

def test_read_map_width2():
    maze = read_map([' S   E'], col_width=2)
    assert len(maze.graph.adj) == 3
    assert (1, 0) in maze.graph.adj[(0, 0)]
    assert (0, 0) in maze.graph.adj[(1, 0)]
    assert (2, 0) in maze.graph.adj[(1, 0)]
    assert (1, 0) in maze.graph.adj[(2, 0)]
    assert maze.beginning == (0, 0)
    assert maze.end == (2, 0)
