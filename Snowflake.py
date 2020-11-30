import random
import pygame
import math

class Snowflake:
    def __init__(self, screen, sprite):
        self.screen = screen
        self.sprite = sprite
        self.scr_width = screen.get_size()[0]
        self.scr_height = screen.get_size()[1]
        self.radius = 1
        self.velocity = 8
        self.frequency = random.randint(150, 300)
        self.x = random.randint(0, self.scr_width)
        self.y = random.randint(0, self.scr_height)
        self.z = random.randint(1, 5)
        self.color = self._set_color()

    def _set_color(self):
        gray_value = self.z * 40
        color_image = self.sprite.copy()
        color_image.convert_alpha()
        color_image.fill((gray_value, gray_value, gray_value))
        color_image.blit(self.sprite, (0,0), special_flags=pygame.BLEND_RGBA_MULT)
        return color_image

    def update(self):
        if self.off_screen():
            return
        self.screen.blit(self._set_color(), self.translate())

    def translate(self):
        self.y += self.z
        delta_x = 50 * math.sin(self.y/self.frequency + self.frequency/200)
        scr_x = self.x + delta_x
        scr_y = self.y 
        return (scr_x, scr_y, 32, 32)

    def off_screen(self):
        if self.y > self.scr_height:
            return True
        return False

