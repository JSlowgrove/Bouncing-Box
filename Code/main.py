import pygame
import Game
from pygame.locals import *

def main():
    # Initialise the clock.
    clock = pygame.time.Clock()

    #Initalise variables for Debug FPS Info.
    FPS = 60
    seconds = 0

    # Used to correctly implement seconds.
    pygame.time.set_timer(USEREVENT + 1, 1000)

    # Initialise PyGame.
    pygame.init()
    # Set window title.
    pygame.display.set_caption("Bouncing Box")

    # The screen dimensions.
    screenDim = pygame.math.Vector2(640, 480)
    # Initialise the screen using the screen dimensions.
    screen = pygame.display.set_mode((int(screenDim.x), int(screenDim.y)))

    # Set up font
    font = pygame.font.Font("Assets/isl_jupiter.ttf", 36)

    # Boolean for Debug FPS Info display.
    displayDebug = False

    # The boolean for keeping the game running.
    running = True
    # Initialise the game state.
    state = Game.Game(screenDim)

    while running:
        # Keep the game running at the same FPS
        clock.tick(FPS)

        # Update out the Debug FPS Info
        time_display = font.render("Time: " + str(clock.get_time()), 1, (0, 0, 0))
        rawtime_display = font.render("Raw Time: " + str(clock.get_rawtime()), 1, (0, 0, 0))
        fps_display = font.render("FPS: " + str(clock.get_fps()), 1, (0, 0, 0))
        pygame_total_ticks_display = font.render("Pygame Ticks (total): " + str(pygame.time.get_ticks()), 1, (0, 0, 0))
        seconds_display = font.render("Seconds: " + str(seconds), 1, (0, 0, 0))

        # Work out the Delta Time.
        dt = clock.get_rawtime() / 1000.0

        # A hack to keep the game playable when Python stutters.
        if dt > 0.01:
            dt = 0.01

        # Handle the PyGame input events.
        for event in pygame.event.get():
            # Set the state of running to the game input.
            running = state.input(event)

            # Check for the Input Event to toggle Debug mode.
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                displayDebug = not displayDebug

        # If the game is still running.
        if running:
            # Set the state of running to the game update.
            running = state.update(dt)

        # Clear the screen.
        screen.fill((252, 0, 0))

        # Draw the game to the screen.
        state.draw(screen)

        # Display the Debug FPS Info.
        if displayDebug:
            screen.blit(rawtime_display, (10, 35))
            screen.blit(fps_display, (10, 60))
            screen.blit(pygame_total_ticks_display, (10, 85))
            screen.blit(seconds_display, (10, 110))
            screen.blit(time_display, (10, 135))

        # Double buffer the screen to the window.
        pygame.display.flip()

main()
quit()
