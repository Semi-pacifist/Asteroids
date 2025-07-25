# imports
import pygame
from circleshape import CircleShape
from constants import *

# class definitions
class Shot(CircleShape):
    # method definitions
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
