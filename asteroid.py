import random
import pygame
from constants import *
from logger import log_event
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.line_width = LINE_WIDTH
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, self.line_width)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        from asteroidfield import AsteroidField
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")

        new_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new1 = self.velocity.rotate(new_angle) * 1.2
        new2 = self.velocity.rotate(-new_angle) * 1.2

        AsteroidField.spawn(self, new_radius, self.position, new1)
        AsteroidField.spawn(self, new_radius, self.position, new2)

