from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_SPEED, PLAYER_TURN_SPEED
from circleshape import CircleShape
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.line_width = LINE_WIDTH
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # Draws the player as a triangle on the screen
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), self.line_width)
    
    # Rotates the player by a certain amount based on the turn speed and delta time
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    # Updates the player's position and rotation based on user input
    def update(self, dt):
         keys = pygame.key.get_pressed()

         if keys[pygame.K_a]:
            self.rotate((-dt))

         if keys[pygame.K_d]:
            self.rotate(dt)
        
         if keys[pygame.K_s]:
            self.move((-dt))
        
         if keys[pygame.K_w]:
            self.move(dt)

    # Moves the player in the direction they are currently facing
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
    
