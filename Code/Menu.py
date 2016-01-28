import pygame

## Documentation for the Menu class.
#
#  This class contains all of the functions and variables that is used by the Menu.
class Menu:

    ## The Menu constructor.
    #  @param self The object pointer.
    #  @param pos The screen dimensions.
    def __init__(self, screenDim):
        ## The screen's Dimensions.
        self.screenDim = screenDim
        ## Set up font.
        self.font = pygame.font.Font("Assets/isl_jupiter.ttf", 36)
        ## The background's image.
        self.background = pygame.image.load('Assets/menuBackground.png')
        ## The logo image.
        self.logo = pygame.image.load('Assets/logo.png')

    ## A function to handle the Menu input.
    #  @param self The object pointer.
    #  @returns A true/False value for if the game should continue.
    def input(self, event):
        # If the window is quit or escape is hit.
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            # Exit the game.
            return 0

        # If ENTER is hit.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return 2

        # Continue the menu.
        return 1

    ## A function to update the Menu.
    #  @param self The object pointer.
    #  @param dt The delta time.
    #  @returns A true/False value for if the game should continue.
    def update(self, dt):

        # Continue the menu.
        return 1

    ## A function to draw the Menu to the screen.
    #  @param self The object pointer.
    #  @param screen The screen to draw to.
    def draw(self, screen):

        #draw the background to the screen.
        screen.blit(self.background, (0.0, 0.0))
        #draw the logo to the screen.
        screen.blit(self.logo, (158.0, 40.0))