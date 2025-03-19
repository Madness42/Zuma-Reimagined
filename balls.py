import math
import pygame
from pathing import Path
from constants import *
import random
from sprite_methods import *


class Ball:
    def __init__(self):
        self.position = pygame.math.Vector2(-1000, -1000)
        self.progress = -100
        self._color = random.randint(0, 3)
        self._spritesheet = pygame.image.load('zumaBalls.png').convert_alpha()
        self._frame_count = BALL_SHEET_SPRITE_COUNT

    def advance(self, speed: float):
        self.progress = self.progress + speed

    def set_progress(self, new_progress: float):
        self.progress = new_progress

    def update_position(self, path: Path):
        self.position = path.progress_to_position(self.progress)

    def draw(self, screen: pygame.display, path: Path):
        circumference = math.pi * BALL_DIAMETER
        revolutions = self.progress / circumference
        frame_count = self._frame_count

        frame = ((frame_count * revolutions) // 1) % frame_count + frame_count * self._color

        image = get_image(self._spritesheet, frame, BALL_DIAMETER, BALL_DIAMETER)
        rotated_image = rotate_ball_image(image, path, self.progress)

        screen.blit(rotated_image, self.position)


class BallsManager:
    def __init__(self, ball_count: int):
        self._speed = 2
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
            ball.set_progress(pushing_ball_progress - BALL_DIAMETER * count)
            count += 1

    def update_position(self, path: Path):
        for ball_clump in self._balls:
            for ball in ball_clump:
                ball.update_position(path)

    def draw(self, screen, path: Path):
        for ball_clump in self._balls:
            for ball in ball_clump:
                ball.draw(screen, path)
