import pygame
import os
print("Loaded sprites.py from:", __file__)
BASE = os.path.dirname(__file__)

TILES = {}
TOWERS = {}
ENEMIES = {}
UI = {}
BULLETS = {}


def load_assets():

    global TILES, TOWERS, ENEMIES, UI, BULLETS

    def load(folder, name):
        return pygame.image.load(
            os.path.join(BASE, folder, name + ".png")
        ).convert_alpha()

    TILES = {
        "grass": load("tiles", "grass"),
        "path": load("tiles", "path"),
        "water": load("tiles", "water"),
        "rock": load("tiles", "rock"),
        "tree": load("tiles", "tree"),
    }

    TOWERS = {
        "basic": load("towers", "basic"),
        "sniper": load("towers", "sniper"),
        "machine": load("towers", "machine"),
    }

    ENEMIES = {
        "basic": load("enemies", "basic"),
        "fast": load("enemies", "fast"),
        "tank": load("enemies", "tank"),
        "boss": load("enemies", "boss"),
    }

    UI = {
        "heart": load("ui", "heart"),
        "coin": load("ui", "coin"),
    }

    BULLETS = {
        "bullet": load("bullets", "bullet"),
    }