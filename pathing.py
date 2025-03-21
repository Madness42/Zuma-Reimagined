import math
import pygame
from level_paths import level_to_points


class Path:
    def __init__(self, level: int):
        self._points = level_to_points(level)
        self._whole_length = 0
        self._lengths = list()

        summ = 0
        for i in range(1, len(self._points)):
            x_side = self._points[i][0] - self._points[i-1][0]
            y_side = self._points[i][1] - self._points[i-1][1]
            self._lengths.append(math.sqrt(x_side**2 + y_side**2))
            summ += math.sqrt(x_side**2 + y_side**2)
        self._whole_length = summ

    def __len__(self):
        return self._whole_length

    def progress_to_position(self, progress: float):
        return self.__position_or_velocity(progress, True)

    def progress_to_normal_velocity(self, progress: float):
        return self.__position_or_velocity(progress, False)

    def __position_or_velocity(self, progress: float, return_position: bool):
        cumulative_length = 0
        count = 0
        segment_progress = progress
        if progress < 0:
            if return_position:
                return pygame.math.Vector2(-1000, -1000)
            return pygame.math.Vector2(1, 0)
        for segment in self._lengths:
            cumulative_length += segment
            if progress >= cumulative_length:
                count += 1
                segment_progress -= segment
                continue
            x = self._points[count][0] + (self._points[count + 1][0] - self._points[count][0])\
                * (segment_progress / segment)
            y = self._points[count][1] + (self._points[count + 1][1] - self._points[count][1])\
                * (segment_progress / segment)
            if return_position:
                return pygame.math.Vector2(x, y)
            sector_end = pygame.math.Vector2(self._points[count + 1][0], self._points[count + 1][1])
            return (sector_end - pygame.math.Vector2(x, y)).normalize()
