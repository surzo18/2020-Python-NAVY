import pygame, sys
from pygame.locals import *
import numpy as np
import time

SLEEP_TIME = 0.5
BOARD_SIZE = 5
TALE_SIZE = 64
SCREEN_WIDTH = BOARD_SIZE * TALE_SIZE
SCREEN_HEIGHT = BOARD_SIZE * TALE_SIZE

white = (255,255,255)

images = {
    "mouse": pygame.image.load("./Utils/assets/mouse.png"),
    "trap": pygame.image.load("./Utils/assets/trap.png"),
    "cheese": pygame.image.load("./Utils/assets/cheese.png")
}

def mouse_render(path, matrix):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    current_index = 0

    while True:
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        mouse = path[current_index]
        traps = list(zip(*np.where(matrix == -1)))
        cheese = list(zip(*np.where(matrix == 100)))[0]

        surface = pygame.Surface((TALE_SIZE, TALE_SIZE))
        screen.blit(images["cheese"], surface.get_rect(topleft=tuple(x * TALE_SIZE for x in cheese)[::-1]))
        for trap in traps:
            screen.blit(images["trap"], surface.get_rect(topleft=tuple(x * TALE_SIZE for x in trap)[::-1]))
        screen.blit(images["mouse"], surface.get_rect(topleft=tuple(x * TALE_SIZE for x in mouse)[::-1]))

        pygame.display.update()
        if current_index + 1 < len(path):
            current_index += 1
        time.sleep(SLEEP_TIME)
