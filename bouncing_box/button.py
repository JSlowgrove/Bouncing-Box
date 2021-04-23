"""A module that contains the class and functions for the Button."""
import pygame


class Button:
    """
    This class contains all of the functions and variables that is used by the
    Button.
    """
    # The Button's sprite. Universal to all instances of Button.
    sprite = pygame.image.load('assets/images/button.png')

    # The Button's pressed sprite. Universal to all instances of Button.
    pressedSprite = pygame.image.load('assets/images/button_pressed.png')

    # The Button's Dimensions. Universal to all instances of Button.
    dimensions = pygame.math.Vector2(sprite.get_width(), sprite.get_height())

    # The mouse's position. Universal to all instances of Button.
    mousePos = pygame.math.Vector2(0.0, 0.0)

    def __init__(self, pos):
        """
        The Button constructor.

        :param pos: The initial value of the Button position.
        :type pos: class:`pygame.math.Vector2`
        """
        # The position of this instance of the Button.
        self.pos = pos
        # A boolean for the current state of the Button.
        self.pressed = False
        # A boolean for if the mouse is over the button.
        self.overButton = False

    def setPos(self, pos):
        """
        The Button position setter.

        :param pos: The new value of the Button's position.
        :type pos: class:`pygame.math.Vector2`
        """
        self.pos = pos

    def setX(self, x):
        """
        The Button x position setter.

        :param x: The new value of the Button's x position.
        :type x: float
        """
        self.pos.x = x

    def setY(self, y):
        """
        The Button y position setter.

        :param y: The new value of the Button's y position.
        :type y: float
        """
        self.pos.y = y

    def getPos(self):
        """
        The Button position getter.

        :return: The Button's position.
        :rtype: class:`pygame.math.Vector2`
        """
        return self.pos

    def getX(self):
        """
        The Button x position getter.

        :return: The Button's x position.
        :rtype: float
        """
        return self.pos.x

    def getY(self):
        """
        The Button y position getter.

        :return: The Button's y position.
        :rtype: float
        """
        return self.pos.y

    def getDimensions(self):
        """
        The Button Dimensions getter.

        :return: The Button's dimensions..
        :rtype: class:`pygame.math.Vector2`
        """
        return self.dimensions

    def getWidth(self):
        """
        The Button width getter.

        :return: The Button's width.
        :rtype: float
        """
        return self.dimensions.x

    def getHeight(self):
        """
        The Button height getter.

        :return: The Button's height.
        :rtype: float
        """
        return self.dimensions.y

    def input(self, event):
        """
        A function to handle the Button's input.

        :return: The input event.
        :rtype: class `Event`
        """
        # Get the new mouse position as a tuple.
        tupleMousePos = pygame.mouse.get_pos()

        # Store the new mouse position as a vector2.
        self.mousePos = pygame.math.Vector2(
            float(tupleMousePos[0]),
            float(tupleMousePos[1])
        )

        # Check the mouse to see if it is over the button.
        self.checkMouseButtonPos()

        # If the mouse is pressed.
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Left click.
            if event.button == 1:
                # The button is pressed.
                self.pressed = True

        # The button is pressed.
        if self.pressed:
            # If the mouse is released.
            if event.type == pygame.MOUSEBUTTONUP:
                # Left click.
                if event.button == 1:
                    # Reset the value of pressed.
                    self.pressed = False

                    # Check if the mouse is over the button.
                    if self.overButton:
                        # The button has been selected.
                        return True

        # The button has not yet been selected.
        return False

    def draw(self, screen):
        """
        A function to draw the Button to the screen.

        :param screen: The screen to draw to.
        :type screen: class `pygame.Surface`
        """
        # Check if the button is pressed.
        if self.overButton:
            # Draw the pressed sprite to the screen at the current position.
            screen.blit(self.pressedSprite, (self.getX(), self.getY()))
        else:
            # Draw the sprite to the screen at the current position.
            screen.blit(self.sprite, (self.getX(), self.getY()))

    def checkMouseButtonPos(self):
        """
        A function to check if the mouse is over the button.

        :return: If the mouse is over the button.
        :rtype: bool
        """
        # Check if the mouse is not over the button.
        if (
            self.mousePos.x > (self.getX() + self.getWidth())
            or self.mousePos.x < self.getX()
            or self.mousePos.y > (self.getY() + self.getHeight())
            or self.mousePos.y < self.getY()
        ):
            # The mouse is not over the button.
            self.overButton = False

        else:
            # The mouse is over the button.
            self.overButton = True
