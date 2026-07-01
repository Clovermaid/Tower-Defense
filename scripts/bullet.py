import pygame
from assets import sprites
class Bullet:
    def __init__(self, x, y, target, damage):
        self.x = x
        self.y = y
        self.damage = damage
        self.target = target

        self.speed = 8
        self.radius = 5
    def update(self):

        if self.target is None:
            return True

        dx = self.target.x - self.x
        dy = self.target.y - self.y

        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance <= self.speed:
            self.target.health -= self.damage
            return True

        self.x += dx / distance * self.speed
        self.y += dy / distance * self.speed

        return False
    def draw(self, screen):
        screen.blit(

            sprites.BULLETS["bullet"],

            (self.x - 16, self.y - 16)
        )