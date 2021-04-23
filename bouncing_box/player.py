"""A module that contains the class and functions for the Player."""
import pygame


class Player:
    """
    This class contains all of the functions and variables that is used by the
    Player.
    """
    # The Player's sprite. Universal to all instances of Player.
    sprite = pygame.image.load('assets/images/player.png')

    # The Player's Dimensions. Universal to all instances of Player.
    dimensions = pygame.math.Vector2(sprite.get_width(), sprite.get_height())

    # The Player's maximum fall velocity. Universal to all instances of Player.
    maxVelocity = 500.0

    def __init__(self, pos):
        """
        The Player constructor.

        :param pos: The initial value of the Player position.
        :type pos: class:`pygame.math.Vector2`
        """
        # The position of this instance of the Player.
        self.pos = pos
        # The y velocity of this instance of the Player.
        self.velocity = 0.0

    def setPos(self, pos):
        """
        The Player position setter.

        :param pos: The new value of the Player's position.
        :type pos: class:`pygame.math.Vector2`
        """
        self.pos = pos

    def setX(self, x):
        """
        The Player x position setter.

        :param x: The new value of the Player's x position.
        :type x: float
        """
        self.pos.x = x

    def setY(self, y):
        """
        The Player y position setter.

        :param y: The new value of the Player's y position.
        :type y: float
        """
        self.pos.y = y

    def getPos(self):
        """
        The Player position getter.

        :return: The Player's position.
        :rtype: class:`pygame.math.Vector2`
        """
        return self.pos

    def getX(self):
        """
        The Player x position getter.

        :return: The Player's x position.
        :rtype: float
        """
        return self.pos.x

    def getY(self):
        """
        The Player y position getter.

        :return: The Player's y position.
        :rtype: float
        """
        return self.pos.y

    def getDimensions(self):
        """
        The Player Dimensions getter.

        :return: The Player's dimensions.
        :rtype: class:`pygame.math.Vector2`
        """
        return self.dimensions

    def getWidth(self):
        """
        The Player width getter.

        :return: The Player's width.
        :rtype: float
        """
        return self.dimensions.x

    def getHeight(self):
        """
        The Player height getter.

        :return: The Player's height.
        :rtype: float
        """
        return self.dimensions.y

    def jump(self):
        """
        A function to make the player jump by setting the velocity to launch it
        up.
        """
        self.velocity = -750.0

    def update(self, dt):
        """
        A function to update the Player.

        :param dt: The delta time.
        :type dt: float
        """
        # If the velocity is less than the max.
        if self.velocity < self.maxVelocity:
            # Increase the velocity
            self.velocity += 50.0

        # Update the player position on the screen.
        self.pos.y += (self.velocity * dt)

        # Make sure that the Player does not go above the screen
        if self.pos.y < 0.0:
            self.pos.y = 0.0

    def draw(self, screen):
        """
        A function to draw the Player to the screen.

        :param screen: The screen to draw to.
        :type screen: class `pygame.Surface`
        """
        # Draw the sprite to the screen at the current player's position.
        screen.blit(self.sprite, (self.getX(), self.getY()))
