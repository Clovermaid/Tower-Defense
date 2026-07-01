import os
import pygame

pygame.init()

# ==========================================
# Paths
# ==========================================

SCRIPT_DIR = os.path.dirname(__file__)

FOLDERS = [
    "tiles",
    "towers",
    "enemies",
    "bullets",
    "ui",
]

for folder in FOLDERS:
    os.makedirs(os.path.join(SCRIPT_DIR, folder), exist_ok=True)


# ==========================================
# Helpers
# ==========================================

SPRITE_SIZE = 32


def new_sprite():
    return pygame.Surface((SPRITE_SIZE, SPRITE_SIZE), pygame.SRCALPHA)


def save(surface, folder, filename):
    pygame.image.save(
        surface,
        os.path.join(SCRIPT_DIR, folder, filename + ".png")
    )


# ==========================================
# Pixel Helpers
# ==========================================

def pixel(surface, color, x, y, size=2):
    pygame.draw.rect(
        surface,
        color,
        (x * size, y * size, size, size)
    )


def rect(surface, color, x, y, w, h, size=2):
    pygame.draw.rect(
        surface,
        color,
        (x * size, y * size, w * size, h * size)
    )


def outline(surface):

    pygame.draw.rect(
        surface,
        (0, 0, 0),
        surface.get_rect(),
        1
    )


# ==========================================
# Tile Generator
# ==========================================

def generate_tiles():

    print("Generating tiles...")

    # Grass
    grass = new_sprite()
    grass.fill((70,170,70))

    for x, y in [
        (2,2),
        (8,5),
        (10,11),
        (5,13),
        (12,4),
        (3,9)
    ]:
        pixel(grass,(40,130,40),x,y)

    save(grass,"tiles","grass")


    # Path
    path = new_sprite()
    path.fill((170,120,70))

    for x,y in [
        (4,5),
        (10,3),
        (8,11),
        (13,8)
    ]:
        pixel(path,(130,90,50),x,y)
        pixel(path,(190,150,90),x+1,y+1)

    save(path,"tiles","path")


    # Water
    water = new_sprite()
    water.fill((50,120,255))

    pygame.draw.arc(
        water,
        (180,220,255),
        (4,8,8,6),
        0,
        3.14,
        2
    )

    pygame.draw.arc(
        water,
        (180,220,255),
        (18,18,8,6),
        0,
        3.14,
        2
    )

    save(water,"tiles","water")


    # Rock
    rock = new_sprite()
    rock.fill((120,120,120))

    pygame.draw.line(rock,(90,90,90),(8,6),(18,12),2)
    pygame.draw.line(rock,(90,90,90),(18,12),(14,22),2)

    save(rock,"tiles","rock")


    # Tree
    tree = new_sprite()

    tree.fill((70,170,70))

    pygame.draw.circle(tree,(20,100,20),(16,12),10)

    pygame.draw.rect(tree,(100,60,20),(14,18,4,10))

    save(tree,"tiles","tree")


# ==========================================
# UI
# ==========================================

def generate_ui():

    print("Generating UI...")

    heart = new_sprite()

    pygame.draw.polygon(
        heart,
        (255,0,0),
        [
            (16,28),
            (4,14),
            (8,6),
            (16,10),
            (24,6),
            (28,14)
        ]
    )

    save(heart,"ui","heart")


    coin = new_sprite()

    pygame.draw.circle(
        coin,
        (255,220,0),
        (16,16),
        8
    )

    pygame.draw.circle(
        coin,
        (255,255,120),
        (14,14),
        3
    )

    save(coin,"ui","coin")


# ==========================================
# Towers
# ==========================================

def generate_towers():

    print("Generating towers...")


    basic = new_sprite()

    pygame.draw.rect(basic,(90,90,90),(8,10,16,18))
    pygame.draw.rect(basic,(50,100,255),(10,6,12,8))

    save(basic,"towers","basic")


    sniper = new_sprite()

    pygame.draw.rect(sniper,(120,120,120),(10,10,12,18))
    pygame.draw.line(sniper,(70,70,70),(16,2),(16,16),3)
    pygame.draw.rect(sniper,(255,220,0),(10,4,12,4))

    save(sniper,"towers","sniper")


    machine = new_sprite()

    pygame.draw.rect(machine,(80,80,80),(8,10,16,18))
    pygame.draw.line(machine,(50,50,50),(12,2),(12,14),3)
    pygame.draw.line(machine,(50,50,50),(20,2),(20,14),3)

    save(machine,"towers","machine")


# ==========================================
# Enemies
# ==========================================

def generate_enemies():

    print("Generating enemies...")


    colours = {

        "basic": (60,220,60),

        "fast": (255,220,40),

        "tank": (70,120,255),

        "boss": (170,70,255)
    }

    for name, colour in colours.items():

        slime = new_sprite()

        pygame.draw.ellipse(
            slime,
            colour,
            (6,10,20,14)
        )

        pygame.draw.circle(slime,(0,0,0),(12,15),1)
        pygame.draw.circle(slime,(0,0,0),(20,15),1)

        save(slime,"enemies",name)


# ==========================================
# Bullets
# ==========================================

def generate_bullets():

    print("Generating bullets...")

    bullet = new_sprite()

    pygame.draw.circle(
        bullet,
        (255,255,0),
        (16,16),
        4
    )

    save(bullet,"bullets","bullet")


# ==========================================
# Generate Everything
# ==========================================

def generate_all():

    generate_tiles()
    generate_towers()
    generate_enemies()
    generate_bullets()
    generate_ui()

    print("\nDone! All assets generated.")


if __name__ == "__main__":
    generate_all()