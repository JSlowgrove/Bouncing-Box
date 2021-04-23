"""A module that contains the class and functions for the Background."""
import pygame


class Background:
    """
    This class contains all of the functions and variables that is used by the
    Background.
    """
    # The Background's sprite. Universal to all instances of Background.
    sprite = pygame.image.load('assets/images/background.png')

    # The Background's Dimensions. Universal to all instances of Background.
    dimensions = pygame.math.Vector2(sprite.get_width(), sprite.get_height())

    # The Background's velocity. Universal to all instances of Background.
    velocity = 500.0

    def __init__(self, pos):
        """
        The Background constructor.

        :param pos: The initial value of the Background position.
        :type pos: class:`pygame.math.Vector2`
        """
        # The position of this instance of the Background.
        self.pos = pos
        # A boolean for if the Background should be moving.
        self.moving = True

    def setPos(self, pos):
        """
        The Background position setter.

        :param pos: The new value of the Background's position.
        :type pos: class:`pygame.math.Vector2`
        """
        self.pos = pos

    def setX(self, x):
        """
        The Background x position setter.

        :param x: The new value of the Background's x position.
        :type x: float
        """
        self.pos.x = x

    def setY(self, y):
        """
        The Background y position setter.

        :param y: The new value of the Background's y position.
        :type y: float
        """
        self.pos.y = y

    def getPos(self):
        """
        The Background position getter.

        :return: The Background's position.
        :rtype: class:`pygame.math.Vector2`
        """
        return self.pos

    def getX(self):
        """
        The Background x position getter.

        :return: The Background's x position.
        :rtype: float
        """
        return self.pos.x

    def getY(self):
        """
        The Background y position getter.

        :return: The Background's y position.
        :rtype: float
        """
        return self.pos.y

    def getDimensions(self):
        """
        The Background Dimensions getter.

        :return: The Background's dimensions.
        :rtype: class:`pygame.math.Vector2`
        """
        return self.dimensions

    def getWidth(self):
        """
        The Background width getter.

        :return: The Background's width.
        :rtype: float
        """
        return self.dimensions.width

    def getHeight(self):
        """
        The Background height getter.

        :return: The Background's height.
        :rtype: float
        """
        return self.dimensions.height

    def update(self, dt):
        """
        A function to update the Background.

        :param dt: The delta time.
        :type dt: float
        """
        if self.moving:
            self.pos.x -= (self.velocity * dt)

        # Make sure the background loops
        if self.pos.x < -self.dimensions.x:
            self.pos.x += (self.dimensions.x * 2.0)

    def stopBackgroundMoving(self):
        """
        A function to stop the Background from moving by setting the moving
        boolean to false.
        """
        self.moving = False

    def startBackgroundMoving(self):
        """
        A function to start the Background moving by setting the moving boolean
        to true.
        """
        self.moving = True

    def draw(self, screen):
        """
        A function to draw the Background to the screen.
        """
        # Draw the sprite to the screen at the current backgrounds position
        screen.blit(self.sprite, (self.getX(), self.getY()))

    def getMoving(self):
        """
        The Background moving getter.

        :return: If the Background's moving.
        :rtype: bool
        """
        return self.moving
