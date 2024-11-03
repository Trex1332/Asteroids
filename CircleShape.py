import pygame
from constants import *
# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen,"white",self.triangle(),width = 2)

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, B):
        distance = self.position.distance_to(B.position)
        total_radius = self.radius + B.radius
        print(f"Distance: {distance}, Self radius: {self.radius}, Other radius: {B.radius}")
        if distance <= self.radius + B.radius:
            return True
        else:
            return False

