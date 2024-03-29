"""A module that contains the class and functions for the Game."""
import pygame

import bouncing_box.player as Player
import bouncing_box.background as Background
import bouncing_box.utilities as Utilities
import bouncing_box.button as Button
import bouncing_box.girder_manager as GirderManager


class Game:
    """
    This class contains all of the functions and variables that is used by the
    Game.
    """

    def __init__(self, screenDim):
        """
        The Game constructor.

        :param screenDim: The The Game constructor..
        :type screenDim: class:`pygame.math.Vector2`
        """
        # The screen's Dimensions.
        self.screenDim = screenDim
        # The Player instance.
        self.player = Player.Player(self.screenDim * 0.25)
        # The first Background instance.
        self.background1 = Background.Background(pygame.math.Vector2(0.0, 0.0))
        # The second Background instance.
        self.background2 = Background.Background(
            pygame.math.Vector2(640.0, 0.0)
        )
        # The games score.
        self.score = 0
        # Set up font.
        self.font = pygame.font.Font("assets/fonts/isl_jupiter.ttf", 36)
        # Update out the score display.
        self.displayScore = self.font.render(
            "Score: " + str(self.score), 1, (75, 75, 75)
        )
        # The jump sound effect.
        self.jumpSound = pygame.mixer.Sound('assets/audio/jump.ogg')
        # The crash sound effect.
        self.crashSound = pygame.mixer.Sound('assets/audio/crash.ogg')
        # The score sound effect.
        self.scoreSound = pygame.mixer.Sound('assets/audio/score.ogg')
        # The end game image.
        self.endGame = pygame.image.load('assets/images/end_game.png')
        # The GirderManager.
        self.girderManager = GirderManager.GirderManager()
        # A boolean for if the game has ended.
        self.gameEnd = False
        # The retry button.
        self.retryButton = Button.Button(pygame.math.Vector2(199.0, 240.0))
        # The exit button.
        self.exitButton = Button.Button(pygame.math.Vector2(199.0, 300.0))
        # The retry button text.
        self.retryText = self.font.render("Retry", 1, (75, 75, 75))
        # The quit button text.
        self.exitText = self.font.render("Exit", 1, (75, 75, 75))

    def stopSpawing(self):
        """
        A function to stop the Girders from spawning.
        """
        self.girderManager.stopSpawing()

    def startSpawing(self):
        """
        A function to start the Girders spawning.
        """
        self.girderManager.startSpawing()

    def resetGirders(self):
        """
        A function to reset the Girders.
        """
        self.girderManager.resetGirders()

    def reset(self):
        """
        A function to reset the game movement.
        """
        self.startSpawing()
        self.resetGirders()
        self.girderManager.startGirdersMoving()
        self.background1.startBackgroundMoving()
        self.background2.startBackgroundMoving()
        self.gameEnd = False
        self.player.setY(self.screenDim.y * 0.25)
        self.score = 0

    def input(self, event):
        """
        A function to handle the Game input.

        :param screenDim: A number for if the next state of the game
            (0 = quit, 1 = menu, 2 = game).
        :type screenDim: int
        """
        # If the window is quit.
        if event.type == pygame.QUIT:
            # Exit the game.
            return 0

        # If escape is hit.
        if (
            event.type == pygame.QUIT
            or event.type == pygame.KEYDOWN
            and event.key == pygame.K_ESCAPE
        ):
            # Return to the menu.
            return 1

        # If SPACE is hit.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # If the player can move
            if self.background1.getMoving():
                # Jump sound effect.
                self.jumpSound.play()
                # Make the player jump.
                self.player.jump()

        # If game end.
        if self.gameEnd:
            # If the exit button is pressed.
            if self.exitButton.input(event):
                return 1
            # If the exit button is pressed.
            if self.retryButton.input(event):
                self.reset()

        # Continue the game.
        return 2

    def update(self, dt):
        """
        A function to update the Game.

        :param dt: The delta time.
        :type dt: float

        :returns: A number for if the next state of the game
            (0 = quit, 1 = menu, 2 = game).
        :rtype: int
        """
        # Update the Backgrounds.
        self.background1.update(dt)
        self.background2.update(dt)

        # Update the girder manager.
        self.girderManager.update(dt)

        # Update the player.
        self.player.update(dt)

        # Check for collision with the girders.
        if self.girderManager.collisionCheck(
            self.player.getPos(), self.player.getDimensions()
        ):
            # If the game has not ended.
            if not self.gameEnd:
                # Play the collision sound.
                self.crashSound.play()
                # Stop the player moving right.
                self.background1.stopBackgroundMoving()
                self.background2.stopBackgroundMoving()
                self.girderManager.stopGirdersMoving()
                # Set the game to end.
                self.gameEnd = True
                # Save the new scores.
                Utilities.sortScores(self.score)

        # If the player falls of the screen end the game and game has not
        # ended.
        if self.player.getY() > self.screenDim.y and not self.gameEnd:
            # Play the collision sound.
            self.crashSound.play()
            # Stop the player moving right.
            self.background1.stopBackgroundMoving()
            self.background2.stopBackgroundMoving()
            self.girderManager.stopGirdersMoving()
            # Set the game to end.
            self.gameEnd = True
            # Save the new scores.
            Utilities.sortScores(self.score)

        # Check for if a score increases.
        if self.girderManager.checkForScore(self.player.getX()):
            # Play the collision sound.
            self.scoreSound.play()
            # Increase the score.
            self.score += 1

        # Update out the score display.
        self.displayScore = self.font.render(
            "Score: " + str(self.score), 1, (75, 75, 75)
        )

        # Continue the game.
        return 2

    def draw(self, screen):
        """
        A function to draw the Game to the screen.

        :param screen: The screen to draw to.
        :type screen: class `pygame.Surface`
        """
        # Draw the backgrounds.
        self.background1.draw(screen)
        self.background2.draw(screen)

        # Update the girder manager.
        self.girderManager.draw(screen)

        # Draw the player.
        self.player.draw(screen)

        if self.gameEnd:
            # Draw the end game box.
            screen.blit(self.endGame, (110, 84))
            # Draw the score.
            screen.blit(self.displayScore, (265, 180))
            # Draw the buttons.
            self.retryButton.draw(screen)
            self.exitButton.draw(screen)
            # Draw the buttons text.
            screen.blit(self.retryText, (210, 240))
            screen.blit(self.exitText, (210, 300))
        else:
            # Draw the score.
            screen.blit(self.displayScore, (10, 10))
