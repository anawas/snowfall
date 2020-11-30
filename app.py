import pygame
import random

SPRITE_SIZE = 32


def get_image(x, y, width=32, height=32):
    image = pygame.Surface((width, height))
    image.set_colorkey((0,0,0))
    image.blit(sheet, (0,0), (x, y, width, height))
    return image

screen = pygame.display.set_mode((800, 800))

try: 
    sheet = pygame.image.load('Flakes1.png').convert()
except pygame.error as e:
    print(f"Unable to load spritesheet image")
    raise SystemExit(e)

flake_sprites = []

for x in range(0, 15):
    for y in range(0, 15):
        rect = pygame.Rect(0,0, 32, 32)
        flake_sprites.append(get_image(x*32, y*32))

for _ in range(200):
    index = random.randrange(0,10)
    xpos = random.randrange(32, 800-32)
    ypos = random.randrange(32, 800-32)
    screen.blit(flake_sprites[index], (xpos,  ypos, 32, 32))

while(True):
    pygame.display.flip()

