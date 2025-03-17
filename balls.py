import pygame
from pathing import Path


class Ball:
    def __init__(self):
        self.position = pygame.math.Vector2(-1000, -1000)
        self.progress = -100

    def advance(self, speed: float):
        self.progress = self.progress + speed

    def set_progress(self, new_progress: float):
        self.progress = new_progress

    def update_position(self, path: Path):
        self.position = path.progress_to_position(self.progress)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.position, 18)
        print("drew circle at", self.position)
        print("ball progress: ", self.progress)


class BallsManager:
    def __init__(self, ball_count: int):
        self._speed = 1
        self._speed_modifier = 1
        self._number_of_balls_left = ball_count
        self._balls = [[]]
        self.initialize_balls()

    def initialize_balls(self):
        for i in range(0, self._number_of_balls_left):
            self._balls[0].append(Ball())

    def advance(self):
        pushing_ball_progress = 0
        count = 0
        for ball in self._balls[0]:
            if count == 0:
                ball.advance(self._speed * self._speed_modifier)
                pushing_ball_progress = ball.progress
                count += 1
                continue
            ball.set_progress(pushing_ball_progress - 36 * count)
            count += 1

    def update_position(self, path: Path):
        for ball_clump in self._balls:
            for ball in ball_clump:
                ball.update_position(path)

    def draw(self, screen):
        for ball_clump in self._balls:
            for ball in ball_clump:
                ball.draw(screen)
