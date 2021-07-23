import pygame

# GAME OBJECT CLASS
class GameObject:
    def __init__(self, x, y, width, height, img_path):
        # Create pygame image
        image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(image, (width, height))

        # Set properties
        self.x = x
        self.y = y
        self.width = width
        self.height = height
# END GAME OBJECT CLASS
