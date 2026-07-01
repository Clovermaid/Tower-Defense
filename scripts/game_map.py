import json
import pygame
import settings
from assets import sprites

# Information about each tile
TILES = {
    0: {"name": "Grass", "buildable": True,  "sprite": "grass"},
    1: {"name": "Path",  "buildable": False, "sprite": "path"},
    2: {"name": "Spawn", "buildable": False, "sprite": "path"},
    3: {"name": "Goal",  "buildable": False, "sprite": "path"},
    4: {"name": "Water", "buildable": False, "sprite": "water"},
    5: {"name": "Rock",  "buildable": False, "sprite": "rock"},
    6: {"name": "Tree",  "buildable": False, "sprite": "tree"},
}


class GameMap:

    def __init__(self):

        with open("data/map.json", "r") as file:
            data = json.load(file)

        self.tile_size = settings.TILE_SIZE
        self.tiles = data["tiles"]

        # Enemy path
        self.path = []

        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[row])):

                tile = self.tiles[row][col]

                if tile in (1, 2, 3):

                    x = col * self.tile_size + self.tile_size // 2
                    y = (
                        row * self.tile_size
                        + self.tile_size // 2
                        + settings.UI_HEIGHT
                    )

                    self.path.append((x, y))

    def draw(self, screen):

        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[row])):

                tile = self.tiles[row][col]

                x = col * self.tile_size
                y = row * self.tile_size + settings.UI_HEIGHT

                sprite_name = TILES[tile]["sprite"]
                sprite = sprites.TILES[sprite_name]

                screen.blit(sprite, (x, y))

    def can_build(self, x, y):

        col = x // self.tile_size
        row = (y - settings.UI_HEIGHT) // self.tile_size

        if row < 0 or row >= len(self.tiles):
            return False

        if col < 0 or col >= len(self.tiles[0]):
            return False

        tile = self.tiles[row][col]

        return TILES[tile]["buildable"]