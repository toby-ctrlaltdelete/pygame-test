# import the pygame module, so you can use it
import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of <HORIZONTAL> x <VERTICAL>
    screen = pygame.display.set_mode((240,180))
     
    # define a variable to control the main loop
    running = True
    
	# Fill the background with white
    screen.fill((255, 255, 255))
	
    # Create a surface; parameters (length, width)
    surf = pygame.Surface((50, 50))
	
	# Put the center of surf at the center of the display
    surf_center = ((SCREEN_WIDTH-surf.get_width())/2,(SCREEN_HEIGHT-surf.get_height())/2)

    # Draw surf at the new coordinates
    screen.blit(player.surf, player.rect)
    pygame.display.flip()

    # Give the surface a color to separate it from the background
    surf.fill((0, 0, 0))
    # to get the rectangle itself, use 'rect = surf.get_rect()'

    # Draw a solid blue circle in the center
	# Parameters: surface, color, center point, radius
    pygame.draw.circle(screen, (0, 0, 255), (90, 120), 20)
	
    # Update the window, because I guess that's not built-in
    pygame.display.flip()
	
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
		    # Look at every event in the queue
            # Did the user hit a key?
            if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    running = False

        # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                running = False
	 
	 
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()