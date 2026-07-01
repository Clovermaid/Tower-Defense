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

        self.cooldown = 0

    def update(self, enemies, bullets):
        if self.cooldown > 0:
            self.cooldown -= 1

        if len(enemies) == 0:
            return

        closest_enemy = None
        closest_distance = float("inf")

        # Centre of the tower
        tower_x = self.x + self.size // 2
        tower_y = self.y + self.size // 2

        for enemy in enemies:
            dx = enemy.x - tower_x
            dy = enemy.y - tower_y
            distance = (dx ** 2 + dy ** 2) ** 0.5

            if distance < closest_distance:
                closest_distance = distance
                closest_enemy = enemy

        if (
            closest_enemy
            and closest_distance <= self.range
            and self.cooldown == 0
        ):
            bullets.append(Bullet(tower_x, tower_y, closest_enemy, self.damage))
            self.cooldown = self.fire_rate

    def draw(self, screen):
        screen.blit(

            sprites.TOWERS[self.type],

            (self.x - 16, self.y - 16)
        )