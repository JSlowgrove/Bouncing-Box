import Girder
import pygame
import threading
from random import randint

## Documentation for the GirderManager class.
#
#  This class contains all of the functions and variables that is used by the GirderManager.
class GirderManager:

    ## The GirderManager constructor.
    #  @param self The object pointer.
    def __init__(self):
        ## The array of Girders.
        self.girders = [Girder.Girder(pygame.math.Vector2(-100.0, 0.0)), Girder.Girder(pygame.math.Vector2(-100.0, 0.0)),
                        Girder.Girder(pygame.math.Vector2(-100.0, 0.0)), Girder.Girder(pygame.math.Vector2(-100.0, 0.0)),
                        Girder.Girder(pygame.math.Vector2(-100.0, 0.0)), Girder.Girder(pygame.math.Vector2(-100.0, 0.0)),
                        Girder.Girder(pygame.math.Vector2(-1000.0, 0.0)), Girder.Girder(pygame.math.Vector2(-100.0, 0.0))]

        ## A boolean for if girders should be spawn.
        self.spawing = False

        # Start the spawn thread.
        self.spawnThread()

    ## A function for spawning the girders every two seconds.
    #  @param self The object pointer.
    def spawnThread(self):
        # Set the spawnCheck up as a thread that happens every two seconds.
        thread = threading.Timer(2, self.spawnThread)
        # Set it to be a daemon thread so it ends with the other main threads.
        thread.setDaemon(True)
        # Start the thread
        thread.start()

        # Spawn the next girders.
        self.spawnNew()

    ## A function for spawning the new girders.
    #  @param self The object pointer.
    def spawnNew(self):
        #Only spawn if spawning is true.
        if self.spawing:

            # Get a random number for variance.
            rndNum = randint(0,300)
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
                    yStart = 175.0

                    # Only need two to spawn.
                    if numSpawned > 2:
                        break

    ## A function to stop the Girders from spawning.
    #  @param self The object pointer.
    def stopSpawing(self):
        self.spawing = False

    ## A function to start the Girders spawning.
    #  @param self The object pointer.
    def startSpawing(self):
        self.spawing = True

    ## A function to update the Girders.
    #  @param self The object pointer.
    #  @param dt The delta time.
    def update(self, dt):
        # Loop through all of the girders.
        for i in range(0, len(self.girders)):
            self.girders[i].update(dt)

    ## A function to draw the Girders to the screen.
    #  @param self The object pointer.
    #  @param screen The screen to draw to.
    def draw(self, screen):
        # Loop through all of the girders.
        for i in range(0, len(self.girders)):
            self.girders[i].draw(screen)

    ## A function to reset the positions of the girders.
    #  @param self The object pointer.
    def resetGirders(self):
        # Loop through all of the girders.
        for i in range(0, len(self.girders)):
            self.girders[i].setPos(pygame.math.Vector2(-1000.0, 0.0))