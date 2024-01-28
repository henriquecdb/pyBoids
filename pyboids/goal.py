import pygame

RED = (0, 255, 0)


class Goal:
    def __init__(self, x, y, width, height):
        self.x = max(0, min(x, width))
        self.y = max(0, min(y, height))

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), 7)
