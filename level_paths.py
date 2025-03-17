LEVEL_1 = ((100, 0), (100, 500), (700, 500), (700, 100), (200, 100), (200, 400), (600, 400), (600, 200))
LEVEL_2 = ()
LEVEL_3 = ()


def level_to_points(level: int):
    if level == 1:
        return LEVEL_1
    if level == 2:
        return LEVEL_2
    if level == 3:
        return LEVEL_3
