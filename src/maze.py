from .graph import Graph, TNODE

class Maze:
    def __init__(self, graph: Graph, beginning: TNODE, end: TNODE, data):
        self.graph = graph
        self.beginning = beginning
        self.end = end
        self.data = data

