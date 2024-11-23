import pygame
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
FPS = 60
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)
SPAWN_TEMPO = 5

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Children playing, having fun")

snowflakes = []
gathered_snow = []

wind_blow = 0.5

class Snowflake:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = 0
        self.size = random.randint(15, 30)
        self.speed = random.uniform(1, 3)
        self.wind = random.uniform(-1.0, 1.0)
        self.isFalling = True
        self.melting = False
        self.melting_rate = random.uniform(0.1, 0.3)

    def fall(self, wind_blow):
        if self.isFalling:
            self.y += self.speed
            self.x += self.wind * wind_blow

            for snow in gathered_snow:
                if abs(self.x - snow.x) < self.size + snow.size and self.y + self.size >= snow.y:
                    self.y = snow.y - self.size
                    self.isFalling = False
                    gathered_snow.append(self)
                    return

            if self.y + self.size > SCREEN_HEIGHT:
                self.y = SCREEN_HEIGHT - self.size
                self.isFalling = False
                gathered_snow.append(self)

        if self.y <= 0:
            pygame.quit()
            exit()

    def melt(self):
        if self.melting:
            self.size -= self.melting_rate
            if self.size <= 0:
                if self in gathered_snow:
                    gathered_snow.remove(self)
                elif self in snowflakes:
                    snowflakes.remove(self)

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), max(0, int(self.size)))

def spawn_snowflakes():
    snowflakes.append(Snowflake())

def draw_snowflakes():
    for snowflake in snowflakes[:]:
        snowflake.fall(wind_blow)
        snowflake.draw()

def check_click():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for snowflake in snowflakes + gathered_snow:
        distance = ((snowflake.x - mouse_x) ** 2 + (snowflake.y - mouse_y) ** 2) ** 0.5
        if distance < snowflake.size:
            snowflake.melting = True

def adjust_snowpile():
    for snowflake in gathered_snow:
        if snowflake.isFalling:
            continue
        for other in gathered_snow:
            if snowflake != other and snowflake.y == other.y - snowflake.size and abs(snowflake.x - other.x) < snowflake.size:
                snowflake.x += random.choice([-1, 1]) * snowflake.size * 0.1

def all_around_me():
    global wind_blow
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(LIGHT_BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                check_click()

        if random.randint(1, SPAWN_TEMPO) == 1:
            spawn_snowflakes()

        wind_blow = random.uniform(0.5, 1.5)

        draw_snowflakes()
        for snowflake in gathered_snow + snowflakes:
            snowflake.melt()
        adjust_snowpile()
        for snow in gathered_snow:
            snow.draw()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    all_around_me()
