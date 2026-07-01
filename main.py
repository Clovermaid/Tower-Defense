import pygame
import json
import settings

pygame.init()

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption(settings.TITLE)

from assets import sprites
sprites.load_assets()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)                  
from scripts.tower import Tower
from scripts.game_map import GameMap
from scripts.wave import WaveManager
money = settings.STARTING_MONEY
game_map = GameMap()
lives = 10
wave_manager = WaveManager(game_map)
towers = []
bullets = []
MENU = 0
PLAYING = 1
GAME_OVER = 2
VICTORY = 3
selected_tower = "basic"
running = True
with open("data/towers.json", "r") as file:
    tower_data = json.load(file)
# main game loop
game_state = MENU
while running:

    # ==========================
    # Events
    # ==========================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if game_state == MENU:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = PLAYING

        elif game_state == PLAYING:
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:
                    selected_tower = "basic"

                elif event.key == pygame.K_2:
                    selected_tower = "sniper"

                elif event.key == pygame.K_3:
                    selected_tower = "machine"
            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_x, mouse_y = pygame.mouse.get_pos()

                if mouse_y < settings.UI_HEIGHT:
                    continue

                grid_x = (mouse_x // settings.TILE_SIZE) * settings.TILE_SIZE
                grid_y = ((mouse_y - settings.UI_HEIGHT) // settings.TILE_SIZE) * settings.TILE_SIZE
                grid_y += settings.UI_HEIGHT

                can_place = True

                for tower in towers:
                    if tower.x == grid_x and tower.y == grid_y:
                        can_place = False
                        break

                if (
                    can_place
                    and money >= tower_data[selected_tower]["cost"]
                    and game_map.can_build(grid_x, grid_y)
                ):
                    towers.append(Tower(grid_x, grid_y, selected_tower, tower_data))
                    money -= tower_data[selected_tower]["cost"]

        elif game_state == GAME_OVER:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:

                    money = settings.STARTING_MONEY
                    lives = 10

                    towers.clear()
                    bullets.clear()

                    game_map = GameMap()
                    wave_manager = WaveManager(game_map)

                    game_state = MENU
        elif game_state == VICTORY:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:

                    money = settings.STARTING_MONEY
                    lives = 10

                    towers.clear()
                    bullets.clear()

                    game_map = GameMap()
                    wave_manager = WaveManager(game_map)

                    game_state = MENU

    # ==========================
    # Update
    # ==========================

    if game_state == PLAYING:

        wave_manager.update()
        if wave_manager.finished:
            game_state = VICTORY
        for enemy in wave_manager.enemies[:]:

            finished = enemy.update()

            if enemy.health <= 0:
                money += enemy.reward
                wave_manager.enemies.remove(enemy)
                continue

            if finished:
                lives -= 1
                wave_manager.enemies.remove(enemy)

                if lives <= 0:
                    game_state = GAME_OVER

        for tower in towers:
            tower.update(wave_manager.enemies, bullets)

        for bullet in bullets[:]:

            finished = bullet.update()

            if finished:
                bullets.remove(bullet)

    # ==========================
    # Draw
    # ==========================

    screen.fill((30, 30, 30))

    if game_state == MENU:

        title = font.render("Tower Defense", True, (255,255,255))
        start = font.render("Press SPACE to Start", True, (255,255,255))

        screen.blit(title,(320,150))
        screen.blit(start,(250,250))

    elif game_state == PLAYING:

        game_map.draw(screen)

        pygame.draw.rect(
            screen,
            (45,45,45),
            (0,0,settings.WIDTH,settings.UI_HEIGHT)
        )
        money_text = font.render(
            f"{money}",
            True,
            (255,255,255)
        )
        tower_text = font.render(
            f"Tower: {selected_tower.title()} (1-3)",
            True,
            (255,255,255)
        )
        wave_text = font.render(
            f"Wave: {wave_manager.current_wave+1}",
            True,
            (255,255,255)
        )

        lives_text = font.render(
            f"{lives}",
            True,
            (255,255,255)
        )

        screen.blit(sprites.UI["coin"], (10, 12))
        screen.blit(money_text, (40, 20))

        screen.blit(sprites.UI["heart"], (140, 12))
        screen.blit(lives_text, (170, 20))

        screen.blit(wave_text, (280, 20))

        screen.blit(tower_text, (500, 20))

        for enemy in wave_manager.enemies:
            enemy.draw(screen)

        for tower in towers:
            tower.draw(screen)

        for bullet in bullets:
            bullet.draw(screen)

    elif game_state == GAME_OVER:

        screen.fill((20,0,0))

        title = font.render("GAME OVER", True, (255,255,255))
        restart = font.render("Press R to Restart", True, (255,255,255))

        screen.blit(title,(320,180))
        screen.blit(restart,(250,250))
    elif game_state == VICTORY:

        screen.fill((20,80,20))

        title = font.render(
            "YOU WIN!",
            True,
            (255,255,255)
        )

        restart = font.render(
            "Press R to Play Again",
            True,
            (255,255,255)
        )

        screen.blit(title,(350,180))
        screen.blit(restart,(250,250))

    pygame.display.flip()
    clock.tick(settings.FPS)

pygame.quit()