"""A module that contains the class and functions for the Girder."""
import pygame


class Girder:
    """
    This class contains all of the functions and variables that is used by the
    Girder.
    """
    # The Girder's sprite. Universal to all instances of Girder.
    sprite = pygame.image.load('assets/images/girder.png')

    # The Girder's Dimensions. Universal to all instances of Girder.
    dimensions = pygame.math.Vector2(sprite.get_width(), sprite.get_height())

    # The Girder's velocity. Universal to all instances of Girder.
    velocity = 700.0

    def __init__(self, pos):
        """
        The Girder constructor.

        :param pos: The initial value of the Girder position.
        :type pos: class:`pygame.math.Vector2`
        """
        # The position of this instance of the Girder.
        self.pos = pos
        # A boolean for if the Girder should be moving.
        self.moving = True
        # A boolean for if the Girder is dead.
        self.dead = True
        # A boolean for if the Girder is scoreable.
        self.scoreable = False

    def setScoreable(self, scoreable):
        """
        The Girder scoreable setter.

        :param scoreable: If the Girder can be scored.
        :type scoreable: bool
        """
        self.scoreable = scoreable

    def getScoreable(self):
        """
        The Girder scoreable getter.

        :returns: If the Girder can be scored.
        :rtype: bool
        """
        return self.scoreable

    def getMoving(self):
        """
        The Girder moving getter.

        :return: The Girder's moving boolean.
        :rtype: bool
        """
        return self.moving

    def setPos(self, pos):
        """
        The Girder position setter.

        :param pos: The new value of the Girder's position.
        :type pos: class:`pygame.math.Vector2`
        """
        self.pos = pos

    def setX(self, x):
        """
        The Girder x position setter.

        :param x: The new value of the Girder's x position.
        :type x: float
        """
        self.pos.x = x

    def setY(self, y):
        """
        The Girder y position setter.

        :param scoreable: The new value of the Girder's y position.
        :type scoreable: float
        """
        self.pos.y = y

    def getPos(self):
        """
        The Girder position getter.

        :return: The Girder's position.
        :rtype: class:`pygame.math.Vector2`
        """
        return self.pos

    def getX(self):
        """
        The Girder x position getter.

        :return: The Girder's x position.
        :rtype: float
        """
        return self.pos.x

    def getY(self):
        """
        The Girder y position getter.

        :return: The Girder's y position.
        :rtype: float
        """
        return self.pos.y

    def getDimensions(self):
        """
        The Girder Dimensions getter.

        :return: The Girder's dimensions.
        :rtype: class:`pygame.math.Vector2`
        """
        return self.dimensions

    def getWidth(self):
        """
        The Girder width getter.

        :return: The Girder's width.
        :rtype: float
        """
        return self.dimensions.x

    def getHeight(self):
        """
        The Girder height getter.

        :return: The Girder's height.
        :rtype: float
        """
        return self.dimensions.y

    def getStatus(self):
        """
        The Girder status getter.

        :return: The Girder's dead boolean.
        :rtype: bool
        """
        return self.dead

    def update(self, dt):
        """
        A function to update the Girder.

        :param dt: The delta time.
        :type dt: float
        """
        if self.moving and self.getStatus():
            self.pos.x -= (self.velocity * dt)

        # Set to dead if off the screen
        if self.pos.x < (0.0 - self.dimensions.x):
            self.killGirder()
            self.setX(640.0)
            self.setScoreable(True)

    def stopGirderMoving(self):
        """
         A function to stop the Girder from moving by setting the moving
         boolean to false.
        """
        self.moving = False

    def startGirderMoving(self):
        """
        A function to start the Girder moving by setting the moving boolean to
        true.
        """
        self.moving = True

    def killGirder(self):
        """
        A function to set the as Girder dead by setting the dead boolean to
        true.
        """
        self.dead = False

    def reviveGirder(self):
        """
        A function to set the as Girder alive by setting the dead boolean to
        false.
        """
        self.dead = True

    def draw(self, screen):
        """
        A function to draw the Girder to the screen.

        :param screen: The screen to draw to.
        :type screen: class `pygame.Surface`
        """
        # Draw the sprite to the screen at the current girders position
        screen.blit(self.sprite, (self.getX(), self.getY()))
