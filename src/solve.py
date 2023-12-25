from typing import List

from .maze import Maze
from .map import read_map
from .graph import TNODE

def read_maze(fn: str, col_width=1) -> Maze:
    with open(fn, 'r') as fh:
        data = fh.readlines()

    return read_map(data, col_width=col_width)

def walk(maze: Maze, current_node: TNODE):
    w = Walk(maze, current_node)

    while not w.advance():
        pass

class Walk:
    def __init__(self, maze: Maze, current_node: TNODE, bfs=False):
        self.maze = maze
        self.current_node = current_node
        self.frontier: List[TNODE] = []
        self.visited = set()
        self.bfs = bfs

    def advance(self):
        if self.current_node == self.maze.end:
            print('we got it!')
            return True

        unvisited_adjacent_nodes = [node for node in self.maze.graph.adj[self.current_node] if node not in self.visited]
        self.frontier.extend(unvisited_adjacent_nodes)
        self.visited.add(self.current_node)

        if self.bfs:
            self.current_node = self.frontier.pop(0)
        else:
            self.current_node = self.frontier.pop()

        if self.current_node is None:
            raise Exception('out of nodes :(')

def solve(maze: Maze):
    where_am_i = maze.beginning
    frontier = []
    walk(maze, where_am_i)
