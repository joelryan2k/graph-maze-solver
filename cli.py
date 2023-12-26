from src.gui import run_game
from src.map import read_map
from src.maze import Maze
from src.micromouse import convert_micro_mouse

import glob

def read_maze(fn: str, col_width=2) -> Maze:
    with open(fn, 'r') as fh:
        data = fh.readlines()

    if any(['o-' in l for l in data]):
        data = convert_micro_mouse(data)

    return read_map(data, col_width=col_width)

if __name__ == '__main__':
    for foo in glob.glob('./mazefiles/classic/*.txt'):
        maze = read_maze(foo)
        run_game(maze)
