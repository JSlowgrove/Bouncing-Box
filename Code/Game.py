import pygame
import Player

## Documentation for the Game class.
#
#  This class contains all of the functions and variables that is used by the Game.
class Game:

    ## The Game constructor.
    #  @param self The object pointer.
    #  @param pos The screen dimensions.
    def __init__(self, screenDim):
        ## The screen's Dimensions.
        self.screenDim = screenDim
        ## The Player instance
        self.player = Player.Player(screenDim * 0.25)

    ## A function to handle the Game input.
    #  @param self The object pointer.
    def input(self, event):
        # If the window is quit or escape is hit.
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            # Exit the game.
            return False

        # If SPACE is hit
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Make the player jump
            self.player.jump()

        # Continue the game.
        return True

    ## A function to update the Game.
    #  @param self The object pointer.
    #  @param dt The delta time.
    #  @returns A true/False value for if the game should continue.
    def update(self, dt):

        # Update the player
        self.player.update(dt)

        # Continue the game.
        return True

    ## A function to draw the Game to the screen.
    #  @param self The object pointer.
    #  @param screen The screen to draw to.
    def draw(self, screen):

        # Draw the player
        self.player.draw(screen)