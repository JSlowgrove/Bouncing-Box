import pygame
import Button
import Utilities

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
        ## The credits image.
        self.scoresImage = pygame.image.load('Assets/scores.png')
        ## The scores image.
        self.creditsImage = pygame.image.load('Assets/credits.png')
        ## The play button
        self.playButton = Button.Button(pygame.math.Vector2(199.0, 240.0))
        ## The scores button
        self.scoresButton = Button.Button(pygame.math.Vector2(199.0, 300.0))
        ## The credit button
        self.creditButton = Button.Button(pygame.math.Vector2(199.0, 360.0))
        ## The exit button
        self.exitButton = Button.Button(pygame.math.Vector2(199.0, 420.0))
        ## The return button
        self.returnButton = Button.Button(pygame.math.Vector2(199.0, 420.0))
        ## The play button text
        self.playText = self.font.render("Play", 1, (75, 75, 75))
        ## The exit button text
        self.exitText = self.font.render("Exit", 1, (75, 75, 75))
        ## The credits button text
        self.creditsText = self.font.render("Credits", 1, (75, 75, 75))
        ## The scores button text
        self.scoresText = self.font.render("Scores", 1, (75, 75, 75))
        ## The return button text
        self.returnText = self.font.render("Return", 1, (75, 75, 75))
        ## A boolean for if the game is in the credits
        self.credits = False
        ## A boolean for if the game is in the scores
        self.scores = False
        ## The array of score text
        self.scoresNumTexts = []

    ## A function to handle the Menu input.
    #  @param self The object pointer.
    #  @returns A true/False value for if the game should continue.
    def input(self, event):
        # If the window is quit.
        if event.type == pygame.QUIT:
            # Exit the game.
                return 0

        # If escape is hit.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            #if in scores
            if self.scores:
                #leave scores
                self.scores = False
            #if in credits
            if self.credits:
                #leave credits
                self.credits = False

        # If in the main menu
        if not self.scores and not self.credits:
            # If the play button is pressed.
            if self.playButton.input(event):
                return 2

            # If the credit button is pressed.
            if self.creditButton.input(event):
                self.credits = True

            # If the scores button is pressed.
            if self.scoresButton.input(event):
                self.scores = True
                #Load the scores
                loadedScores = Utilities.loadScores()
                self.scoresNumTexts = [self.font.render("#1 - %d" % int(loadedScores[0]), 1, (19, 42, 107)),
                                       self.font.render("#2 - %d" % int(loadedScores[1]), 1, (19, 42, 107)),
                                       self.font.render("#3 - %d" % int(loadedScores[2]), 1, (19, 42, 107)),
                                       self.font.render("#4 - %d" % int(loadedScores[3]), 1, (19, 42, 107)),
                                       self.font.render("#5 - %d" % int(loadedScores[4]), 1, (19, 42, 107))]

            # If the exit button is pressed.
            if self.exitButton.input(event):
                return 0
        else:
            # If the return button is pressed.
            if self.returnButton.input(event):
                self.scores = False
                self.credits = False

        # Continue the menu.
        return 1

    ## A function to draw the Menu to the screen.
    #  @param self The object pointer.
    #  @param screen The screen to draw to.
    def draw(self, screen):

        #draw the background to the screen.
        screen.blit(self.background, (0.0, 0.0))

        #if in the scores draw the scores menu
        if self.scores:
            #draw the scores to the screen.
            screen.blit(self.scoresImage, (10.0, 10.0))
            #draw the return button
            self.returnButton.draw(screen)
            #draw the return text
            screen.blit(self.returnText, (210, 420))
            #draw the scores
            screen.blit(self.scoresNumTexts[0], (210, 120))
            screen.blit(self.scoresNumTexts[1], (210, 170))
            screen.blit(self.scoresNumTexts[2], (210, 220))
            screen.blit(self.scoresNumTexts[3], (210, 270))
            screen.blit(self.scoresNumTexts[4], (210, 320))

        #if in the credits draw the scores menu
        elif self.credits:
            #draw the credits to the screen.
            screen.blit(self.creditsImage, (10.0, 10.0))
            #draw the return button
            self.returnButton.draw(screen)
            #draw the return text
            screen.blit(self.returnText, (210, 420))

        #else draw the main menu
        else:
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