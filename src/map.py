import typing

from .maze import Maze
from .graph import TNODE, Graph

def is_beginning(data: typing.List[str], x: int, y: int):
    return data[y][x] == 'S'

def is_end(data: typing.List[str], x: int, y: int):
    return data[y][x] == 'E'

def is_passable(data: typing.List[str], x: int, y: int):
    if x < 0 or y < 0 or (x > len(data[0]) - 1) or (y > len(data) - 1):
        return False
    
    return data[y][x] in (' ', 'S', 'E')

def adjust_width(row: str, col_width: int):
    if col_width == 1:
        return row
    
    return row[1::col_width]

def read_map(data: typing.List[str], col_width: int):
    beginning: typing.Union[TNODE, None] = None
    end: typing.Union[TNODE, None] = None
    graph = Graph()

    data = [adjust_width(row, col_width) for row in data]

    for y, row in enumerate(data):
        for x, _ in enumerate(row):
            if not is_passable(data, x, y):
                continue

            if is_beginning(data, x, y):
                beginning = (x, y)
            elif is_end(data, x, y):
                end = (x, y)

            # right
            if is_passable(data, x + 1, y):
                graph.add_path((x, y), (x + 1, y))

            # left
            if is_passable(data, x - 1, y):
                graph.add_path((x, y), (x - 1, y))

            # above
            if is_passable(data, x, y - 1):
                graph.add_path((x, y), (x, y - 1))

            # below
            if is_passable(data, x, y + 1):
                graph.add_path((x, y), (x, y + 1))

    if not beginning:
        raise Exception('no beginning')

    if not end:
        raise Exception('no end')

    return Maze(graph, beginning, end, data)
