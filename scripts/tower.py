from assets import sprites
from scripts.bullet import Bullet
class Tower:
    def __init__(self, x, y, tower_type, tower_data):
        stats = tower_data[tower_type]
        self.type = tower_type
        self.x = x
        self.y = y

        self.damage = stats["damage"]
        self.range = stats["range"]
        self.fire_rate = stats["fire_rate"]
        self.size = stats["size"]
        self.color = stats["color"]
        self.cost = stats["cost"]
        self.target = None

        self.cooldown = 0

    def update(self, enemies, bullets):
        if self.cooldown > 0:
            self.cooldown -= 1

        # 1. If target died or left the game, clear it
        if self.target not in enemies:
            self.target = None

        tower_x = self.x + self.size // 2
        tower_y = self.y + self.size // 2
        range_sq = self.range ** 2

        # 2. Check if current target is still in range
        if self.target:
            dx = self.target.x - tower_x
            dy = self.target.y - tower_y
            if (dx ** 2 + dy ** 2) > range_sq:
                self.target = None # Out of range, drop target

        # 3. ONLY scan the enemy list if we need a new target (O(1) most frames!)
        if not self.target and len(enemies) > 0:
            closest_dist_sq = float("inf")
            for enemy in enemies:
                dx = enemy.x - tower_x
                dy = enemy.y - tower_y
                dist_sq = dx ** 2 + dy ** 2

                if dist_sq < closest_dist_sq:
                    closest_dist_sq = dist_sq
                    self.target = enemy

        # 4. Attack the locked target
        if self.target and self.cooldown == 0:
            # Double check distance one last time before firing
            dx = self.target.x - tower_x
            dy = self.target.y - tower_y
            if (dx ** 2 + dy ** 2) <= range_sq:
                bullets.append(Bullet(tower_x, tower_y, self.target, self.damage))
                self.cooldown = self.fire_rate

    def draw(self, screen):
        screen.blit(

            sprites.TOWERS[self.type],

            (self.x - 16, self.y - 16)
        )