import typing

TNODE = typing.Tuple[int, int]

class Graph:
    adj: typing.Dict[TNODE, typing.List[TNODE]] = {}

    def __init__(self):
        self.adj: typing.Dict[TNODE, typing.List[TNODE]] = {}

    def add_path(self, f: TNODE, t: TNODE):
        if not f in self.adj:
            self.adj[f] = []

        self.adj[f].append(t)
