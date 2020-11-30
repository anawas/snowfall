import pygame
import random

SPRITE_SIZE = 32


def get_image(sheet, x, y, width=32, height=32):
    image = pygame.Surface((width, height))
    image.set_colorkey((0, 0, 0))
    image.blit(sheet, (0, 0), (x, y, width, height))
    return image


def event_handler(event_queue):
    for event in event_queue:
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
    return True


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    screen.fill((0, 0, 0))

    try:
        sheet = pygame.image.load('Flakes1.png').convert()
    except pygame.error as e:
        print(f"Unable to load spritesheet image")
        raise SystemExit(e)

    flake_sprites = []

    for x in range(0, 15):
        for y in range(0, 15):
            flake_sprites.append(get_image(sheet, x*32, y*32))

    for _ in range(200):
        index = random.randrange(0, 10)
        xpos = random.randrange(32, 800-32)
        ypos = random.randrange(32, 800-32)
        screen.blit(flake_sprites[index], (xpos,  ypos, 32, 32))

    clock = pygame.time.Clock()
    print('Entering game loop')
    running = True
    while(running):
        clock.tick(30)
        running = event_handler(pygame.event.get())

        pygame.display.flip()


if __name__ == "__main__":
    main()
