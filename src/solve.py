from typing import List, Literal, Union, Dict

from .maze import Maze
from .graph import TNODE

def walk(maze: Maze, current_node: TNODE):
    w = Walk(maze, current_node)

    while not w.advance():
        pass

SEARCH_TYPE = Union[Literal['dfs'], Literal['bfs']]

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
        changes = [self.current_node]

        unvisited_adjacent_nodes = [node for node in self.maze.find_adjacent_nodes(self.maze.data, self.current_node) if node not in self.visited]
        self.frontier.extend(unvisited_adjacent_nodes)
        self.visited.add(self.current_node)

        if self.search_type == 'bfs':
            self.current_node = self.frontier.pop(0)
        elif self.search_type == 'dfs':
            self.current_node = self.frontier.pop()
        else:
            raise Exception('unknown search type')

        if self.current_node is None:
            raise Exception('out of nodes :(')
        
        changes.append(self.current_node)

        return changes
        
    def is_complete(self):
        return self.maze.end == self.current_node
    
INFINITY = float("inf")

class AStar:
    def __init__(self, maze: Maze, start: TNODE, search_type: SEARCH_TYPE='dfs'):
        self.maze = maze

        self.open_set = [start]
        self.visited = set(start)
        self.came_from = {}
        self.g_score = {}
        self.g_score[start] = 0
        self.f_score = {}
        self.f_score[start] = heuristic(start, self.maze.end)
        self.current_node = start
        self.path = set()

    def advance(self):
        if not len(self.open_set):
            return []

        previous_node = self.current_node

        self.current_node = sorted(self.open_set, key=lambda x: heuristic(x, self.maze.end))[0]
        self.visited.add(self.current_node)
        if self.is_complete():
            self.path = self.reconstruct_path(self.came_from, self.current_node)
        
        self.open_set.remove(self.current_node)

        for neighbor in self.maze.find_adjacent_nodes(self.maze.data, self.current_node):
            tentative_g_score = self.g_score[self.current_node] + 1 # could be d(current, neighbor)

            if tentative_g_score < self.g_score.get(neighbor, INFINITY):
                self.came_from[neighbor] = self.current_node
                self.g_score[neighbor] = tentative_g_score
                self.f_score[neighbor] = tentative_g_score + heuristic(neighbor, self.maze.end)
                if neighbor not in self.open_set and neighbor not in self.visited:
                    self.open_set.append(neighbor)

        return [previous_node, self.current_node]
        
    def is_complete(self):
        return self.maze.end == self.current_node
    
    def reconstruct_path(self, came_from: Dict[TNODE, TNODE], current_node: TNODE):
        total_path: List[TNODE] = [current_node]
        while current_node in came_from:
            current_node = came_from[current_node]
            total_path.insert(0, current_node)
        return total_path

def solve(maze: Maze):
    where_am_i = maze.beginning
    walk(maze, where_am_i)
