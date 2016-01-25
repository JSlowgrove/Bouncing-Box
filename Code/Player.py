import pygame

## Documentation for the Player class.
#
#  This class contains all of the functions and variables that is used by the Player.
class Player:

    ##The Player's sprite. Universal to all instances of Player.
    sprite = pygame.image.load('Assets/player.png')

    ##The Player's Dimensions. Universal to all instances of Player.
    dimensions = pygame.math.Vector2(sprite.get_width(), sprite.get_height())

    ##The Player's maximum fall velocity. Universal to all instances of Player.
    maxVelocity = 1000.0

    ## The Player constructor.
    #  @param self The object pointer.
    #  @param pos The initial value of the Player position.
    def __init__(self, pos):
        ## @var The position of this instance of the Player.
        self.pos = pos
        ## @var The y velocity of this instance of the Player.
        self.velocity = 0.0

    ## The Player position setter.
    #  @param self The object pointer.
    #  @param pos The new value of the Player's position.
    def setPos(self,pos):
        self.pos = pos

    ## The Player x position setter.
    #  @param self The object pointer.
    #  @param x The new value of the Player's x position.
    def setX(self, x):
        self.pos.x = x

    ## The Player y position setter.
    #  @param self The object pointer.
    #  @param y The new value of the Player's y position.
    def setY(self, y):
        self.pos.y = y

    ## The Player position getter.
    #  @param self The object pointer.
    #  @return The Player's position.
    def getPos(self):
        return self.pos

    ## The Player x position getter.
    #  @param self The object pointer.
    #  @return The Player's x position.
    def getX(self):
        return self.pos.x

    ## The Player y position getter.
    #  @param self The object pointer.
    #  @return The Player's y position.
    def getY(self):
        return self.pos.y

    ## The Player Dimensions getter.
    #  @param self The object pointer.
    #  @return The Player's dimensions.
    def getDimensions(self):
        return self.dimensions

    ## The Player width getter.
    #  @param self The object pointer.
    #  @return The Player's width.
    def getWidth(self):
        return self.dimensions.x

    ## The Player height getter.
    #  @param self The object pointer.
    #  @return The Player's height.
    def getHeight(self):
        return self.dimensions.y

    ## A function to make the player jump by setting the velocity to launch it up.
    #  @param self The object pointer.
    def jump(self):
        self.velocity = -1000.0

    ## A function to update the Player.
    #  @param self The object pointer.
    #  @param dt The delta time.
    def update(self, dt):
        #If the velocity is less than the max.
        if self.velocity < self.maxVelocity:
            #Increase the velocity
            self.velocity += 50.0

        #Update the player position on the screen.
        self.pos.y += (self.velocity * dt)

        #Make sure that the Player does not go above the screen
        if self.pos.y < 0.0:
            self.pos.y = 0.0

    ## A function to draw the Player to the screen.
    #  @param self The object pointer.
    def draw(self, screen):
        #draw the sprite to the screen at the current player's position.
        screen.blit(self.sprite, (self.getX(), self.getY()))