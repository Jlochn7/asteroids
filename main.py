import pygame
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from logger import log_state


def main():
    print(f"Starting Asteroids with pygame version: {pygame.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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

        # Update game state and draw sprites here
        pygame.display.flip()


if __name__ == "__main__":
    main()
