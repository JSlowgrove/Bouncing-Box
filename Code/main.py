import time
import pygame
import Game

# Initialise the clock.
lastTime = time.clock()

# Initialise PyGame.
pygame.init()

# The screen dimensions.
screenDim = pygame.math.Vector2(640, 480)
# Initialise the screen using the screen dimensions.
screen = pygame.display.set_mode((int(screenDim.x), int(screenDim.y)))

# The boolean for keeping the game running.
running = True
# Initialise the game state.
state = Game.Game(screenDim)

# The main loop.
while running:
    # Set the current time.
    currentTime = time.clock()
    # Work out the delta time.
    dt = currentTime - lastTime
    # Set the last time to the current time
    lastTime = currentTime

    # Handle the PyGame input events.
    for event in pygame.event.get():
        # Set the state of running to the game input.
        running = state.input(event)

    # If the game is still running.
    if running:
        # Set the state of running to the game update.
        running = state.update(dt)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the game to the screen.
    state.draw(screen)

    # Double buffer the screen to the window.
    pygame.display.flip()

    # Frame rate limiter
    if dt < (1.0 / 50.0):
        time.sleep((1.0 / 50.0) - dt)
