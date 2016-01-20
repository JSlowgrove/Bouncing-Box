import pygame

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

    ## A function to handle the Game input.
    #  @param self The object pointer.
    def input(self, event):
        # If the window is quit.
        if event.type == pygame.QUIT:
            # Exit the game.
            return False

        # Continue the game.
        return True

    ## A function to update the Game.
    #  @param self The object pointer.
    #  @param dt The delta time.
    #  @returns A true/False value for if the game should continue.
    def update(self, dt):

        # Continue the game.
        return True

    ## A function to draw the Game to the screen.
    #  @param self The object pointer.
    #  @param screen The screen to draw to.
    def draw(self, screen):
        return