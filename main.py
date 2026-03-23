import sys

import pygame
from asteroid import Asteroid
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from logger import log_state
from logger import log_event
from player import Player
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame
    pygame.init()

    # Set up the game clock for managing frame rate and delta time
    game_clock = pygame.time.Clock()
    dt = 0
    
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set up sprite groups for managing updatable and drawable objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Add the player to the updatable and drawable groups   
    # This allows the player to be updated and drawn each frame without needing to manage them separately
    # This must be done before creating any player objects 
    Player.containers = (updatable, drawable)

    # Add asteroid to asteroids, updatable, and drawable groups
    Asteroid.containers = (asteroids, updatable, drawable)
    
    # Set asteroid field to be updatable so it can spawn asteroids
    AsteroidField.containers = (updatable,)

    # Add shots to shots, updatable, and drawable groups
    Shot.containers = (shots, updatable, drawable)
    
    # Create player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Create asteroid field object
    field = AsteroidField()

    # Main game loop
    while (True):
        # Log the game state at the start of each frame
        log_state()
        
        # Handle events (e.g., quit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Clear the screen (for demonstration purposes)
        screen.fill("black")

        # Update the player state
        updatable.update(dt)

        # Check for collisions between the player and asteroids
        for asteroid in asteroids:
            collision = player.collide_with(asteroid)
            if collision:
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
                return

        # Draw the player
        for thing in drawable:
            thing.draw(screen)

        # Update game state and draw sprites here
        pygame.display.flip()

        # Cap the frame rate and calculate delta time
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
