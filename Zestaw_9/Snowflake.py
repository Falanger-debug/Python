import random
import pygame

from snow_is_falling import *


class Snowflake:

    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = 0
        self.size = random.randint(15, 30)
        self.speed = random.uniform(1, 3)
        self.wind = random.uniform(-0.5, 0.5)
        self.isFalling = True
        self.exists = True

    def fall(self):
        self.y += self.speed
        self.x += self.wind
        if self.y > SCREEN_HEIGHT:
            self.isFalling = False

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.size)

