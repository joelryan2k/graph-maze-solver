import pygame
import time

from .maze import Maze
from .map import is_beginning, is_end, is_passable
from .solve import Walk

SQUARE_SIZE = 15

def run_game(maze: Maze):
    walk = Walk(maze=maze, current_node=maze.beginning, search_type='a-star')

    pygame.init()

    pygame.display.set_caption('Quick Start')
    window_surface = pygame.display.set_mode((800, 600))

    background = pygame.Surface((800, 600))
    background.fill(pygame.Color('#000000'))

    is_running = True

    while is_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        for y, row in enumerate(maze.data):
            for x, col in enumerate(row):
                if walk.current_node == (x, y):
                    color = 'purple'
                elif is_beginning(maze.data, x, y):
                    color = 'green'
                elif is_end(maze.data, x, y):
                    color = 'yellow'
                elif (x, y) in walk.visited:
                    color = 'grey'
                elif is_passable(maze.data, x, y):
                    color = 'black'
                else:
                    color = 'red'

                pygame.draw.rect(window_surface, color, pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        pygame.display.update()

        time.sleep(.1)
        walk.advance()
        # window_surface.blit(background, (0, 0))

    pygame.display.update()
