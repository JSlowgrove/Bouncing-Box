"""A module that contains the class and functions for the GirderManager."""
import pygame
import threading

import bouncing_box.girder as Girder
import bouncing_box.utilities as Utilities

from random import randint


class GirderManager:
    """
    This class contains all of the functions and variables that is used by the
    GirderManager.
    """

    def __init__(self):
        """
        The GirderManager constructor.
        """
        # The array of Girders.
        self.girders = [
            Girder.Girder(pygame.math.Vector2(-100.0, 0.0)),
            Girder.Girder(pygame.math.Vector2(-100.0, 0.0)),
            Girder.Girder(pygame.math.Vector2(-100.0, 0.0)),
            Girder.Girder(pygame.math.Vector2(-100.0, 0.0)),
            Girder.Girder(pygame.math.Vector2(-100.0, 0.0)),
            Girder.Girder(pygame.math.Vector2(-100.0, 0.0)),
            Girder.Girder(pygame.math.Vector2(-100.0, 0.0)),
            Girder.Girder(pygame.math.Vector2(-100.0, 0.0))
        ]

        # A boolean for if girders should be spawn.
        self.spawing = False

        # Start the spawn thread.
        self.spawnThread()

    def spawnThread(self):
        """
        A function for spawning the girders every two seconds.
        """
        # Set the spawnCheck up as a thread that happens every two seconds.
        thread = threading.Timer(2, self.spawnThread)
        # Set it to be a daemon thread so it ends with the other main threads.
        thread.setDaemon(True)
        # Start the thread
        thread.start()

        # Spawn the next girders.
        self.spawnNew()

    def spawnNew(self):
        """
        A function for spawning the new girders.
        """
        # Only spawn if spawning is true.
        if self.spawing:

            # Get a random number for variance.
            rndNum = randint(0, 300)
            # The number of girders spawned.
            numSpawned = 0

            # The y start point.
            yStart = -350.0

            # Loop through all of the girders.
            for i in range(0, len(self.girders)):

                # If a dead girder.
                if not self.girders[i].getStatus():

                    # Revive the girder.
                    self.girders[i].reviveGirder()

                    # Set the y plus the variance.
                    self.girders[i].setY(yStart + float(rndNum))

                    # Increase the number of spawned.
                    numSpawned += 1

                    # Set the y start point to the lower spawn.
                    yStart = 200.0

                    # Only need two to spawn.
                    if numSpawned > 2:
                        break

    def stopSpawing(self):
        """
        A function to stop the Girders from spawning.
        """
        self.spawing = False

    def startSpawing(self):
        """
        A function to start the Girders spawning.
        """
        self.spawing = True

    def update(self, dt):
        """
        A function to update the Girders.

        :param dt: The delta time.
        :type dt: float
        """
        # Loop through all of the girders.
        for i in range(0, len(self.girders)):
            self.girders[i].update(dt)

    def draw(self, screen):
        """
        A function to draw the Girders to the screen.

        :param screen: The screen to draw to.
        :type screen: class `pygame.Surface`
        """
        # Loop through all of the girders.
        for i in range(0, len(self.girders)):
            self.girders[i].draw(screen)

    def resetGirders(self):
        """
        A function to reset the positions of the girders.
        """
        # Loop through all of the girders.
        for i in range(0, len(self.girders)):
            self.girders[i].setPos(pygame.math.Vector2(-100.0, 0.0))

    def checkForScore(self, playerX):
        """
        A function to check if the girder scores a point.

        :param playerX: The player's X position.
        :type playerX: float

        :return: A boolean for if the player scores a point.
        :rtype: bool
        """
        scorePoint = False
        # Loop through all of the girders.
        for i in range(0, len(self.girders)):
            # Check if the girder is to the left of the player and can be
            # scored.
            if (
                playerX > (
                    self.girders[i].getX() + self.girders[i].getWidth()
                ) and self.girders[i].getScoreable()
            ):
                self.girders[i].setScoreable(False)
                scorePoint = True
        return scorePoint

    def collisionCheck(self, playerPos, playerDim):
        """
        A function to check for girder collision.

        :param playerPos: The player's position.
        :type playerPos: class:`pygame.math.Vector2`

        :param playerDim: The player's Dimensions.
        :type playerDim: class:`pygame.math.Vector2`

        :return: If there is a collision.
        :rtype: bool
        """
        # Loop through all of the girders.
        for i in range(0, len(self.girders)):
            # Check for a collision with the player
            if Utilities.rectRectIntersection(
                playerPos,
                playerDim,
                self.girders[i].getPos(),
                self.girders[i].getDimensions()
            ):
                # Loop through all of the girders.
                for j in range(0, len(self.girders)):
                    # Set the girders to not move.
                    self.girders[j].stopGirderMoving()
                # Return collision.
                return True

        # No collision
        return False

    def startGirdersMoving(self):
        """
        A function to start all the girders moving.
        """
        # Loop through all of the girders.
        for i in range(0, len(self.girders)):
            # Set the girders to move.
            self.girders[i].startGirderMoving()

    def stopGirdersMoving(self):
        """
        A function to stop all the girders moving.
        """
        # Loop through all of the girders.
        for i in range(0, len(self.girders)):
            # Set the girders to not move.
            self.girders[i].stopGirderMoving()
