from random import randint
from enemy import Enemy

# ENEMY FACTORY CLASS
class EnemyFactory:
    # Static Properties
    X_START_LEFT = 55
    X_START_RIGHT = 745

    # Init Function
    def __init__(self):
        # Properties
        self.enemies = []
        self.level_speed_modifier = 0

    # Generate Enemy Function
    def generate_enemy(self, x, y):
        self.enemies.append(Enemy(x, y, randint(2, 6) + self.level_speed_modifier))

    def move_enemies(self):
        for enemy in self.enemies:
            enemy.move()

    def destruct(self):
        self.enemies.clear()

    def set_level_speed_modifier(self, level_speed_modifier):
        self.level_speed_modifier = level_speed_modifier
# END ENEMY FACTORY CLASS
