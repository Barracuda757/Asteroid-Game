import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pygame.draw.circle(screen, "white",self.position,  self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        # must override
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        child_1 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
        child_1.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle) * 1.2
        child_2 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
        child_2.velocity = pygame.math.Vector2.rotate(-self.velocity, -random_angle) * 1.2
        log_event("asteroid_split")
