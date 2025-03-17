import pygame
from pathing import Path
from balls import BallsManager

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class GameManager:
    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self._clock = pygame.time.Clock()
        self._level = 1

    def play(self):
        running = True
        path = Path(self._level)
        balls_manager = BallsManager(10)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self._screen.fill((0, 0, 0))

            balls_manager.advance()
            balls_manager.update_position(path)
            balls_manager.draw(self._screen)

            pygame.display.update()
            self._clock.tick(60)

        pygame.quit()
