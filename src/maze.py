from .graph import TNODE

class Maze:
    def __init__(self, beginning: TNODE, end: TNODE, data):
        self.beginning = beginning
        self.end = end
        self.data = data

    def find_adjacent_nodes(self, data, node: TNODE):
        from .map import is_passable

        to_check = [
            (node[0] - 1, node[1]),
            (node[0] + 1, node[1]),
            (node[0], node[1] - 1),
            (node[0], node[1] + 1),
        ]

        return [x for x in to_check if is_passable(data, *x)]

