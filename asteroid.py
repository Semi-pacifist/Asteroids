# imports
import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


# Class definitions
class Asteroid(CircleShape):
    # method definitions
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        ran_angle = random.uniform(20, 50)
        pos_velocity = self.velocity.rotate(ran_angle)
        neg_velocity = self.velocity.rotate(-ran_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = pos_velocity * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = neg_velocity * 1.2
        self.kill()
