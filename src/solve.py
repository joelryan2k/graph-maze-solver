from typing import List, Literal, Union

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

SEARCH_TYPE = Union[Literal['dfs'], Literal['bfs'], Literal['a-star']]

def heuristic(from_node: TNODE, to_node: TNODE):
    return abs(to_node[1] - from_node[1]) + abs(to_node[0] - from_node[0])

class Walk:
    def __init__(self, maze: Maze, current_node: TNODE, search_type: SEARCH_TYPE='dfs'):
        self.maze = maze
        self.current_node = current_node
        self.frontier: List[TNODE] = []
        self.visited = set()
        self.search_type = search_type

    def advance(self):
        if self.current_node == self.maze.end:
            print('we got it!')
            return True

        unvisited_adjacent_nodes = [node for node in self.maze.find_adjacent_nodes(self.maze.data, self.current_node) if node not in self.visited]
        self.frontier.extend(unvisited_adjacent_nodes)
        self.visited.add(self.current_node)

        if self.search_type == 'bfs':
            self.current_node = self.frontier.pop(0)
        elif self.search_type == 'dfs':
            self.current_node = self.frontier.pop()
        elif self.search_type == 'a-star':
            self.frontier = sorted(self.frontier, key=lambda x: heuristic(x, self.maze.end))
            self.current_node = self.frontier.pop(0)
        else:
            raise Exception('unknown search type')

        if self.current_node is None:
            raise Exception('out of nodes :(')

def solve(maze: Maze):
    where_am_i = maze.beginning
    walk(maze, where_am_i)
