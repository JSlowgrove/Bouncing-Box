import pygame

## Documentation for the Background class.
#
#  This class contains all of the functions and variables that is used by the Background.
class Background:

    ##The Background's sprite. Universal to all instances of Background.
    sprite = pygame.image.load('Assets/background.png')

    ##The Background's Dimensions. Universal to all instances of Background.
    dimensions = pygame.math.Vector2(sprite.get_width(), sprite.get_height())

    ##The Background's velocity. Universal to all instances of Background.
    velocity = 500.0

    ## The Background constructor.
    #  @param self The object pointer.
    #  @param pos The initial value of the Background position.
    def __init__(self, pos):
        ## @var The position of this instance of the Background.
        self.pos = pos
        ##A boolean for if the Background should be moving.
        self.moving = True

    ## The Background position setter.
    #  @param self The object pointer.
    #  @param pos The new value of the Background's position.
    def setPos(self,pos):
        self.pos = pos

    ## The Background x position setter.
    #  @param self The object pointer.
    #  @param x The new value of the Background's x position.
    def setX(self, x):
        self.pos.x = x

    ## The Background y position setter.
    #  @param self The object pointer.
    #  @param y The new value of the Background's y position.
    def setY(self, y):
        self.pos.y = y

    ## The Background position getter.
    #  @param self The object pointer.
    #  @return The Background's position.
    def getPos(self):
        return self.pos

    ## The Background x position getter.
    #  @param self The object pointer.
    #  @return The Background's x position.
    def getX(self):
        return self.pos.x

    ## The Background y position getter.
    #  @param self The object pointer.
    #  @return The Background's y position.
    def getY(self):
        return self.pos.y

    ## The Background Dimensions getter.
    #  @param self The object pointer.
    #  @return The Background's dimensions.
    def getDimensions(self):
        return self.dimensions

    ## The Background width getter.
    #  @param self The object pointer.
    #  @return The Background's width.
    def getWidth(self):
        return self.dimensions.width

    ## The Background height getter.
    #  @param self The object pointer.
    #  @return The Background's height.
    def getHeight(self):
        return self.dimensions.height

    ## A function to update the Background.
    #  @param self The object pointer.
    #  @param dt The delta time.
    def update(self, dt):
        if self.moving:
            self.pos.x -= (self.velocity * dt)

        # Make sure the background loops
        if self.pos.x < -self.dimensions.x:
            self.pos.x += (self.dimensions.x * 2.0)

    ## A function to stop the Background from moving by setting the moving boolean to false.
    #  @param self The object pointer.
    def stopBackgroundMoving(self):
        self.moving = False

    ## A function to start the Background moving by setting the moving boolean to true.
    #  @param self The object pointer.
    def startBackgroundMoving(self):
        self.moving = True

    ## A function to draw the Background to the screen.
    #  @param self The object pointer.
    def draw(self, screen):
        #draw the sprite to the screen at the current backgrounds position
        screen.blit(self.sprite, (self.getX(), self.getY()))