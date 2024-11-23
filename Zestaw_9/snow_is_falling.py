import pygame
import random
from settings import *

def all_around_me():
    pygame.init()

    if FULLSCREEN:
        screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Children playing, having fun")

    clock = pygame.time.Clock()

pygame.init()

screen_width = 600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Topienie Płatków Śniegu")



# Czas gry
clock = pygame.time.Clock()

# Funkcja tworzenia płatka śniegu
def create_snowflake():
    x = random.randint(0, screen_width - snowflake_size)
    y = 0  # zaczynamy od góry ekranu
    return pygame.Rect(x, y, snowflake_size, snowflake_size)

# Funkcja rysująca płatki śniegu
def draw_snowflakes():
    for flake in snowflakes:
        pygame.draw.rect(screen, WHITE, flake)

# Funkcja sprawdzająca kolizję z kliknięciem myszy
def check_click(position):
    global snowflakes
    for flake in snowflakes[:]:
        if flake.collidepoint(position):
            snowflakes.remove(flake)

# Główna pętla gry
running = True
score = 0
while running:
    screen.fill(BLUE)  # tło gry

    # Wydarzenia (kliknięcia myszką i zamknięcie okna)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_click((mouse_x, mouse_y))

    # Tworzenie nowych płatków śniegu co określoną ilość klatek
    if random.randint(1, snowflake_spawn_rate) == 1:
        snowflakes.append(create_snowflake())

    # Spadanie płatków śniegu
    for flake in snowflakes[:]:
        flake.y += snowflake_speed
        if flake.y > screen_height:
            snowflakes.remove(flake)
            # Można dodać penalizację za przepuszczenie płatka

    # Rysowanie płatków śniegu
    draw_snowflakes()

    # Wyświetlanie wyniku
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Śnieg stopiony: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Aktualizacja ekranu
    pygame.display.flip()

    # Ustawienie liczby klatek na sekundę
    clock.tick(60)

pygame.quit()
