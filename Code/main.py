import pygame
import Game
import Menu
from pygame.locals import *

def main():
    # Initialise PyGame.
    pygame.init()

    # Initialise the clock.
    clock = pygame.time.Clock()

    #Initalise variables for Debug FPS Info.
    FPS = 60
    seconds = 0

    # Used to correctly implement seconds.
    pygame.time.set_timer(USEREVENT + 1, 1000)

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
    # Initialise the game.
    game = Game.Game(screenDim)
    # Initialise the Menu.
    menu = Menu.Menu(screenDim)

    # The current state of the game (1 = menu, 2 = game)
    currentState = 1
    # The next state of the game (0 = quit, 1 = menu, 2 = game)
    nextState = 1

    # Play the background music infinitely
    pygame.mixer.music.load('Assets/BackgroundMusic.ogg')
    #pygame.mixer.music.play(-1)

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

            # If the current state is the menu
            if currentState == 1:
                # Set the state of the game to the menu input.
                nextState = menu.input(event)

            # If the current state is the game
            elif currentState == 2:
                # Set the state of the game to the game input.
                nextState = game.input(event)

            # Check for the Input Event to toggle Debug mode.
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                displayDebug = not displayDebug

        # If the next state is still the same as the current state
        if currentState == nextState:
            # If the current state is the game
            if currentState == 2:
                # Set the state of the game to the game update.
                nextState = game.update(dt)

        # Clear the screen.
        screen.fill((252, 0, 0))

        # If the current state is the menu
        if currentState == 1:
            # Draw the menu to the screen.
            menu.draw(screen)

        # If the current state is the game
        elif currentState == 2:
            # Draw the game to the screen.
            game.draw(screen)

        # Display the Debug FPS Info.
        if displayDebug:
            screen.blit(rawtime_display, (10, 35))
            screen.blit(fps_display, (10, 60))
            screen.blit(pygame_total_ticks_display, (10, 85))
            screen.blit(seconds_display, (10, 110))
            screen.blit(time_display, (10, 135))

        # Double buffer the screen to the window.
        pygame.display.flip()

        # Set the value of the current state or end the game
        if nextState == 0:
            # Quit
            running = False
        elif nextState == 1:
            #If this is leaving a game set the girders to not spawn
            if nextState is not currentState:
                game.stopSpawing()
            # Menu
            currentState = 1
        elif nextState == 2:
            #If this is starting a new game set the girders to spawn
            if nextState is not currentState:
                game.reset()
            # Game
            currentState = 2


main()
quit()
