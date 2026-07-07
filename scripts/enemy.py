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
        
        # Start precisely at the center of the first path node
        self.x = self.path[0][0]
        self.y = self.path[0][1]

    def update(self):
        if self.path_index >= len(self.path) - 1:
            return True 

        target_x, target_y = self.path[self.path_index + 1]

        # Calculate distances along the axes
        dx = target_x - self.x
        dy = target_y - self.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        # If we are close enough to the checkpoint, snap to it and switch targets
        if distance <= self.speed:
            self.x = target_x
            self.y = target_y
            self.path_index += 1
        else:
            # Normalize vector to ensure perfectly consistent diagonal speed
            self.x += (dx / distance) * self.speed
            self.y += (dy / distance) * self.speed
        
        return False

    def draw(self, screen):
        # LAZY FAIL-SAFE: Safely read sprite dictionary without crashing if asset is missing
        sprite = sprites.ENEMIES.get(self.enemy_type)

        if sprite:
            sprite_w = sprite.get_width()
            sprite_h = sprite.get_height()
            screen.blit(sprite, (self.x - sprite_w // 2, self.y - sprite_h // 2))
        else:
            # Fallback placeholder dimensions
            sprite_w, sprite_h = 18, 18
            pygame.draw.rect(screen, self.color, (self.x - 16, self.y - 16, 32, 32))

        # Health bar background positioning
        bar_y = self.y - sprite_h // 2 - 8
        pygame.draw.rect(screen, (255, 0, 0), (self.x - 20, bar_y, 40, 5))

        # Health bar foreground calculation
        if self.max_health > 0:
            health_ratio = max(0, min(1, self.health / self.max_health))
            pygame.draw.rect(screen, (0, 255, 0), (self.x - 20, bar_y, 40 * health_ratio, 5))
