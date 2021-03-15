# a package for building barriers
# coding:utf-8
# Author:The Crazy Turtle
# Date:2021/03/13

import pygame


class Bars:
    def __init__(self, image, surface, pos, size):
        self.WIN = surface
        self.pos = pos
        self.size = size
        self.image = image

    def create(self):
        pic = pygame.transform.smoothscale(pygame.image.load(self.image), self.size)
        self.WIN.blit(pic, self.pos)
