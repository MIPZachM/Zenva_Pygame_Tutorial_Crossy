import pygame

from gameObject import GameObject
from player import Player
from enemyFactory import EnemyFactory


# GAME CLASS
class Game:
    def __init__(self):
        # Generic Properties
        self.WHITE_COLOR = (255, 255, 255)
        self.DIRECTION_UP = -1
        self.DIRECTION_DOWN = 1
        self.DIRECTION_NEUTRAL = 0

        # Specific Properties
        self.screen_width = 800
        self.screen_height = 700
        self.advance_level = False
        self.game_over = False
        self.current_level = 1
        self.level_speed_modifier = 1

        pygame.display.set_caption("Zenva Learning PyGame")
        self.game_window = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.enemyFactory = EnemyFactory()
        self.enemyFactory.set_level_speed_modifier(self.level_speed_modifier)

        self.background = GameObject(0, 0, self.screen_width, self.screen_height, 'assets/background.png')
        self.treasure = GameObject(375, 50, 50, 50, 'assets/treasure.png')
        self.player = Player()

        self.enemyFactory.generate_enemy(EnemyFactory.X_START_LEFT, 200)
        self.enemyFactory.generate_enemy(EnemyFactory.X_START_LEFT, 400)
        self.enemyFactory.generate_enemy(EnemyFactory.X_START_LEFT, 500)
        self.enemyFactory.generate_enemy(EnemyFactory.X_START_RIGHT, 100)
        self.enemyFactory.generate_enemy(EnemyFactory.X_START_RIGHT, 300)

    # Reset Stage Function
    def reset_stage(self):
        self.treasure = GameObject(375, 50, 50, 50, 'assets/treasure.png')
        self.player = Player()

        self.enemyFactory.generate_enemy(EnemyFactory.X_START_LEFT, 200)
        self.enemyFactory.generate_enemy(EnemyFactory.X_START_LEFT, 400)
        self.enemyFactory.generate_enemy(EnemyFactory.X_START_LEFT, 500)
        self.enemyFactory.generate_enemy(EnemyFactory.X_START_RIGHT, 100)
        self.enemyFactory.generate_enemy(EnemyFactory.X_START_RIGHT, 300)

    # Detect Collision Function
    @staticmethod
    def detect_collision(obj_1, obj_2):
        # Check overlap on Y-axis
        if obj_1.y > (obj_2.y + obj_2.height):
            return False
        elif (obj_1.y + obj_1.height) < obj_2.y:
            return False

        # Check overlap on X-axis
        if obj_1.x > (obj_2.x + obj_2.width):
            return False
        elif (obj_1.x + obj_1.width) < obj_2.x:
            return False

        return True

    # Game Loop Function
    def run_game_loop(self):
        # Set initial properties
        moving_direction = self.DIRECTION_NEUTRAL
        if self.advance_level:
            self.current_level += 1
            self.advance_level = False

        # Start loop
        while True:
            if self.game_over:
                self.enemyFactory.destruct()
                self.reset_stage()
                self.game_over = False
                self.current_level = 1
                self.advance_level = False
                self.enemyFactory.set_level_speed_modifier(1)
            # Set game caption @ current level
            pygame.display.set_caption("Zenva Learning PyGame Level {}".format(self.current_level))

            # Handle events
            events = pygame.event.get()
            for event in events:
                # Quit Game Event
                if event.type == pygame.QUIT:
                    return
                # Key Down Event
                elif event.type == pygame.KEYDOWN:
                    # Up Arrow
                    if event.key == pygame.K_UP:
                        moving_direction = self.DIRECTION_UP
                    # Down Arrow
                    elif event.key == pygame.K_DOWN:
                        moving_direction = self.DIRECTION_DOWN
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        moving_direction = self.DIRECTION_NEUTRAL

            # Init default background
            self.game_window.fill(self.WHITE_COLOR)

            # Execute logic
            self.enemyFactory.move_enemies()
            self.move_player(moving_direction)
            self.draw_images()

            # Update display
            pygame.display.update()

            # Check Collision
            for enemy in self.enemyFactory.enemies:
                if self.detect_collision(self.player, enemy):
                    self.advance_level = False
                    self.game_over = True
                    break

            if self.detect_collision(self.player, self.treasure):
                self.advance_level = True
                break

            self.clock.tick(60)

        if self.advance_level:
            self.enemyFactory.destruct()
            self.enemyFactory.set_level_speed_modifier(5 * (self.current_level / 5))
            self.reset_stage()
            self.run_game_loop()

    # Draw Images Function
    def draw_images(self):
        self.game_window.blit(self.background.image, (self.background.x, self.background.y))
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))

        for enemy in self.enemyFactory.enemies:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))

    # Move Player Function
    def move_player(self, move_direction):
        self.player.move(move_direction)
# END GAME CLASS
