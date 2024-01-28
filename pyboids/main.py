import random

import pygame

from boid import Boid
from goal import Goal

pygame.init()

BLACK = (0, 0, 0)
WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boids Simulation")


def main():
    clock = pygame.time.Clock()
    num_boids = 10
    boids = [Boid(random.uniform(0, WIDTH), random.uniform(0, HEIGHT), WIDTH, HEIGHT) for _ in range(num_boids)]
    goal = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if goal is None or any(boid.reached_goal(goal.x, goal.y) for boid in boids):
            goal = Goal(random.uniform(0, WIDTH), random.uniform(0, HEIGHT), WIDTH, HEIGHT)

        screen.fill(BLACK)

        if goal is not None:
            goal.draw(screen)

        for boid in boids:
            boid.update(boids, goal.x, goal.y)
            boid.draw(screen)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
