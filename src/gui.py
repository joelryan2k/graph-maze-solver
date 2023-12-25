import pygame
import time

from .maze import Maze
from .map import is_beginning, is_end, is_passable
from .solve import Walk

SQUARE_SIZE = 15

def draw_node(node, walk: Walk, window_surface):
    if walk.current_node == node:
        color = 'purple'
    elif is_beginning(walk.maze.data, *node):
        color = 'green'
    elif is_end(walk.maze.data, *node):
        color = 'yellow'
    elif node in walk.visited:
        color = 'grey'
    elif is_passable(walk.maze.data, *node):
        color = 'black'
    else:
        color = 'red'

    pygame.draw.rect(window_surface, color, pygame.Rect(node[0] * SQUARE_SIZE, node[1] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def run_game(maze: Maze):
    walk = Walk(maze=maze, current_node=maze.beginning, search_type='a-star')

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

    while is_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        # time.sleep(.1)
        if not walk.is_complete():
            changes = walk.advance()
            # print(changes)
            for change in changes:
                draw_node(change, walk, window_surface)
            pygame.display.update()

        # window_surface.blit(background, (0, 0))

    pygame.display.update()
