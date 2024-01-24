import math
import random

import pygame

WHITE = (255, 255, 255)


class Boid:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = 2
        self.width = width
        self.height = height

    def update(self, boids):
        alignment = self.alignment(boids)
        cohesion = self.cohesion(boids)
        separation = self.separation(boids)

        self.angle += alignment + cohesion + separation
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

    def alignment(self, boids):
        avg_angle = sum(b.angle for b in boids) / len(boids)
        return (avg_angle - self.angle) / 8

    def cohesion(self, boids):
        avg_x = sum(b.x for b in boids) / len(boids)
        avg_y = sum(b.y for b in boids) / len(boids)
        angle_to_avg = math.atan2(avg_y - self.y, avg_x - self.x)
        return (angle_to_avg - self.angle) / 100

    def separation(self, boids):
        min_distance = 25
        move_x, move_y = 0, 0

        for b in boids:
            if b != self:
                distance = math.sqrt((self.x - b.x) ** 2 + (self.y - b.y) ** 2)
                if distance < min_distance:
                    move_x += self.x - b.x
                    move_y += self.y - b.y

        separation_angle = math.atan2(move_y, move_x)
        return (separation_angle - self.angle) / 8

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), 5)
