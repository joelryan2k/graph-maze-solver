from src.solve import read_maze
from src.gui import run_game

if __name__ == '__main__':
    maze = read_maze('maze2.txt', col_width=2)
    # solve(maze)
    run_game(maze)
