import pygame


def get_image(sheet, frame, width, height):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame % 10) * width, (frame // 10) * height, width, height))
    image.set_colorkey((0, 0, 0))
    return image


def rotate_ball_image(image, path, progress):
    angle = 90 + path.progress_to_normal_velocity(progress).angle_to(pygame.math.Vector2(1, 0))

    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image.set_colorkey((0, 0, 0))
    return rotated_image
