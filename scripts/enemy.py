import pygame
from assets import sprites
class Enemy:
    def __init__(self, enemy_type, enemy_data, path):
        stats = enemy_data[enemy_type]
        self.enemy_type = enemy_type
        self.health = stats["health"]
        self.max_health = self.health
        self.speed = stats["speed"]
        self.color = stats["color"]
        self.reward = stats["reward"]
        self.path_index = 0
        self.path = path
        self.width = stats["width"]
        self.height = stats["height"]
        self.x = self.path[0][0] - self.width // 2
        self.y = self.path[0][1] - self.height // 2

    def update(self):
        if self.path_index >= len(self.path) - 1:
            return True 

        target_x, target_y = self.path[self.path_index + 1]

        if self.x < target_x: self.x += self.speed 
        elif self.x > target_x: self.x -= self.speed
        if self.y < target_y: self.y += self.speed
        elif self.y > target_y: self.y -= self.speed

        if abs(self.x - target_x) < self.speed and abs(self.y - target_y) < self.speed:
            self.path_index += 1 
        
        return False
             

    def draw(self, screen):

        sprite = sprites.ENEMIES[self.enemy_type]

        screen.blit(
            sprite,
            (
                self.x - sprite.get_width() // 2,
                self.y - sprite.get_height() // 2,
            ),
        )

        # Health bar background
        pygame.draw.rect(
            screen,
            (255, 0, 0),
            (
                self.x - 20,
                self.y - sprite.get_height() // 2 - 8,
                40,
                5,
            ),
        )

        # Health bar
        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (
                self.x - 20,
                self.y - sprite.get_height() // 2 - 8,
                40 * (self.health / self.max_health),
                5,
            ),
        )