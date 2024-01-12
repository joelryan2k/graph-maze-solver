import pygame
import time
import datetime

from .maze import Maze
from .map import is_beginning, is_end, is_passable
from .solve import Walk, AStar

SQUARE_SIZE = 15

def draw_node(node, walk: AStar, window_surface):
    if is_beginning(walk.maze.data, *node):
        color = 'blue'
    elif is_end(walk.maze.data, *node):
        color = 'yellow'
    elif walk.path and node in walk.path:
        color = 'green'
    elif walk.current_node == node:
        color = 'purple'
    elif node in walk.visited:
        color = 'grey'
    elif is_passable(walk.maze.data, *node):
        color = 'black'
    else:
        color = 'red'

    pygame.draw.rect(window_surface, color, pygame.Rect(node[0] * SQUARE_SIZE, node[1] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def run_game(maze: Maze):
    # walk = Walk(maze=maze, current_node=maze.beginning, search_type='a-star')
    walk = AStar(maze=maze, start=maze.beginning)

    pygame.init()

    pygame.display.set_caption('Quick Start')
    window_surface = pygame.display.set_mode((800, 600))


    background = pygame.Surface((800, 600))
    background.fill(pygame.Color('#000000'))

    for y, row in enumerate(maze.data):
        for x, col in enumerate(row):
            draw_node((x, y), walk, window_surface)

    pygame.display.update()
    is_running = True
    kill = None

    while is_running and (kill is None or kill > datetime.datetime.now()):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        # time.sleep(.1)
        changes = []

        if not walk.is_complete():
            changes = walk.advance()
        else:
            changes = walk.path

        if len(changes):
            for change in changes:
                draw_node(change, walk, window_surface)

            pygame.display.update()

        if walk.is_complete() and kill is None:
            print(walk.path)
            pygame.display.update()
            kill = datetime.datetime.now() + datetime.timedelta(seconds=.5)

    # pygame.display.update()
