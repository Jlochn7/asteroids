import pygame
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from logger import log_state
from player import Player


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
    
    # Add the player to the updatable and drawable groups   
    # This allows the player to be updated and drawn each frame without needing to manage them separately
    # This must be done before creating any player objects 
    Player.containers = (updatable, drawable)

    # Create player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        
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

        # Draw the player
        for thing in drawable:
            thing.draw(screen)

        # Update game state and draw sprites here
        pygame.display.flip()

        # Cap the frame rate and calculate delta time
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
