from gameObject import GameObject

# ENEMY CLASS
class Enemy(GameObject):
    # Static Constants
    START_POS_X_LEFT = 55
    START_POS_X_RIGHT = 745

    # Init Function
    def __init__(self, x, y, speed):
        # Generic properties
        self.DIRECTION_LEFT = -1
        self.DIRECTION_RIGHT = 1
        self.CURRENT_DIRECTION = 0

        if x == Enemy.START_POS_X_LEFT:
            self.CURRENT_DIRECTION = self.DIRECTION_RIGHT
        elif x == Enemy.START_POS_X_RIGHT:
            self.CURRENT_DIRECTION = self.DIRECTION_LEFT

        # Create underlying game object
        super().__init__(x, y, 50, 50, 'assets/enemy.png')

        # Set speed property
        self.speed = speed

    def move(self):
        if self.x >= 750:
            self.CURRENT_DIRECTION = self.DIRECTION_LEFT
        elif self.x <= 50:
            self.CURRENT_DIRECTION = self.DIRECTION_RIGHT
        self.x += self.CURRENT_DIRECTION * self.speed
# END ENEMY CLASS
