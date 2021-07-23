from gameObject import GameObject

# PLAYER CLASS
class Player(GameObject):
    def __init__(self):
        # Generic properties
        self.DIRECTION_UP = 1
        self.DIRECTION_DOWN = -1

        # Create underlying game object
        super().__init__(375, 615, 50, 50, 'assets/player.png')

        # Set speed property
        self.speed = 5

    # Move Function
    def move(self, direction):
        # Constrain player movement
        if self.y >= 635 and direction == self.DIRECTION_UP:
            direction = 0
        elif self.y <= 55 and direction == self.DIRECTION_DOWN:
            direction = 0

        # Make the move
        self.y += direction * self.speed
# END PLAYER CLASS
