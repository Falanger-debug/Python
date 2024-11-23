import pygame
import random

from Snowflake import Snowflake
from settings import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Children playing, having fun")

snowflakes = []



def draw_snowflakes():
    for snowflake in snowflakes:
        if snowflake.isFalling:
            snowflake.fall()
            snowflake.draw()
        elif snowflake.exists:
            snowflake.draw()
        else:
            snowflakes.remove(snowflake)

def spawn_snowflakes():
    if len(snowflakes) < SPAWN_TEMPO:
        snowflakes.append(Snowflake())

def all_around_me():
    global snowflakes

    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill(LIGHT_BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        spawn_snowflakes()

        for snowflake in snowflakes:
            snowflake.fall()
        draw_snowflakes()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    all_around_me()
