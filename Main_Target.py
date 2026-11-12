# 1 - Import packages
import pygame
from pygame.locals import *
from Target_Manager import TargetManager
import sys

# 2 - Define constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30
N_TARGET = 3

GREY = (200, 200, 200)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()


# 4 - Load assets: image(s), sounds, etc.
font = pygame.font.Font(None, 36)


# 5 - Initialize variables
score = 0

Target_Manager = TargetManager(window, WINDOW_WIDTH, WINDOW_HEIGHT, N_TARGET)
# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if Target_Manager.handle_event(event):
            score = score + 1

    # 8 - Do any "per frame" actions

    # 9 - Clear the window before drawing it again
    window.fill(GREY)


    # 10 - Draw the window elements
    #score board (x, y, width, heigth)
    pygame.draw.rect(window, WHITE, (325, 15, 150, 45))
    score_text = font.render("Score: " + str(score), True, BLACK)
    window.blit(score_text, (345, 22))

    Target_Manager.draw_all()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)