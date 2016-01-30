import pygame

## Documentation for the Button class.
#
#  This class contains all of the functions and variables that is used by the Button.
class Button:

    ##The Button's sprite. Universal to all instances of Button.
    sprite = pygame.image.load('Assets/button.png')

    ##The Button's pressed sprite. Universal to all instances of Button.
    pressedSprite = pygame.image.load('Assets/buttonPressed.png')

    ##The Button's Dimensions. Universal to all instances of Button.
    dimensions = pygame.math.Vector2(sprite.get_width(), sprite.get_height())

    ##The mouse's position. Universal to all instances of Button.
    mousePos = pygame.math.Vector2(0.0, 0.0)

    ## The Button constructor.
    #  @param self The object pointer.
    #  @param pos The initial value of the Button position.
    def __init__(self, pos):
        ## @var The position of this instance of the Button.
        self.pos = pos
        ##A boolean for the current state of the Button.
        self.pressed = False
        ##A boolean for if the mouse is over the button.
        self.overButton = False

    ## The Button position setter.
    #  @param self The object pointer.
    #  @param pos The new value of the Button's position.
    def setPos(self,pos):
        self.pos = pos

    ## The Button x position setter.
    #  @param self The object pointer.
    #  @param x The new value of the Button's x position.
    def setX(self, x):
        self.pos.x = x

    ## The Button y position setter.
    #  @param self The object pointer.
    #  @param y The new value of the Button's y position.
    def setY(self, y):
        self.pos.y = y

    ## The Button position getter.
    #  @param self The object pointer.
    #  @return The Button's position.
    def getPos(self):
        return self.pos

    ## The Button x position getter.
    #  @param self The object pointer.
    #  @return The Button's x position.
    def getX(self):
        return self.pos.x

    ## The Button y position getter.
    #  @param self The object pointer.
    #  @return The Button's y position.
    def getY(self):
        return self.pos.y

    ## The Button Dimensions getter.
    #  @param self The object pointer.
    #  @return The Button's dimensions.
    def getDimensions(self):
        return self.dimensions

    ## The Button width getter.
    #  @param self The object pointer.
    #  @return The Button's width.
    def getWidth(self):
        return self.dimensions.x

    ## The Button height getter.
    #  @param self The object pointer.
    #  @return The Button's height.
    def getHeight(self):
        return self.dimensions.y

    ## A function to handle the Button's input.
    #  @param self The object pointer.
    #  @param dt The delta time.
    def input(self, event):

        # Get the new mouse position as a tuple.
        tupleMousePos = pygame.mouse.get_pos()

        # Store the new mouse position as a vector2.
        self.mousePos = pygame.math.Vector2(float(tupleMousePos[0]), float(tupleMousePos[1]))

        # Check the mouse to see if it is over the button.
        self.checkMouseButtonPos()

        # If the mouse is pressed.
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Left click.
            if event.button == 1:
                #The button is pressed.
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

    ## A function to draw the Button to the screen.
    #  @param self The object pointer.
    def draw(self, screen):
        #Check if the button is pressed.
        if self.overButton:
            #draw the pressed sprite to the screen at the current position.
            screen.blit(self.pressedSprite, (self.getX(), self.getY()))
        else:
            #draw the sprite to the screen at the current position.
            screen.blit(self.sprite, (self.getX(), self.getY()))

    ## A function to check if the mouse is over the button.
    #  @param self The object pointer.
    #  @return If the mouse is over the button.
    def checkMouseButtonPos(self):

        #Check if the mouse is not over the button.
        if self.mousePos.x > (self.getX() + self.getWidth()) or self.mousePos.x < self.getX() \
                or self.mousePos.y > (self.getY() + self.getHeight()) or self.mousePos.y < self.getY():
            # The mouse is not over the button.
            self.overButton = False

        else:
            # The mouse is over the button.
            self.overButton = True