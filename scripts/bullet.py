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
        # 1. Safety check: make sure target exists and has health left
        # (Change .health to whatever health variable name you use in enemy.py)
        if self.target is None or getattr(self.target, 'health', 0) <= 0:
            return True # Delete bullet safely if enemy is dead

        dx = self.target.x - self.x
        dy = self.target.y - self.y

        # 2. Fast Check: Compare squared distance first (No square root yet!)
        dist_sq = dx ** 2 + dy ** 2
        speed_sq = self.speed ** 2

        # If the bullet is close enough to hit, deal damage immediately
        if dist_sq <= speed_sq:
            self.target.health -= self.damage
            return True # Target hit! Tell main script to delete bullet

        # 3. Only calculate the heavy square root if the bullet is still flying
        distance = dist_sq ** 0.5

        # Move bullet toward target
        self.x += dx / distance * self.speed
        self.y += dy / distance * self.speed

        return False # Bullet stays alive

    def draw(self, screen):
        screen.blit(
            sprites.BULLETS["bullet"],
            (self.x - 16, self.y - 16)
        )