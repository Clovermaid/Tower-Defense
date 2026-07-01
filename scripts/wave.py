import json
from scripts.enemy import Enemy
class WaveManager:
    def __init__(self, game_map):
        with open("data/enemies.json", "r") as file:
            self.enemy_data = json.load(file)
        with open("data/waves.json", "r") as file:
            self.waves = json.load(file)
        self.enemies = []
        self.game_map = game_map
        self.current_wave = 0
        self.spawn_index = 0
        self.spawn_timer = 0
        self.spawn_delay = 60
        self.finished = False
    def update(self):
        self.spawn_timer += 1
        current_wave = self.waves[self.current_wave]
        if self.spawn_timer >= self.spawn_delay:
            self.spawn_timer = 0
            if self.spawn_index < len(current_wave["enemies"]):
                self.wave_started = True
                enemy_type = current_wave["enemies"][self.spawn_index]
                enemy = Enemy(enemy_type,self.enemy_data,self.game_map.path)
                self.enemies.append(enemy)
                self.spawn_index += 1
        if (
        self.spawn_index >= len(current_wave["enemies"])
        and len(self.enemies) == 0
        ):
            if self.current_wave < len(self.waves) - 1:
                self.current_wave += 1
                self.spawn_index = 0
                self.spawn_timer = 0
                print("Starting Wave", self.current_wave + 1)
        elif (
            self.current_wave == len(self.waves)-1
            and self.spawn_index >= len(current_wave["enemies"])
            and len(self.enemies) == 0
        ):
            self.finished = True