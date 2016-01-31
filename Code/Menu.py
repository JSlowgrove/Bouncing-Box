import pygame
import Button

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
        ## The play button
        self.playButton = Button.Button(pygame.math.Vector2(199.0, 240.0))
        ## The scores button
        self.scoresButton = Button.Button(pygame.math.Vector2(199.0, 300.0))
        ## The credit button
        self.creditButton = Button.Button(pygame.math.Vector2(199.0, 360.0))
        ## The exit button
        self.exitButton = Button.Button(pygame.math.Vector2(199.0, 420.0))
        # The play button text
        self.playText = self.font.render("Play", 1, (75, 75, 75))
        # The exit button text
        self.exitText = self.font.render("Exit", 1, (75, 75, 75))
        # The credits button text
        self.creditsText = self.font.render("Credits", 1, (75, 75, 75))
        # The scores button text
        self.scoresText = self.font.render("Scores", 1, (75, 75, 75))

    ## A function to handle the Menu input.
    #  @param self The object pointer.
    #  @returns A true/False value for if the game should continue.
    def input(self, event):
        # If the window is quit or escape is hit.
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            # Exit the game.
            return 0

        # If the play button is pressed.
        if self.playButton.input(event):
            return 2

        # If the credit button is pressed.
        if self.creditButton.input(event):
            return 1

        # If the scores button is pressed.
        if self.scoresButton.input(event):
            return 1

        # If the exit button is pressed.
        if self.exitButton.input(event):
            return 0

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
        #draw the play button.
        self.playButton.draw(screen)
        #draw the play text
        screen.blit(self.playText, (210, 240))
        #draw the scores button.
        self.scoresButton.draw(screen)
        #draw the scores text
        screen.blit(self.scoresText, (210, 300))
        #draw the credits button.
        self.creditButton.draw(screen)
        #draw the credits text
        screen.blit(self.creditsText, (210, 360))
        #draw the exit button.
        self.exitButton.draw(screen)
        #draw the exit text
        screen.blit(self.exitText, (210, 420))