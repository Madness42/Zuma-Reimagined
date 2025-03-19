import pygame
from pathing import Path
from balls import BallsManager
from constants import *


class GameManager:
    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self._clock = pygame.time.Clock()
        self._level = 1

    def play(self):
        running = True
        path = Path(self._level)
        balls_manager = BallsManager(100)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self._screen.fill((50, 50, 50))

            balls_manager.advance()
            balls_manager.update_position(path)
            balls_manager.draw(self._screen, path)

            pygame.display.update()
            self._clock.tick(FPS)

        pygame.quit()
