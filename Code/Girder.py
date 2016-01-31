import pygame

## Documentation for the Girder class.
#
#  This class contains all of the functions and variables that is used by the Girder.
class Girder:

    ##The Girder's sprite. Universal to all instances of Girder.
    sprite = pygame.image.load('Assets/girder.png')

    ##The Girder's Dimensions. Universal to all instances of Girder.
    dimensions = pygame.math.Vector2(sprite.get_width(), sprite.get_height())

    ##The Girder's velocity. Universal to all instances of Girder.
    velocity = 700.0

    ## The Girder constructor.
    #  @param self The object pointer.
    #  @param pos The initial value of the Girder position.
    def __init__(self, pos):
        ## @var The position of this instance of the Girder.
        self.pos = pos
        ##A boolean for if the Girder should be moving.
        self.moving = True
        ##A boolean for if the Girder is dead.
        self.dead = True

    ## The Girder moving getter.
    #  @param self The object pointer.
    #  @return The Girder's moving boolean.
    def getMoving(self):
        return self.moving

    ## The Girder position setter.
    #  @param self The object pointer.
    #  @param pos The new value of the Girder's position.
    def setPos(self,pos):
        self.pos = pos

    ## The Girder x position setter.
    #  @param self The object pointer.
    #  @param x The new value of the Girder's x position.
    def setX(self, x):
        self.pos.x = x

    ## The Girder y position setter.
    #  @param self The object pointer.
    #  @param y The new value of the Girder's y position.
    def setY(self, y):
        self.pos.y = y

    ## The Girder position getter.
    #  @param self The object pointer.
    #  @return The Girder's position.
    def getPos(self):
        return self.pos

    ## The Girder x position getter.
    #  @param self The object pointer.
    #  @return The Girder's x position.
    def getX(self):
        return self.pos.x

    ## The Girder y position getter.
    #  @param self The object pointer.
    #  @return The Girder's y position.
    def getY(self):
        return self.pos.y

    ## The Girder Dimensions getter.
    #  @param self The object pointer.
    #  @return The Girder's dimensions.
    def getDimensions(self):
        return self.dimensions

    ## The Girder width getter.
    #  @param self The object pointer.
    #  @return The Girder's width.
    def getWidth(self):
        return self.dimensions.width

    ## The Girder height getter.
    #  @param self The object pointer.
    #  @return The Girder's height.
    def getHeight(self):
        return self.dimensions.height

    ## The Girder status getter.
    #  @param self The object pointer.
    #  @return The Girder's dead boolean.
    def getStatus(self):
        return self.dead

    ## A function to update the Girder.
    #  @param self The object pointer.
    #  @param dt The delta time.
    def update(self, dt):
        if self.moving and self.getStatus():
            self.pos.x -= (self.velocity * dt)

        # Set to dead if off the screen
        if self.pos.x < (0.0 - self.dimensions.x):
            self.killGirder()
            self.setX(640.0)

    ## A function to stop the Girder from moving by setting the moving boolean to false.
    #  @param self The object pointer.
    def stopGirderMoving(self):
        self.moving = False

    ## A function to start the Girder moving by setting the moving boolean to true.
    #  @param self The object pointer.
    def startGirderMoving(self):
        self.moving = True

    ## A function to set the as Girder dead by setting the dead boolean to true.
    #  @param self The object pointer.
    def killGirder(self):
        self.dead = False

    ## A function to set the as Girder alive by setting the dead boolean to false.
    #  @param self The object pointer.
    def reviveGirder(self):
        self.dead = True

    ## A function to draw the Girder to the screen.
    #  @param self The object pointer.
    def draw(self, screen):
        #draw the sprite to the screen at the current girders position
        screen.blit(self.sprite, (self.getX(), self.getY()))