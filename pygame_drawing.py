# Drawing
# Author: Rachel
# Date: Jan 5, 2025

from zipfile import BadZipfile

import pygame


def game():
    pygame.init()

    # COLOURS - (R, G, B)
    # CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GREY = (128, 128, 128)

    # CONSTANTS
    WIDTH = 1920
    HEIGHT = 1080
    SIZE = (WIDTH, HEIGHT)

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Beautiful Drawing")

    # Variables
    done = False
    clock = pygame.time.Clock()

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC

        # ------ DRAWING TO SCREEN
        screen.fill(WHITE)  # background
        # Draw a rectangle in the middle of he screen
        # Make it red

        # Draw 7 purple lines from the top midde right of th screen
        # to the middle right of the screen
        # Repeats by translating down 75 px
        for offset in range(7):
            pygame.draw.line(
                screen,
                (228, 45, 216),
                (WIDTH / 2 + 20, 20 + offset * 75),
                (WIDTH - 20, HEIGHT / 2 - 20 + offset * 75),
            )
        # funky caterpillar
        pygame.draw.ellipse(screen, RED, (WIDTH / 2 - 50, HEIGHT / 2 - 50, 200, 100))
        pygame.draw.ellipse(
            screen, (255, 165, 0), (WIDTH / 2 - 50, HEIGHT / 2, 200, 100)
        )
        pygame.draw.ellipse(
            screen, (251, 208, 67), (WIDTH / 2 - 50, HEIGHT / 2 + 50, 200, 100)
        )
        pygame.draw.ellipse(
            screen, (132, 255, 115), (WIDTH / 2 - 50, HEIGHT / 2 + 100, 200, 100)
        )
        pygame.draw.ellipse(
            screen, (82, 219, 255), (WIDTH / 2 - 50, HEIGHT / 2 + 150, 200, 100)
        )
        pygame.draw.ellipse(
            screen, (210, 145, 255), (WIDTH / 2 - 50, HEIGHT / 2 + 200, 200, 100)
        )
        # flower center
        pygame.draw.circle(
            screen, (251, 208, 67), (WIDTH / 2 - 500, HEIGHT / 2 - 300), 50
        )
        pygame.draw.circle(
            screen, (210, 145, 255), (WIDTH / 2 - 500, HEIGHT / 2 - 200), 50
        )
        pygame.draw.circle(
            screen, (210, 145, 255), (WIDTH / 2 - 400, HEIGHT / 2 - 300), 50
        )

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60)  # 60 fps

    pygame.quit()


if __name__ == "__main__":
    game()
